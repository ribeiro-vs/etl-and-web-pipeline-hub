import pyodbc
import pandas as pd
from plconfig import MachineInfo as machine_info,SecInfo as sec
import os
from azure.storage.blob import BlobServiceClient
from verifiers import send_message
from etltools import PhatomReport,FileToGSheets,SnowFlakeToDF

i=sec()
query = f"""
SELECT * 

FROM {i.pc_sales}

;
"""

file = str(r'G:'+machine_info().pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\order_history_new\gmvp_by_day.csv')

data = SnowFlakeToDF(query)
data.df_to_csv(file,False)

placed_data_allbases_report = PhatomReport('Base LG',file)
placed_data_load = FileToGSheets(placed_data_allbases_report,'1QBPcfxqucGalXPUYtetpACbspa58DN1rcaYRVqZHW1Q','Placed',True)
placed_data_load.force_load()
i=''