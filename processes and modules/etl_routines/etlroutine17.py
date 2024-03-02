import pyodbc
import pandas as pd
from plconfig import MachineInfo as machine_info,SecInfo as sec
import os
from verifiers import send_message
from etltools import PhatomReport,FileToGSheets,SnowFlakeToDF

i=sec()
query = f"""
{i.wlt_query}
"""

file = str(r'G:'+machine_info().pathlang0+r'\Data & Performance\Relatórios de Growth\0 - ECOMMERCE\Wallet Class - BRA.csv')

data = SnowFlakeToDF(query)
data.df_to_csv(file,False)

placed_data_allbases_report = PhatomReport('Wallet Class - BRA',file)
placed_data_load = FileToGSheets(placed_data_allbases_report,'1ACLq8wmqclhh2BT_cVjQ_koehh9S_7HYjjAo5pH6Fm8','Input',False)
placed_data_load.force_load()

os.remove(file)
i=''