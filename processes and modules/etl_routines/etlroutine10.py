from plconfig import MachineInfo as machine_info,SecInfo as sec
from datetimetools import Alternative_date_variables as ad
import os
from azure.storage.blob import BlobServiceClient
from datetime import timedelta
from datetime import datetime
from verifiers import send_message

machine_info = machine_info()
ad = ad() 

file = str(r'G:'+machine_info.pathlang0+r'\Data & Performance\Relatórios de Empresas Parceiras\AMBEV\Detalle de transacci 2024'+str((datetime.today() - timedelta(days=1)).strftime('%m'))+r'.csv')

sas_uri = sec().sas_url_ambev 
 
blob_service_client = BlobServiceClient(account_url=sas_uri)

files = [file]

try:
    for each in files:
        
        blob_name = os.path. basename(each)
        blob_client = blob_service_client.get_blob_client(container='redejusto', blob=blob_name)
        with open(each, 'rb') as data:
            blob_client.upload_blob(data, overwrite=True)

        print("Ambev sales file succesfully uploaded ("+str(each)+").")

except Exception as e:
    e10=f"Ambev sales file didn't uploaded. Exception: {e}"
    print(e10)
    send_message(e10,'bot_channel')