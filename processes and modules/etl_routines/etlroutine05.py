import pandas as pd
import numpy as np
from plconfig import MachineInfo as machine_info, SecInfo as sec
from datetimetools import Alternative_date_variables as ad
from verifiers import send_message
from etltools import SnowFlakeToDF

machine_info = machine_info()
try:
    
    destination = r'G:'+machine_info.pathlang0+r'\Data & Performance\Relatórios de Empresas Parceiras\UNILEVER\unilever_'+str(ad().year_month)+r'.csv'
    
    i=sec()
    query = f"""
    SELECT * 
    FROM {i.u_sales}
    WHERE TO_CHAR(TO_DATE("Delivery_date",'MM-DD-YYYY'),'MM-YYYY') = '{str(ad().month_hyphen_year)}';
    """

    sf_data = SnowFlakeToDF(query)
    sf_data.df_to_csv(destination,False)  
    i=''

except:
    emsg='<!channel> Error while doing the Unilever sales ETL (etl5).'
    print(emsg)
    send_message(emsg,'#bot_channel')