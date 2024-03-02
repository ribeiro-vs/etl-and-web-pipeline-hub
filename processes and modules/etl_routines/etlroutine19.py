import pandas as pd
import json
import requests
import json 
import requests
from plconfig import SecInfo, MachineInfo as machine_info
from datetimetools import Metabase_date_format,Alternative_date_variables
from etltools import SnowFlakeToDF
from verifiers import process_registrant

sec = SecInfo()
date = Metabase_date_format()
adate= Alternative_date_variables()

dates = [
 [date.yesterday,10]
,[date.yesterday,15]
]

total_pedidos = 0
total_pedidos_cancelados = 0
soma_vendas = 0.0
soma_vendas_canceladas = 0.0

# functions that will generate the data

for date_filtered,warehouse_num in dates:

    # current_month
    query = f"""
    SELECT * FROM {sec.sh_view}
    WHERE DATETIME_DELIVERY LIKE '{date_filtered}%'
    """
    data  = SnowFlakeToDF(query)
    sh_df = data.create_df()

    logpath  = r'G:'+machine_info().pathlang3+r'\API KEYS\logs\scantech_batches_'+date.yesterday+r'.txt'

    jsonpath = r'G:'+machine_info().pathlang3+r'\API KEYS\jsons\all_orders_warehouse_'+str(warehouse_num)+'_'+date.yesterday+r'.json'
    
    username = sec.sh_usr
    password = sec.sh_pss

    if warehouse_num == 10:
        url = sec.sh_burl1  
        aurl= sec.sh_aurl1
    else:
        url = sec.sh_burl2
        aurl= sec.sh_aurl2

    # Function to create delivered orders

    def create_order_json_adjusted(order_group):

        formatted_date = order_group['DATETIME_DELIVERY'].iloc[0].strftime('%Y-%m-%dT%H:%M:%S.000-0300')
        descuentoTotal = sum((row['LOYALTY_DISCOUNT_APPLIED']*row['QUANTITY_FULFILLED_PZ']) if row['LOYALTY_DISCOUNT_APPLIED'] >= 1.0 else 0.0 for _, row in order_group.iterrows())
        detalles_list = []

        for _, row in order_group.iterrows():

            cantidad = round(row['QUANTITY_ORDERED_PZ'],2) if ((row['QUANTITY_FULFILLED_PZ'] == 0) & (row['GMV'] != 0)) else round(row['QUANTITY_FULFILLED_PZ'],2)

            detalles_list.append({
                "codigoArticulo": str(row['PRODUCT_ID']),
                "codigoBarras": str(row['EAN']),
                "descripcionArticulo": row['PRODUCT'],
                "cantidad": cantidad,
                "importeUnitario": round((((row['GMV'] / cantidad if cantidad != 0 else 0.0)+(row['LOYALTY_DISCOUNT_APPLIED'] if row['LOYALTY_DISCOUNT_APPLIED'] >= 1.0 else 0.0) if row['GMV'] != 0.0 else 0.1)),2),
                "importe": round((row['GMV']),2),
                "descuento": round((row['LOYALTY_DISCOUNT_APPLIED']*row['QUANTITY_FULFILLED_PZ']),2),
                "recargo": 0.00
            })

        order_json = {
            "fecha": formatted_date,
            "numero": int(order_group['ORDER_ID'].iloc[0]),
            "descuentoTotal": round(descuentoTotal, 2), 
            "recargoTotal": 0.00,
            "codigoMoneda": "986",
            "cotizacion": 1.00,
            "total": round(order_group['GMV'].sum(),2),
            "cancelacion": False,
            "documentoCliente": None,
            "codigoCanalVenta": 2,
            "descripcionCanalVenta": "ECOMMERCE",
            "detalles": detalles_list,
            "pagos": [
                {
                    "codigoTipoPago": 9,
                    "codigoMoneda": "986",
                    "importe": round(order_group['GMV'].sum(),2),
                    "cotizacion": 1.00,
                    "documentoCliente": None,
                    "bin": None,
                    "ultimosDigitosTarjeta": None,
                    "numeroAutorizacion": None,
                    "codigoTarjeta": None
                }
            ]
        }
        return order_json

    # Function to create canceled orders

    def create_cancelled_order_json_adjusted(order_group):
        
        formatted_date = order_group['DATETIME_DELIVERY'].iloc[0].strftime('%Y-%m-%dT%H:%M:%S.000-0300')
        descuentoTotal = sum((row['LOYALTY_DISCOUNT_APPLIED']*row['QUANTITY_ORDERED_PZ']) if row['LOYALTY_DISCOUNT_APPLIED'] >= 1.0 else 0.0 for _, row in order_group.iterrows())
        
        order_json_false = {
            "fecha": formatted_date,
            "numero": int(order_group['ORDER_ID'].iloc[0]),
            "descuentoTotal": round(descuentoTotal, 2),
            "recargoTotal": 0.00,
            "codigoMoneda": "986",
            "cotizacion": 1.00,
            "total": round(order_group['GMVP'].sum(),2),
            "cancelacion": False,
            "documentoCliente": None,
            "codigoCanalVenta": 2,
            "descripcionCanalVenta": "ECOMMERCE",
            "detalles": [ 
                {
                    "codigoArticulo": str(row['PRODUCT_ID']),
                    "codigoBarras": str(row['EAN']),
                    "descripcionArticulo": row['PRODUCT'],
                    "cantidad": round(row['QUANTITY_ORDERED_PZ'],2),
                    "importeUnitario": round((((row['GMVP'] / row['QUANTITY_ORDERED_PZ'] if row['QUANTITY_ORDERED_PZ'] != 0 else 0.0)+(row['LOYALTY_DISCOUNT_APPLIED'] if row['LOYALTY_DISCOUNT_APPLIED'] >= 1.0 else 0.0) if row['GMVP'] != 0.0 else 0.1)),2),
                    "importe": round((row['GMVP'] if row['GMVP'] != 0.0 else 0.1),2),
                    "descuento": round((row['LOYALTY_DISCOUNT_APPLIED']*row['QUANTITY_ORDERED_PZ']),2),
                    "recargo": 0.0
                }
                for _, row in order_group.iterrows()
            ],
            "pagos": [
                {
                    "codigoTipoPago": 9,
                    "codigoMoneda": "986",
                    "importe": round(order_group['GMVP'].sum(),2),
                    "cotizacion": 1.00,
                    "documentoCliente": None,
                    "bin": None,
                    "ultimosDigitosTarjeta": None,
                    "numeroAutorizacion": None,
                    "codigoTarjeta": None
                }
            ]
        } 

        order_json_true = order_json_false.copy()
        order_json_true["numero"] = "-"+str(int(order_group['ORDER_ID'].iloc[0]))
        order_json_true["cancelacion"] = True

        return order_json_false,order_json_true

    # Function to divid orders into batches

    def divide_into_batches(order_list, batch_size):
        return [order_list[i:i + batch_size] for i in range(0, len(order_list), batch_size)]


    def process_orders_to_batches(df_arg, batch_size=300, specified_date=None):

        global total_pedidos
        global total_pedidos_cancelados
        global soma_vendas
        global soma_vendas_canceladas

        sales_df = df_arg

        mask = (sales_df['STATUS_PICKING'].str.startswith('fulfilled')) & (sales_df['STATUS_ORDER'] == 'delivered') & (sales_df['GMV'] == 0)
        sales_df.loc[mask, 'UNIT_PRICE'] = 0.1
        sales_df.loc[mask, 'GMV'] = sales_df['QUANTITY_FULFILLED_PZ'] * sales_df['UNIT_PRICE']
        sales_df = sales_df[(sales_df['PRODUCT_ID'] != 12466)] 
        sales_df = sales_df[(sales_df['STORE_ID'] == warehouse_num)]
        
        if specified_date:
            sales_df = sales_df[sales_df['DATETIME_DELIVERY'].dt.strftime('%Y-%m-%d') == specified_date]

        grouped_orders = sales_df.groupby('ORDER_ID')
        order_json_list = []

        for _, group in grouped_orders:

            total_pedidos += 1
             
            process_registrant.register_info(f"Processando pedido: {group['ORDER_ID'].iloc[0]}")
            process_registrant.register_info(f"Status dos itens no pedido: {group['STATUS_ORDER'].unique()}")
            
            if (group['STATUS_ORDER'] != 'delivered').all():

                total_pedidos_cancelados += 1
                soma_vendas_canceladas += group['GMVP'].sum()

                process_registrant.register_info("Pedido totalmente cancelado.")
                json_cancelled = create_cancelled_order_json_adjusted(group)
                order_json_list.extend(json_cancelled)
            else:

                soma_vendas += group['GMV'].sum()
                
                group['STATUS_PICKING'] = group['STATUS_PICKING'].fillna('')
                group = group[(group['STATUS_PICKING'].str.startswith('fulfilled'))]
                process_registrant.register_info("Pedido contém itens entregues ou outros status.")
                try:
                    order_json_list.append(create_order_json_adjusted(group))
                except:
                    pass

        metrics_df = pd.DataFrame({
            'Data': [date_filtered],
            'Total Pedidos': [total_pedidos],
            'Total Pedidos Cancelados': [total_pedidos_cancelados],
            'Soma Vendas': [soma_vendas],
            'Soma Vendas Canceladas': [soma_vendas_canceladas],
            'Warehouse': [str(warehouse_num)]
        })
        metrics_df.to_csv(r'G:'+machine_info().pathlang0+r'\Data & Performance\Relatórios de Empresas Parceiras\SCANTECH\scantech_summary_'+date_filtered+r'_warehouse_'+str(warehouse_num)+r'.csv', index=False)

        order_batches = divide_into_batches(order_json_list, batch_size)

        return order_batches

    # Sending the orders data to Scantech
    
    def ler_lotes_do_json(json_file_path):
        """
        Reads the batches of orders in the JSON file
        """
        with open(json_file_path, 'r') as file:
            lotes = json.load(file)
        return lotes

    def enviar_lote(lote, url, username, password, file):
        """
        Sends a batch of orders to the API and registers the responses in a file.
        """
    
        response = requests.post(
            url,
            auth=(username, password),
            headers={'Content-Type': 'application/json','pdv-version': '1.0.0','backEnd-version': '1.0.0'},
            json=lote
        )

        if response.status_code == 200:
            process_registrant.register_info("Succeeded when sending batch: "+ str(response.json()))
            file.write("Succeeded when sending batch: " + str(response.json()) + "\n")
        else:
            "Failed when sending batch: {} - {}".format(response.status_code, response.text)
            process_registrant.register_error("Failed when sending batch: {} - {}".format(response.status_code, response.text))
            file.write("Failed when sending batch: " + str(response.status_code) + " " + response.text + "\n")

    def enviar_todos_os_lotes(json_file_path, nome_arquivo):
        """
        Reads the batches of orders in a JSON and sends it, one by one.
        Registers the execution in a file.
        """
        lotes = ler_lotes_do_json(json_file_path)

        with open(nome_arquivo, 'w') as file:
            for i, lote in enumerate(lotes, start=1):
                process_registrant.register_info(f"Sending batch {i} of {len(lotes)}...")
                file.write(f"Sending batch {i} of {len(lotes)}...\n")
                enviar_lote(lote, url, username, password, file)


    # Generation of json data source

    result = process_orders_to_batches(sh_df, batch_size=300, specified_date=date_filtered)
    with open(jsonpath, 'w') as f:
        json.dump(result, f, indent=4)


    # Sending orders batches data to Scantech

    enviar_todos_os_lotes(jsonpath, logpath)


    # Sending the aggregate of the day to Scantech

    monto_venta_liquida = soma_vendas 
    monto_cancelaciones = soma_vendas_canceladas
    cantidad_movimientos = total_pedidos
    cantidad_cancelaciones = total_pedidos_cancelados


    fecha_ventas = date_filtered
    fechamento_diario = {
        "montoVentaLiquida": round(monto_venta_liquida, 2),
        "montoCancelaciones": round(monto_cancelaciones, 2),
        "cantidadMovimientos": cantidad_movimientos,
        "fechaVentas": fecha_ventas,
        "cantidadCancelaciones": cantidad_cancelaciones
    }   

    new = aurl                   
    url_fechamento_diario = new

    response = requests.post(
        url_fechamento_diario,
        auth=(username, password),
        headers={'Content-Type': 'application/json','pdv-version': '1.0.0','backEnd-version': '1.0.0'},
        json=fechamento_diario
    )
    process_registrant.register_info(fechamento_diario)

    # for data outside the batch format the response comes empty
    if response.status_code == 200:
        process_registrant.register_info("Success sending the aggregate of the day.")
        process_registrant.register_info("Response details:")
        process_registrant.register_info(f"Headers: {response.headers}")
        process_registrant.register_info(f"Response body: {response.text}")  
            
    else:
        process_registrant.register_error(f"Failed sending the aggregate of the day: {response.status_code}")
        process_registrant.register_info("Response details:")
        process_registrant.register_info(f"Headers: {response.headers}")
        process_registrant.register_info(f"Response body: {response.text}")  