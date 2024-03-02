import pandas as pd
import glob
from etltools import PhatomReport,FileToGSheets
from plconfig import MachineInfo
import os

mi = MachineInfo()

pd.options.display.float_format = '{:,.2f}'.format

origin_files = glob.glob(r'G:'+mi.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\order_history_historico\*.csv')

list_dfs = [pd.read_csv(f) for f in origin_files]

df = pd.concat(list_dfs, ignore_index=True)

df = df[['ORDER_ID','ORDER_STATUS','ORDER_DATE', 'DELIVERY_DATE', 'USER_ID','GMV_DELIVERED','CLUSTER','SOURCE']]

df['DELIVERY_DATE']=pd.to_datetime(df['DELIVERY_DATE'])

df_filtered = df[
    (df['ORDER_STATUS'] == 'delivered')
]

df_filtered = df_filtered.sort_values('DELIVERY_DATE')

df_filtered['ANO_MES'] = df_filtered['DELIVERY_DATE'].dt.to_period('M')

group_user_id_cluster = df_filtered.groupby(['USER_ID','ANO_MES']).agg({
    'CLUSTER': 'first', #last
    'DELIVERY_DATE': 'first' #last
}).reset_index()

groped_by_order_id_gmv = df_filtered.groupby(['ORDER_ID']).agg({
    'GMV_DELIVERED': 'sum', 
    'DELIVERY_DATE': 'last',
    'CLUSTER': 'last'
}).reset_index()

order_count = groped_by_order_id_gmv.groupby(['DELIVERY_DATE', 'CLUSTER'], dropna=False)['ORDER_ID'].nunique().reset_index(name='PEDIDOS')

user_count = group_user_id_cluster.groupby(['DELIVERY_DATE', 'CLUSTER'], dropna=False)['USER_ID'].nunique().reset_index(name='USUARIOS')

result = pd.merge(order_count, user_count,  how='left', left_on=['DELIVERY_DATE','CLUSTER'], right_on = ['DELIVERY_DATE','CLUSTER'])

gmv_sum = groped_by_order_id_gmv.groupby(['DELIVERY_DATE', 'CLUSTER'], dropna=False)['GMV_DELIVERED'].sum().reset_index(name='GMV')

result2 = pd.merge(result, gmv_sum, how='left', left_on=['DELIVERY_DATE','CLUSTER'], right_on = ['DELIVERY_DATE','CLUSTER'])

result2 = result2.rename(columns={'PEDIDOS':'ORDERS'})

result2 = result2.rename(columns={'USUARIOS':'USERS'})

result2 = result2[['DELIVERY_DATE','CLUSTER','GMV','ORDERS','USERS']]

gmv_delivery_path = r'G:'+mi.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\gmv_delivered_by_day.csv'

result2.to_csv(gmv_delivery_path, index=False)

gmv_delivery = PhatomReport('GMV Delivery - All Bases',gmv_delivery_path)

gmv_delivery_load = FileToGSheets(gmv_delivery,'1QBPcfxqucGalXPUYtetpACbspa58DN1rcaYRVqZHW1Q','Delivered')
gmv_delivery_load.force_load()

# os.remove(file)