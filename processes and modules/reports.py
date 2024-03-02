from plconfig import MachineInfo
from pathlib import Path
from datetimetools import Metabase_date_format,Alternative_date_variables,Time_formats

"""
    It is strictly for the purposes of:
        - Define reports used in each type of automation
"""   

class ReportBase:
    def __init__(self):
        self.time_formats = Time_formats()
        self.metabase_date_format = Metabase_date_format()
        self.machine_info = MachineInfo()
        self.alternative_date_variables = Alternative_date_variables()
        self.instant_notification = False  # Pode ser definido como True ou False nas classes filhas
        self.channel = 'bot_channel'
        self.forced_try = True
        self.name = None  # Definir nas classes filhas
        self.original_file_name = None  # Definir nas classes filhas
        self.gkey = None  # Opcional, usar se necessário nas classes filhas
        self.gsheet = None  # Opcional, usar se necessário nas classes filhas
        self.sheets_report = None  # Pode ser definido como True ou False nas classes filhas

# Metabase

class MReport01(ReportBase):
    instant_notification=True
    name='Avanço do Dia Por Armazém SD'
    original_file_name='avanco_do_dia_por_armazem'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios Last Mile\0 - AVANCO DO DIA POR ARMAZEM\avanco_do_dia_por_armazem_'+self.time_formats.hour+r'h.xlsx')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/1407-avanco-do-dia-por-armazem?almacen=10&date='+self.metabase_date_format.today
        return result
    limit_time = 200
   
class MReport02(ReportBase):
    instant_notification=True 
    name='Closed Delivered By Warehouse SD'
    original_file_name='closed___delivered_by_warehouse'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios Last Mile\1 - CLOSED DELIVERED BY WAREHOUSE\closed_delivered_by_warehouse_'+self.time_formats.hour+r'h.xlsx')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/1375-closed-delivered-by-warehouse?almacen=10&date='+self.metabase_date_format.today  
        return result
    limit_time=200
    
class MReport03(ReportBase):
    instant_notification=True
    name='Linhas Para Pickear Armazém Separado Por Pasillo SD'
    original_file_name='linhas_para_pickear_armazem'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios Last Mile\2 - LINHAS PARA PICKEAR ARMAZEM SEPARADO POR PASILLO\linhas_para_pickear_armazem_separado_por_pasillo_'+self.time_formats.hour+r'h.xlsx')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/2369-linhas-para-pickear-armazem-separado-por-pasillo?date='+self.metabase_date_format.today+'&Armazen=10'
        return result  
    limit_time=200

class MReport04(ReportBase):
    instant_notification=True
    channel='alertas_last_mile'    
    name='Avanço do Dia Por Armazém NM'
    original_file_name='avanco_do_dia_por_armazem'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios Last Mile\Novo Mundo\0 - AVANCO DO DIA POR ARMAZEM\avanco_do_dia_por_armazem_'+self.time_formats.hour+r'h.xlsx')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/1407-avanco-do-dia-por-armazem?almacen=15&date='+self.metabase_date_format.today
        return result
    limit_time=200

class MReport05(ReportBase):
    instant_notification=True
    channel='alertas_last_mile'    
    name='Closed Delivered By Warehouse NM'
    original_file_name='closed___delivered_by_warehouse'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios Last Mile\Novo Mundo\1 - CLOSED DELIVERED BY WAREHOUSE\closed_delivered_by_warehouse_'+self.time_formats.hour+r'h.xlsx')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/1375-closed-delivered-by-warehouse?almacen=15&date='+self.metabase_date_format.today 
        return result
    limit_time=200

class MReport06(ReportBase):
    instant_notification=True
    channel='alertas_last_mile'    
    name='Linhas Para Pickear Armazém Separado Por Pasillo NM'
    original_file_name='linhas_para_pickear_armazem'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios Last Mile\Novo Mundo\2 - LINHAS PARA PICKEAR ARMAZEM SEPARADO POR PASILLO\linhas_para_pickear_armazem_separado_por_pasillo_'+self.time_formats.hour+r'h.xlsx')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/2369-linhas-para-pickear-armazem-separado-por-pasillo?date='+self.metabase_date_format.today+'&Armazen=15'
        return result
    limit_time=200

# class MReport07(ReportBase):
#     forced_try=False
#     name='Base de Vendas por SKU Status e Periodo'
#     original_file_name='base_de_vendas_por_sku__status_e_periodo'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios Last Mile\Novo Mundo\2 - LINHAS PARA PICKEAR ARMAZEM SEPARADO POR PASILLO\linhas_para_pickear_armazem_separado_por_pasillo_'+self.time_formats.hour+r'h.xlsx')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/4961-base-de-vendas-por-sku-status-e-periodo?from_date='+self.metabase_date_format.current_month_first_day+'&to_date='+self.metabase_date_format.current_month_last_day
#         return result
#     limit_time=35

class MReport08(ReportBase):
    name='Funil Pedidos Ops'
    original_file_name='funil_pedidos_ops'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\12 - FUNIL DE OPS\Bases\reagendamentos.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/4677-funil-pedidos-ops?from_date='+self.metabase_date_format.thirty_days_before+'&to_date='+self.metabase_date_format.thirty_days_ahead
        return result
    limit_time=65

class MReport09(ReportBase):
    name='Listado de SKUs Ativos y Agotados - Brasil'
    original_file_name='listado_de_skus'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Planning\1 - LISTADO DE SKUS ATIVOS Y AGOTADOS BR\listado_de_skus_'+self.time_formats.hour+r'h.xlsx')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/1641-listado-de-skus-activos-y-agotados-brasil'
        return result
    limit_time=35

class MReport10(ReportBase):
    name='User Info'
    original_file_name='user_info'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r"\Data & Performance\Sandbox Automatizações\user_info.csv")
                ,Path(r'G:'+self.machine_info.pathlang0+r"\Data & Performance\Relatórios\8 - ON MAPS\4 - CEP'S e Usuários\User_info\user_info.csv")]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/1774-user-info?desde=2021-01-09&hasta='+self.metabase_date_format.today
        return result
    limit_time=250

class MReport11(ReportBase):
    name='Active CEPs By Warehouse'
    original_file_name='active_ceps_by'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r"\Data & Performance\Relatórios\8 - ON MAPS\10  - CEP's Ativos\CEP'S ATIVOS.xlsx")]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/1592-active-ceps-by-warehouse'
        return result
    limit_time=130

class MReport12(ReportBase):        
    name='Aux. Gateway & Canceled Reasons'
    original_file_name='orders_additional_information'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\aux_gateway_cancel_historico\orders_additional_information_'+self.alternative_date_variables.year+'.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/5726-orders-additional-information-gateway-cancelation-reason?from_date='+self.metabase_date_format.current_year_first_day+'&to_date='+self.metabase_date_format.current_year_last_day
        return result
    limit_time=180

# class MReport13(ReportBase):
#     forced_try=False
#     name='Cluster Placed'
#     original_file_name='cluster_placed'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\cluster_historico\cluster_placed_growth_'+self.alternative_date_variables.year_month+'.csv')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/5416-cluster-placed-growth?from_date='+self.metabase_date_format.current_month_first_day+'&to_date='+self.metabase_date_format.today
#         return result
#     limit_time=260

# class MReport14(ReportBase):
#     name='Cluster Placed M-1'
#     original_file_name='cluster_placed'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\cluster_historico\cluster_placed_growth_'+self.alternative_date_variables.past_month_year_month+'.csv')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/5416-cluster-placed-growth?from_date='+self.metabase_date_format.past_month_first_day+'&to_date='+self.metabase_date_format.past_month_last_day
#         return result
#     limit_time=210

class MReport15(ReportBase):
    name='Order History - SF'
    original_file_name='order_history'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\order_history_historico\order_history__updated____new_'+self.alternative_date_variables.year_month+r'.csv')
                ,Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\8 - ON MAPS\9 - Order History 2.0\order_history__updated____new_'+self.alternative_date_variables.year_month+r'.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/6383-order-history?from_date_d='+self.metabase_date_format.current_month_first_day+'&to_date_d='+self.metabase_date_format.next_month_fifteenth_day
        return result
    limit_time=180
        
class MReport16(ReportBase):    
    name='Order History - SF (M-1)'
    original_file_name='order_history'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\order_history_historico\order_history__updated____new_'+self.alternative_date_variables.past_month_year_month+r'.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/6383-order-history?from_date_d='+self.metabase_date_format.past_month_first_day+'&to_date_d='+self.metabase_date_format.past_month_last_day
        return result
    limit_time=180
    
# class MReport18(ReportBase):
#     name='Sales By SKU'
#     original_file_name='sales_by_sku'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\6 - FUNIL\Bases\sales_by_sku_'+self.alternative_date_variables.month_year+'.csv')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/4292-sales-by-sku?from_date='+self.metabase_date_format.current_month_first_day+'&to_date='+self.metabase_date_format.yesterday
#         return result
#     limit_time=120

# class MReport19(ReportBase):
#     forced_try=False
#     name='Conversão por Código - Add to Cart'
#     original_file_name='conversao_por_codigo'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\6 - FUNIL\Bases\add to cart by product.csv')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/3929-conversao-por-codigo-add-to-cart-vs-visitas?desde='+self.metabase_date_format.past_month_first_day+'&ate='+self.metabase_date_format.yesterday
#         return result
#     limit_time=200
    
class MReport20(ReportBase):
    forced_try=False
    name='Checkout Funil'
    original_file_name='checkout_funil'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\6 - FUNIL\Bases\checkout.xlsx')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/4535-checkout-funil'
        return result
    limit_time=200
    
    
class MReport23(ReportBase): 
    name='SignUp`s Referidos'
    original_file_name='signup_s_referidos'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\6 - FUNIL\Bases\signups referidos.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/4752-signup-s-referidos?desde='+self.metabase_date_format.past_month_first_day+'&ate='+self.metabase_date_format.today
        return result
    limit_time=75
    
class MReport24(ReportBase):
    forced_try=False
    name='Purchase Referidos'
    original_file_name='purchase_referidos'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\6 - FUNIL\Bases\purchase referidos.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/4751-purchase-referidos?desde='+self.metabase_date_format.past_month_first_day+'&ate='+self.metabase_date_format.today
        return result
    limit_time=80
    
class MReport26(ReportBase):
    forced_try=False
    name='Contagem de referidos (Sessions)'
    original_file_name='contagem_de_referidos'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\6 - FUNIL\Bases\session referidos.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/4496-contagem-de-referidos-sessions?date='+self.metabase_date_format.past_month_first_day
        return result
    limit_time=300
    
class MReport28(ReportBase):
    name='Reagendados Ops/CX BR'
    original_file_name='reagendados_ops'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Motoristas\Reagendamento Metabase\reagendados_ops_cx_br.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/2950-reagendados-ops-cx-br'
        return result
    limit_time=150 
    
class MReport29(ReportBase): 
    forced_try=False
    name='Loyalty User Extraction'
    original_file_name='loyalty_loyaltyuser'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\LOYALTY\Loyalty User Extraction.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/3679-loyalty-loyaltyuser-extraction'
        return result
    limit_time=510
    
class MReport30(ReportBase): 
    name='Data Order Survey Br'
    original_file_name='data_order_survey'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\RYO\Data Order Survey Br.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/4812-data-order-survey-br'
        return result
    limit_time=30
    
class MReport31(ReportBase): 
    name='Slots with Tolerance Br'
    original_file_name='slots_with_tolerance'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\17 - MOTORISTAS\Bases\Metabase - Slots Com Tolerancia Metabase\Slots with Tolerance Br '+self.alternative_date_variables.month_dot_year+'.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/3727-slots-with-tolerance-br?From='+self.metabase_date_format.current_month_first_day+'&To='+self.metabase_date_format.current_month_last_day
        return result
    limit_time=25
    
class MReport32(ReportBase): 
    forced_try=False
    name='Delivered Orders Full Jorney'
    original_file_name='delivered_orders'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\17 - MOTORISTAS\Bases\Metabase - Jornada da Entrega\delivered_orders__full_journey_br_'+self.alternative_date_variables.month_dot_year+'.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/3520-delivered-orders-full-journey-br?desde='+self.metabase_date_format.current_month_first_day+'&hasta='+self.metabase_date_format.current_month_last_day
        return result
    limit_time=200
    
# class MReport33(ReportBase): 
#     instant_notification=True
#     name='Gestão À Vista'
#     original_file_name='gestao_a_vista'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\16 - GESTÃO À VISTA\bases\gestao_a_vista.csv')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/5683'
#         return result
#     limit_time=40
    

# class MReport56(ReportBase): 
#     instant_notification=True
#     channel='data_performace_br'
#     
#     name='Gestão À Vista'
#     original_file_name='gestao_a_vista'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\16 - GESTÃO À VISTA\bases\gestao_a_vista.csv')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/5683'
#         return result
#     limit_time=40
    
# class MReport34(ReportBase): 
#     forced_try=False
#     name='Base de Vendas por SKU Status e Período'
#     original_file_name='base_de_vendas_por_sku'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Pricing\5 - PRECIFICA\01. Relatório de Venda\Base Venda_Competitividade_'+self.alternative_date_variables.month_name_capitalized+'_'+self.alternative_date_variables.year+'.csv')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/4961-base-de-vendas-por-sku-status-e-periodo?from_date='+self.metabase_date_format.current_month_first_day+'&to_date='+self.metabase_date_format.current_month_last_day
#         return result
#     limit_time=180

# class MReport35(ReportBase):
#     name='Order History - Real Time'
#     original_file_name='order_history'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\order_history_real_time\order_history__updated__last_thirty_one_days.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/5724-order-history-updated-new?from_date_p='+self.metabase_date_format.past_thirty_first_day+'&to_date_p='+self.metabase_date_format.today
#         return result
#     limit_time=210

# class MReport36(ReportBase):
#     name='Cluster Placed D-Atual'
#     original_file_name='cluster_placed'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\cluster_historico\cluster_placed_growth_realtime.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/5416-cluster-placed-growth?from_date='+self.metabase_date_format.today+'&to_date='+self.metabase_date_format.today
#         return result
#     limit_time=300

class MReport37(ReportBase):
    name='Fraud Prevention Tool Br - All Orders'
    original_file_name='fraud_prevention'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\ENVIO PESQUISAS\fraud_prevention_tool_br___all_orders_'+self.alternative_date_variables.year_month+'.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/1587-fraud-prevention-tool-br-all-orders?from='+self.metabase_date_format.current_month_first_day+'&to='+self.metabase_date_format.current_month_last_day
        return result
    limit_time=60

# class MReport38(ReportBase):
#     name='Funnel Audiência - Web'
#     original_file_name='funnel_audiencia_'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\funnel\Funnel Audiência - Web.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/4097-funnel-audiencia-web-br?desde='+self.metabase_date_format.six_months_ago_first_day+'&hasta='+self.metabase_date_format.today
#         return result
#     limit_time=75

# class MReport39(ReportBase):
#     name='Funnel Audiência - IOS'
#     original_file_name='funnel_audiencia_'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\funnel\Funnel Audiência - IOS.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/4099-funnel-audiencia-ios-br?desde='+self.metabase_date_format.six_months_ago_first_day+'&hasta='+self.metabase_date_format.today
#         return result
#     limit_time=75

# class MReport40(ReportBase):
#     name='Funnel Audiência - Android'
#     original_file_name='funnel_audiencia_'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\funnel\Funnel Audiência - Android.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/4101-funnel-audiencia-android-br?desde='+self.metabase_date_format.six_months_ago_first_day+'&hasta='+self.metabase_date_format.today
#         return result
#     limit_time=75

class MReport41(ReportBase):
    name='Cupom All'
    original_file_name='cupom_all'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\funnel\Cupom All.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/3944-cupom-all'
        return result
    limit_time=30

# class MReport42(ReportBase):
#     name='Tabla Conversion Diária Br'
#     original_file_name='tabla_conversion_'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\funnel\Tabla Conversión Diaria (General) - Br.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/3313-tabla-conversion-diaria-general-br?desde='+self.metabase_date_format.current_year_first_day+'&hasta='+self.metabase_date_format.today
#         return result
#     limit_time=85

class MReport43(ReportBase):
    name='Vendas Diárias Nível Orderline'
    original_file_name='vendas_diarias'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Pricing\0 - VENDAS DIÁRIAS NÍVEL ORDERLINE\Bases Originais\M-Atual.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/3480-vendas-diarias-nivel-orderline?from_date='+self.metabase_date_format.current_month_first_day+'&to_date='+self.metabase_date_format.next_month_fifteenth_day
        return result
    limit_time=480

class MReport44(ReportBase):
    name='Vendas Diárias Nível Orderline (M-1)'
    original_file_name='vendas_'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Pricing\0 - VENDAS DIÁRIAS NÍVEL ORDERLINE\Bases Originais\M-1.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/3480-vendas-diarias-nivel-orderline?from_date='+self.metabase_date_format.past_month_first_day+'&to_date='+self.metabase_date_format.past_month_last_day
        return result
    limit_time=85

# class MReport45(ReportBase):
#     name='All Skus SD'
#     original_file_name='all_skus'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\15 - MAPA DE ABASTECIMENTO 2.0\bases\All_Skus_SD.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/2308-all-skus-brasil-com-peso-reservado'
#         return result
#     limit_time=200
    
# class MReport46(ReportBase):
#     name='All Skus NM'
#     original_file_name='all_skus'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\15 - MAPA DE ABASTECIMENTO 2.0\bases\All_Skus_NM.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/5531-all-skus-brasil-novo-mundo'
#         return result
#     limit_time=200

# class MReport47(ReportBase):
#     name='Gestão À Vista MX'
#     original_file_name='gestao_a_vista'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\MX\Reports\Gestão Á Vista\gestao_a_vista.csv')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/5647'
#         return result
#     limit_time=40

# class MReport48(ReportBase): 
#     name='Produtos com Desconto'
#     original_file_name='produtos_com_desconto'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\15 - MAPA DE ABASTECIMENTO 2.0\bases\Descontos.csv')]
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/1935'
#         return result
#     limit_time=60

class MReport49(ReportBase): 
    name='Informações Gerais Sobre Faltantes'
    original_file_name='informacoes_gerais_sobre_faltantes'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\10 - DASHBOARD FALTANTES\Bases\informacoes_gerais_sobre_faltantes.xlsx')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/4508-informacoes-gerais-sobre-faltantes?de='+self.metabase_date_format.two_months_ago_first_day+'&ate='+(self.metabase_date_format.yesterday 
        if self.metabase_date_format.current_month_first_day < self.metabase_date_format.yesterday else self.metabase_date_format.current_month_first_day)
        return result
    limit_time=260 # check ! 

class MReport50(ReportBase): 
    name='Vendas Por SKU Diário'
    original_file_name='vendas_por_sku__torre_de_controle'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\2 - SUPPLY DASHBOARD\Bases Metabase\venda_por_sku_diario_'+self.alternative_date_variables.year_month+r'.csv')]
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/3744-vendas-por-sku-torre-de-controle?from_date='+self.metabase_date_format.current_month_first_day+'&to_date='+self.metabase_date_format.current_month_last_day
        return result
    limit_time=320 # check ! 

# class MReport51(ReportBase):
#     name='Vendas Diárias Nível Orderline'
#     original_file_name='vendas_diarias'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Pricing\0 - VENDAS DIÁRIAS NÍVEL ORDERLINE\Bases Originais\M-Atual.xlsx')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/3480-vendas-diarias-nivel-orderline?from_date='+self.metabase_date_format.current_month_first_day+'&to_date='+self.metabase_date_format.next_month_fifteenth_day
#         return result
#     limit_time=480

class MReport52(ReportBase):
    name='Produtos Recebidos Entre Duas Datas (Recebimento)'
    original_file_name='produtos_recebidos_entre_duas_datas'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\2 - SUPPLY DASHBOARD\Recebimento.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/2266'
        return result
    limit_time=120

class MReport53(ReportBase):
    name='Costo de Envio'
    original_file_name='reporte_pedidos_entregados'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Pricing\8 - RELATÓRIO DE FRETE\Custo_Frete_'+self.alternative_date_variables.month_name_capitalized+self.alternative_date_variables.year_two_digits+'.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/2273-reporte-pedidos-entregados-con-costo-de-envio?fecha_desde='+self.metabase_date_format.current_month_first_day+'&fecha_hasta='+self.metabase_date_format.yesterday
        return result
    limit_time=60

class MReport54(ReportBase):
    name='Dias Esgotados'
    original_file_name='dias_esgotados'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\2 - SUPPLY DASHBOARD\Dias Esgotados.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/2140-dias-esgotados?dia='+self.metabase_date_format.yesterday
        return result
    limit_time=60

class MReport55(ReportBase):
    name='Abonos a Wallet'
    original_file_name='abonos_a_wallet'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Bases Abonos e Wallet\abonos_a_wallet_'+self.alternative_date_variables.month_year+'.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/2296-abonos-a-wallet?desde='+self.metabase_date_format.current_month_first_day+'&hasta='+self.metabase_date_format.yesterday
        return result
    limit_time=60

class MReport56(ReportBase):
    name='Base Relatório Vendas'
    original_file_name='base_relatorio_vendas'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\1 - DAILY SALES\Bases Originais\M-Atual.csv'),
                     Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\1 - DAILY SALES\Bases Históricas\M-Atual.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/2327-base-relatorio-vendas?from_date='+self.metabase_date_format.current_month_first_day+'&to_date='+self.metabase_date_format.next_month_fifteenth_day
        return result
    limit_time=720

# class MReport57(ReportBase):
#     name='Vendas por SKU Diário (Mapa)'
#     original_file_name='vendas_por_sku'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\15 - MAPA DE ABASTECIMENTO 2.0\bases\Base Vendas\vendas_por_sku_ultimos_90_dias.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/3744-vendas-por-sku-torre-de-controle?from_date='+self.metabase_date_format.past_ninety_five_days+'&to_date='+self.metabase_date_format.next_fifteen_days
#         return result
#     limit_time=310

# class MReport58(ReportBase):
#     name='Vendas por SKU Diário (Mapa)'
#     original_file_name='vendas_por_sku'
#     @property
#     def default_destination_path(self):
#         path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\15 - MAPA DE ABASTECIMENTO 2.0\bases\Base Vendas\vendas_por_sku_ultimos_90_dias.csv')]
#         return path_list
#     @property
#     def link(self):
#         result = 'https://infinite.justo.mx/question/3744-vendas-por-sku-torre-de-controle?from_date='+self.metabase_date_format.past_ninety_five_days+'&to_date='+self.metabase_date_format.next_fifteen_days
#         return result
#     limit_time=310

class MReport59(ReportBase):
    name='Estoque Mínimo Por SKU'
    original_file_name='estoque_minimo_por_sku'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\10 - DASHBOARD FALTANTES\Bases\estoque mínimo por sku\estoque_minimo_por_sku '+self.alternative_date_variables.today_dd_mm_yyyy_with_hyphen+'.xlsx')
                    ,Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\2 - SUPPLY DASHBOARD\Estoque Mínimo.xlsx')
                    ,Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\0 - BASES UNIVERSAIS\estoque mínimo por sku\estoque_minimo_por_sku '+self.alternative_date_variables.today_dd_mm_yyyy_with_hyphen+'.xlsx')]     
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/4585'
        return result
    limit_time=120

class MReport60(ReportBase):
    name='BR Cohorts DB'
    original_file_name='br_cohorts'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:\Meu Drive\Docs\Justo\Brasil\Churn\Cohorts_Temp.csv')] # Change !    
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/1942-br-cohorts-db?desde='+self.metabase_date_format.past_month_first_day+'&hasta='+self.metabase_date_format.next_month_fifteenth_day
        return result
    limit_time=130

class MReport61(ReportBase):
    
    name='Cupom All - MX'
    original_file_name='cupom_all'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\funnel\Cupom All - MX.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/6687'
        return result
    limit_time=30

class MReport62(ReportBase):
    
    name='Produtos Recebidos Entre Duas Datas - NM (Recebimento)'
    original_file_name='wms_'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\2 - SUPPLY DASHBOARD\Recebimento_NM.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/6619-wms-recibo-orden-de-compra-transferencias-cedis-mfc-br'
        return result
    limit_time=120

class MReport63(ReportBase):
    
    name='Info Existencias FYV Bodegas - En Vivo'
    original_file_name='info_existencias'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang3+r'\Shared Drives Shortcuts\Processos de Mexico\Performance\Info Existencias FYV Bodegas.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/4750-info-existencias-fyv-bodegas-en-vivo'
        return result
    limit_time=60

class MReport64(ReportBase):
    
    name='Reporte Fly Productos Afectados BR'
    original_file_name='reporte_fly_productos_afectados'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Base FLY\reporte_fly_productos_afectados_'+self.alternative_date_variables.month_year+'.csv')]     
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/3030-reporte-fly-productos-afectados-br?desde='+self.metabase_date_format.current_month_first_day+'&hasta='+self.metabase_date_format.yesterday
        return result
    limit_time=80

class MReport65(ReportBase):
    name='Canceled Orders Information'
    original_file_name='canceled_orders'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\BI Team - Global\Reports\MX\6 - Histórico Nivel Producto\Fraud orders\Canceled_Orders.csv')]     
        return path_list
    @property
    def link(self):
        result = 'https://infinite.justo.mx/question/6053-canceled-orders-table'
        return result
    limit_time=900

# Zendesk

# class ZReport01(ReportBase):name='SAC Reagendamento'
#     original_file_name='SAC'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\12 - FUNIL DE OPS\Bases\sac_reagendamento\sac_reagendamento_'+self.alternative_date_variables.yest_str+'.csv')]
#     @property
#     def link(self):
#         result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/118420981'
#         return result
#     limit_time=35

# class ZReport02(ReportBase):name='SAC Cancelamento'
#     original_file_name='SAC'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\12 - FUNIL DE OPS\Bases\sac_cancelamento\sac_cancelamento_'+self.alternative_date_variables.yest_str+'.csv')]
#     @property
#     def link(self):
#         result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/116325031'
#         return result
#     limit_time=35

# class ZReport03(ReportBase):name='Motorista Reagendamento Cancelamento LOG'
#     original_file_name='Motorista'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\12 - FUNIL DE OPS\Bases\motorista_reagendamento_cancelamento_log\motorista_reagendamento_cancelamento_log_'+self.alternative_date_variables.yest_str+'.csv')]
#     @property
#     def link(self):
#         result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/135830651'
#         return result
#     limit_time=35

# class ZReport04(ReportBase):

#     
#     
#     
#     instant_notification =False
#     
#     
#     name='Cliente Reagendamento Cancelamento LOG'
#     original_file_name='Cliente'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\12 - FUNIL DE OPS\Bases\cliente_reagendamento_cancelamento_log\cliente_reagendamento_cancelamento_log_'+self.alternative_date_variables.year+'.csv')]
#     @property
#     def link(self):
#         result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/137369241'
#         return result
#     limit_time=60

class ZReport05(ReportBase):
    
    instant_notification =False  
    name='Anidado 1'
    original_file_name='Anidado'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Anidado 1\anidado_1_'+self.alternative_date_variables.yesterday_hyphen_separated_mm_dd_yyyy+r'.csv')]
    @property
    def link(self):
        result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/135671991'
        return result
    limit_time=35

class ZReport06(ReportBase):
    
    instant_notification =False  
    name='Anidado 2'
    original_file_name='Anidado'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Anidado 2\anidado_2_'+self.alternative_date_variables.yesterday_hyphen_separated_mm_dd_yyyy+r'.csv')]
    @property
    def link(self):
        result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/135672081'
        return result
    limit_time=35

class ZReport07(ReportBase):
    
    instant_notification =False  
    name='Anidado 3'
    original_file_name='Anidado'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Anidado 3\anidado_3_'+self.alternative_date_variables.yesterday_hyphen_separated_mm_dd_yyyy+r'.csv')]
    @property
    def link(self):
        result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/135672551'
        return result
    limit_time=35

class ZReport08(ReportBase):
    
    instant_notification =False  
    name='CX Insights Metrics Master V2'
    original_file_name='CX'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\CX Insights Metrics Master v2 BR\cx_insights_metrics_master_v2_br_'+self.alternative_date_variables.yesterday_hyphen_separated_mm_dd_yyyy+r'.csv')]
    @property
    def link(self):
        result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/15551351/report/135672701'
        return result
    limit_time=35

class ZReport09(ReportBase):
    
    instant_notification =False  
    name='Encuestas Enviadas BR'
    original_file_name='Encuestas'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Encuestas Enviadas BR\encuestas_enviadas_br_'+self.alternative_date_variables.yesterday_hyphen_separated_mm_dd_yyyy+r'.csv')]
    @property
    def link(self):
        result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/135671361'
        return result
    limit_time=35

class ZReport10(ReportBase):
    
    instant_notification =False  
    name='Problema BR'
    original_file_name='Problema'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Problema BR\problema_br_'+self.alternative_date_variables.yesterday_hyphen_separated_mm_dd_yyyy+r'.csv')]
    @property
    def link(self):
        result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/135671961'
        return result
    limit_time=35

class ZReport11(ReportBase):
    
    instant_notification =False  
    name='Anidado 4'
    original_file_name='Anidado'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Anidado 4\anidado_4_'+self.alternative_date_variables.yesterday_hyphen_separated_mm_dd_yyyy+r'.csv')]
    @property
    def link(self):
        result = 'https://justo7393.zendesk.com/explore#/pivot-table/connection/13828291/report/158077251'
        return result
    limit_time=35

#API Link

class AReport01(ReportBase):
    gkey = '1mlhF7hzp29VGSeP2cj11Cja4a4Rwf5vyXvNw4KPRzQg'
    gsheet = 'android'
    name='Apps Flyer - Android'
    original_file_name='mx.justo.android'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\Appsflyer\Android\Apps Flyer - Android.csv')]
    @property
    def link(self):
        result = 'https://hq1.appsflyer.com/aggreports/enc/mx.justo.android/geo_by_date_report/v5?api_token=834b33d6-0d5e-4985-b1c5-73c3de21e39b&from=2023-05-01&to='+self.alternative_date_variables.year+'-12-31'
        return result
    limit_time=35

class AReport02(ReportBase):
    gkey = '1TKE8ZGlX3lE74BkzR2JRwbiAwyMirEHt6apTOLj9LDY'
    gsheet = 'ios'
    name='Apps Flyer - IOS'
    original_file_name='id'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\Appsflyer\iOS\Apps Flyer - IOS.csv')]
    @property
    def link(self):
        result = 'https://hq.appsflyer.com/export/id1491969468/geo_by_date_report/v5?api_token=834b33d6-0d5e-4985-b1c5-73c3de21e39b&from=2023-05-01&to='+self.alternative_date_variables.year+'-12-31'
        return result
    result = 35
    limit_time=180

# GSheets

class GReport01(ReportBase):
    name='Nuevo NPS BR'
    original_file_name='Nuevo NPS BR'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\8 - ON MAPS\8 - Base NPS\Nuevo NPS BR  - NPS '+self.alternative_date_variables.year+'.tsv')
                ,Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\NPS\Nuevo NPS BR  - NPS '+self.alternative_date_variables.year+'.tsv')
                ]
    @property
    def link(self):
        result='https://docs.google.com/spreadsheets/d/1GZ0CfwIcB_Y9EwS46PqYj70xwwwmRyuFE6z1owxrwlg/edit#gid=1034856542'
        return result
    limit_time=40
    
class GReport02(ReportBase):
    name='FOS Master BR'
    original_file_name='FOS Master BR'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\FOS\FOS Master BR.tsv')
                ]
    @property
    def link(self):
        result='https://docs.google.com/spreadsheets/d/1oJvG-ExYmpkJmoG2fokPiEJ9gRhhH1A2hqcPQU3G6iw/edit#gid=1764063349'
        return result
    limit_time=20
    
class GReport03(ReportBase):
    name='ROS Master BR'
    original_file_name='ROS Master BR'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\ROS\ROS Master BR.tsv')
                ]
    @property
    def link(self):
        result='https://docs.google.com/spreadsheets/d/1RjCQVg4Z4TidCUE-KPRTD-8LBf6s4NzWvvpQgQajS8U/edit#gid=1999979131&fvid=1322998572'
        return result
    limit_time=20

# class GReport04(ReportBase):
#     name='Conferencia de Devolução dos Pedidos'
#     original_file_name='Conferencia de devolução dos pedidos'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\17 - MOTORISTAS\Bases\Base Google Sheets - Conferencia de Pedidos Devolvidos\Conferencia de Pedidos Devolvidos.csv')
#                 ]
#     @property
#     def link(self):
#         result='https://docs.google.com/spreadsheets/d/1t-CcamEJd4QzrulsmSUCjWUUM4fM2yi5N0SBuF5ztu4/edit#gid=1265549727'
#         return result   
#     limit_time=20
    
# class GReport05(ReportBase):
#     name='Produtividade Last Mile (respostas) V3 '
#     original_file_name='Produtividade Last Mile'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\17 - MOTORISTAS\Bases\Base Google Sheets - Produtividade dos Puxadores de Pedidos\Produtividade dos Puxadores de Pedidos.csv')
#                 ]
#     @property
#     def link(self):
#         result='https://docs.google.com/spreadsheets/d/1VU4U9olMLgtGxxCsE2dfOjriL280iSTVmzkwx2iYWXk/edit#gid=1780023177'
#         return result
#     limit_time=20
    
# class GReport06(ReportBase):
#     name='Devolução de Pedidos e Produtos CX (respostas)'
#     original_file_name='Devolução de pedidos'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\17 - MOTORISTAS\Bases\Base Google Sheets - Forms de Devolucao de Pedidos\Devolução de Pedidos e Produtos CX (respostas).csv')
#                 ]
#     @property
#     def link(self):
#         result='https://docs.google.com/spreadsheets/d/1LtnEHSM_llT7SvFGLiOiax6V5Q2vLD-K91fkz1He27E/edit#gid=1333431273'
#         return result
#     limit_time=20
    
class GReport07(ReportBase):
    name='Pesquisa de Motoristas BR'
    original_file_name='Pesquisa Motoristas'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\17 - MOTORISTAS\Bases Motoristas\GSHEETS - PESQUISA MOTORISTAS\Pesquisa de Motoristas.csv')
                ]
    @property
    def link(self):
        result='https://docs.google.com/spreadsheets/d/1h-9u7HtGql9DIIpGJBw5dDRqc6s9Q0tquCJUb-v7erw/edit#gid=0'
        return result
    limit_time=20

class GReport08(ReportBase): 
    name='Survey Master BR CX CSAT BR'
    original_file_name='Survey Master BR' 
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Bases Pesquisa CSAT\survey_master_br_cx_csat_br.csv')]
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1-7j7BrA78hIWDkjLEorsJyatNa6RXNxAeOgHrEe1gmQ/edit#gid=1216479918'
        return result
    limit_time=40   

class GReport09(ReportBase): 
    name='Merma São Domingos 2023'
    original_file_name='Merma São Domingos'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\2 - SUPPLY DASHBOARD\Merma Motivo\Novas\Merma Novo Mundo FLV_2023_Nova.xlsx')]
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1kOrPPUK9SeIlULaHNxnax4vvcz_PLsrphMW1mzfbGqA/edit#gid=1875775712'
        return result
    limit_time=60 

class GReport10(ReportBase): 
    name='NPS - Disparos Via WhatsApp'
    original_file_name='NPS'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\NPS VIA WHATSAPP\NPS - Disparos via WhatsApp - NPS - WhatsApp.csv')]
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1jl8bL8hL-jiKjqZQOATxnHQo9SCHm3e_JtwFDCP-iME/edit#gid=239712821'
        return result
    limit_time=25 

class GReport11(ReportBase): 
    name='Merma SD'
    original_file_name='Merma_SD'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\23 - RELATORIO MERMA\Bases RCA\Preenchidas\Merma_SD.xlsx')]
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1uA6f_F9bfe3GN7ZwqM6IkHtyvyCVMzxc1ufEcgS3ud8/edit#gid=1749802247'
        return result
    limit_time=70 

class GReport12(ReportBase): 
    name='Merma NM'
    original_file_name='Merma_NM'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\23 - RELATORIO MERMA\Bases RCA\Preenchidas\Merma_NM.xlsx')]
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1ts8fqG8HL_CgsAM3KETsdj6UjogDcWDgKD8NOVVntu8/edit#gid=1749802247'
        return result
    limit_time=40 

class GReport13(ReportBase): 
    name='Merma FLV SD'
    original_file_name='Merma_FLV_SD'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\23 - RELATORIO MERMA\Bases RCA\Preenchidas\Merma_FLV_SD.xlsx')]
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1ieOE2zRrN6_qiA5iashfJAGx6Hwr3DslLdX6QDXrYYs/edit#gid=1749802247'
        return result
    limit_time=45 

class GReport14(ReportBase): 
    name='Merma FLV NM'
    original_file_name='Merma_FLV_NM'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\23 - RELATORIO MERMA\Bases RCA\Preenchidas\Merma_FLV_NM.xlsx')]
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1eB3rkB5vNudVe5_JcjHSBEM0mZvju47bELgG7euJT04/edit#gid=1749802247'
        return result
    limit_time=25 

class GReport15(ReportBase): 
    name='Signup_Br'
    original_file_name='Signup_Br'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\SIGNUP\Signup_Br.csv')]
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1LFnzCY6NoHytkIcOQ-HZ8mivorj-AlJ99M2HPvz-6h8/edit#gid=153235506'
        return result
    limit_time=25 

class GReport16(ReportBase): 
    name='Encuesta Churn BR'
    original_file_name='Encuesta Churn BR'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\18 - EXPERIENCIA DO CLIENTE\Bases\CHURN\Encuesta Churn BR.csv')]
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1hqdBwFRPkb6evzA3XA4b4JCZMhHdD6u7ER9iAVcYI5M/edit#gid=1182028654'
        return result
    limit_time=25 

class GReport17(ReportBase): 
    name='Validações De Cupons Não Classificados'
    original_file_name='Coupon Class'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\funnel\Validações De Cupons Não Classificados.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/17CFjwuAFKejYNV0mCEIxRcY09vKLPgggveiNLq1TiNI/edit#gid=572491840'
        return result
    limit_time=85  

class GReport18(ReportBase): 
    name='All Bases'
    original_file_name='All Bases'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\all bases history\all_bases_'+self.alternative_date_variables.year_month+'.xlsx')]
        return path_list
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1QBPcfxqucGalXPUYtetpACbspa58DN1rcaYRVqZHW1Q/edit?pli=1#gid=1882945107'
        return result
    limit_time=85  

class GReport19(ReportBase): 
    name='Lista de Faltantes Por Dia BR'
    original_file_name='FALTANTES_2023'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\10 - DASHBOARD FALTANTES\Bases\lista_de_faltantes_por_dia_br.xlsx')]
        return path_list
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1HCq3TcfJaTA0Wm6NRyFubhqIh1NoM3sksqdAl_e0Ego/edit#gid=0'
        return result
    limit_time=75  
    
class GReport20(ReportBase): 
    name='Master Catálogo'
    original_file_name='Master Catálogo - Brasil'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\0 - BASES UNIVERSAIS\Master Catálogo - Brasil.xlsx')]
        return path_list
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1g39z5xnVei_n7p5ahiFFfYjYInA9M_eM9W4p185OHeI/edit'
        return result
    limit_time=200  

class GReport21(ReportBase): 
    name='Perda Merma Atual'
    original_file_name='MERMA_2023'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\2 - SUPPLY DASHBOARD\Merma Motivo.xlsx'),
                     Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\2 - SUPPLY DASHBOARD\Merma Motivo\Merma Motivo '+self.alternative_date_variables.year+'.xlsx')]
        return path_list
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/13WT6PRMB80T4jFrOmFyxpQb3DET5-gIyrk9uh6kGTys/edit#gid=0'
        return result
    limit_time=120  

class GReport22(ReportBase): 
    name='Agendamento Justo_Planejamento de Capacidade Ajustado'
    original_file_name='Agendamento Justo_Planejamento de Capacidades_Ajustado'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\7 - ACOMPANHAMENTO OCS\Agendamento Novo.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1oVYOj_IrRuhGrrPXeWADGLoUhmtaN-5B/edit#gid=1701322921'
        return result
    limit_time=40     

class GReport23(ReportBase): 
    name='Solicitação de Transferência de Saldo'
    original_file_name='SOLICITAÇÃO DE TRANSFERÊNCIA DE SALDO'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\2 - SUPPLY DASHBOARD\Outros RCAs Merma.xlsx')]
        return path_list
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1Wi4PHdTGufbsRaZNyoJubKEZ5auz223e92EVByb_Jyw/edit#gid=1174782242'
        return result
    limit_time=100     

class GReport24(ReportBase): 
    name='Validações De Cupons Não Classificados - MX'
    original_file_name='Coupon Class'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios de Growth\1 - PERFORMANCE\funnel\Validações De Cupons Não Classificados - MX.csv')]
        return path_list
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1NKbFcNHg13nnxZAt76yOLYKVwxLTG3VirvA33OkYYO8/edit#gid=572491840'
        return result
    limit_time=85

class GReport25(ReportBase): 
    name='Acoes Comerciais'
    original_file_name='Consolidado Ações'
    @property
    def default_destination_path(self):
        path_list = [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\29 - Tracking de Ações Comerciais\Acoes Comerciais.xlsx')]
        return path_list
    @property
    def link(self):
        result = 'https://docs.google.com/spreadsheets/d/1RtVvYIYpNB7zL4Bjsvrg93o2lnY2WYZSCZqEUk1XbH4/edit#gid=0'
        return result
    limit_time=85

# Playvox

class PReport01(ReportBase): 
    name='Base Atual - BR CX Suporte (PlayVox)'
    original_file_name='br_cx_suporte'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\13 - BASES CX\Bases\Bases Qualidade\Base Atual.csv')
                ]
    @property
    def link(self):
        result='https://justobrazil.playvox.com/quality/evaluations'
        return result
    limit_time=25
    
# # Locus

# class LReport01(ReportBase):
    
#     
#     
#     
#     
#     
#     sheets_report=True
#     
#     
#     name='Task Export (Locus)'
#     original_file_name='task-export'
#     @property
#     def default_destination_path(self):
#         return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\17 - MOTORISTAS\Bases\Base Locus\task-export-'+self.alternative_date_variables.yesterday_hyphen_separated_mm_dd_yyyy+'.csv')
#                 ]
#     @property
#     def link(self):
#         result='https://justo-br.locus-dashboard.com/#/client/justo-br/live_view/tasks?selectedStatus=all'
#         return result
#     limit_time=45 

# Extranet

class EReport01(ReportBase): 
    name='Produtos Ifood - SD'
    original_file_name='produtos'
    @property
    def default_destination_path(self):
        return [Path(r'G:\Meu Drive\Shared Drives Shortcuts\Product Ifood\sd_product_info.xlsx')
                ]
    @property
    def link(self):
        result='https://extranet.sitemercado.com.br/loja/edit/41686/download/PRODUTOS'
        return result
    limit_time=40

class EReport02(ReportBase): 
    name='Produtos Ifood - NM'
    original_file_name='produtos'
    @property
    def default_destination_path(self):
        return [Path(r'G:\Meu Drive\Shared Drives Shortcuts\Product Ifood\nm_product_info.xlsx')
                ]
    @property
    def link(self):
        result='https://extranet.sitemercado.com.br/loja/edit/41687/download/PRODUTOS'
        return result
    limit_time=40

# Gen.te
    
class BReport01(ReportBase): 
    name='Base LG - Gen.te'
    original_file_name='produtos'
    @property
    def default_destination_path(self):
        return [Path(r'G:'+self.machine_info.pathlang0+r'\Data & Performance\Relatórios\0 - BASES UNIVERSAIS\Base LG\Base LG.xlsx')
                ]
    @property
    def link(self):
        result='https://prd-ng2.lg.com.br/Gente/Produtos/Infraestrutura/Suite/Index'
        return result
    limit_time=40