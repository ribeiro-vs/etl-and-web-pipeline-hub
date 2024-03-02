import pyodbc
import pandas as pd
from plconfig import MachineInfo as machine_info,SecInfo as sec
from datetimetools import Alternative_date_variables as ad
import os
from azure.storage.blob import BlobServiceClient
from datetime import timedelta
from datetime import datetime
from verifiers import send_message
from etltools import SnowFlakeToDF
from plconfig import SecInfo as sec

i=sec()
query = f"""
SELECT * 
FROM {i.u_stock}
;
"""

file = str(r'G:'+machine_info().pathlang0+r'\Data & Performance\Relatórios de Empresas Parceiras\UNILEVER\envios estoque\2024-'+str((datetime.today() - timedelta(days=1)).strftime('%m'))+r'.csv')

myclass = SnowFlakeToDF(query)
myclass.df_to_csv(file,False)

sas_url = sec().sas_url_unilever 
blob_service_client = BlobServiceClient(account_url=sas_url)

files = [file]

try:
    for each in files:
        blob_name = os.path. basename(each)
        blob_client = blob_service_client.get_blob_client(container='envios estoque', blob=blob_name)

        with open(each, 'rb') as data:
            blob_client.upload_blob(data, overwrite=True)

        print("Unilever stock file succesfully uploaded ("+str(each)+").")

except Exception as e:
    e9="<!channel> Unilever stock file didn't uploaded. Details: "+"\n\n"+str(e)
    print(e9)
    send_message(e9,'bot_channel')

i=''