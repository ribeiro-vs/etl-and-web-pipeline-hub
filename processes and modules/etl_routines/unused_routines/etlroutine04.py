import pandas as pd
from plconfig import MachineInfo
from datetime import timedelta
from datetime import datetime
from datetimetools import Alternative_date_variables as ad

mi = MachineInfo()
pd.options.display.float_format = '{:,.2f}'.format
origin_file = r'G:'+mi.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\ENVIO PESQUISAS\fraud_prevention_tool_br___all_orders_'+str(ad().year_month)+'.csv'
original_source = pd.read_csv(origin_file)

df0 = original_source[['phone','name','user_id','Succesful purchases','delivery_date','order_id','order_status','store']]
df0 = df0.rename(columns = {'Succesful purchases':'succesful_purchase'})
df0 = df0[

    (df0['order_status'] == 'delivered')

]

df0 = df0.sort_values('delivery_date')
df0['delivery_date'] = pd.to_datetime(df0['delivery_date'])

three_days_ago = pd.Timestamp.now() - timedelta(days=3)

df0 = df0[
    (df0['delivery_date'].dt.date == three_days_ago.date())
]

df0['delivery_date_new_format'] = df0['delivery_date'].dt.strftime('%d-%m-%y')
df0['delivery_date'] = df0['delivery_date'].dt.strftime('%d-%m-%Y')

df0 = df0.drop('order_status', axis=1)

df0['name'] = df0['name'].str.split().str[0]

df0.drop_duplicates(subset='user_id', inplace=True)

df0['today'] = pd.Timestamp.now()
df0['today'] = df0['today'].dt.strftime('%d-%m-%Y')
df0['delivery_date'] = pd.to_datetime(df0['delivery_date'])
df0['delivery_date_new_format'] = df0['delivery_date'].dt.strftime('%d-%m-%y')
df0['delivery_date'] = df0['delivery_date'].dt.strftime('%d-%m-%Y')

df0['all_info'] = df0.apply(lambda row: f'user_id={row["user_id"]}&num_of_orders={row["succesful_purchase"]}&date_last_order={row["delivery_date"]}&store={row["store"]}&datadeenvio={row["today"]}&order={row["order_id"]}', axis=1)

df0 = df0[['phone','name','all_info']]

now = datetime.now()
today_date = now.strftime('%Y_%m_%d')

df0.to_excel(r'G:'+mi.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\ENVIO WHATSAPP\envio_bot_maker_'+today_date+'.xlsx', index=False)
