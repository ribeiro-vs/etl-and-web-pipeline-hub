
import pandas as pd
import glob
from etltools import load_to_gsheets
from plconfig import MachineInfo
import os

mi = MachineInfo()

pd.options.display.float_format = '{:,.2f}'.format

origin_files = glob.glob(r'G:'+mi.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\cluster_historico\*.csv')
aux_files = glob.glob(r'G:'+mi.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\order_history_historico\*.csv')

list_dfs1 = [pd.read_csv(f) for f in origin_files]
list_dfs2 = [pd.read_csv(f) for f in aux_files]

df1 = pd.concat(list_dfs1, ignore_index=True)
df2 = pd.concat(list_dfs2, ignore_index=True)

df1 = df1[['order_id','created_date','user_id', 'user_classification_raw']]
df2 = df2[['ORDER_ID','ORDER_STATUS','GMVP', 'ORDER_DATE','USER_ID']]      

df2['ORDER_DATE']=pd.to_datetime(df2['ORDER_DATE'])
df1['created_date']=pd.to_datetime(df1['created_date'])

df1_filtered = df1
df2_filtered = df2

df2_filtered['ANO_MES'] = df2_filtered['ORDER_DATE'].dt.to_period('M')

df1_filtered = df1_filtered.drop(columns=['user_id'])

df1_filtered_2 = df1_filtered.sort_values(by="created_date").drop_duplicates(subset=["order_id"], keep="last")

merge_all = pd.merge(df2_filtered,df1_filtered_2,how='left',left_on=['ORDER_ID'],right_on=['order_id'])

merge_all = merge_all[merge_all['ORDER_STATUS'] != 'canceled']

merge_all['CLUSTER'] = merge_all['user_classification_raw']

table = merge_all.groupby(['ORDER_DATE','CLUSTER'],dropna=False).agg({
    'GMVP': 'sum',
    'ORDER_ID':'nunique'
}).reset_index()
9
table = table.rename(columns={'ORDER_ID':'ORDERS'})

table2 = merge_all.groupby(['ANO_MES','USER_ID'],dropna=False).agg({
    'CLUSTER': 'last',
    'ORDER_DATE':'last'
}).reset_index()

table3 = table2.groupby(['ANO_MES','ORDER_DATE','CLUSTER']).agg({
    'USER_ID': 'nunique'
}).reset_index()

table3.rename(columns={'USER_ID':'USERS'},inplace=True)

final = pd.merge(table,table3,how='left',left_on=['ORDER_DATE','CLUSTER'],right_on=['ORDER_DATE','CLUSTER'])

final = final.drop(columns=['ANO_MES'])

file = r'G:'+mi.pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\gmvp_by_day.csv'

final.to_csv(file, index=False)

load_to_gsheets(file, '.csv', '1QBPcfxqucGalXPUYtetpACbspa58DN1rcaYRVqZHW1Q', 'Placed')

os.remove(file)