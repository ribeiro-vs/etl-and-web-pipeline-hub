from azure.storage.blob import BlobServiceClient
from plconfig import MachineInfo as machine_info, SecInfo as sec
from datetimetools import Alternative_date_variables as ad
from verifiers import send_message

machine_info = machine_info()
ad = ad() 

sas_url = sec().sas_url_unilever
 
file = 'unilever_'+str(ad.year_month)+'.csv'

blob_service_client = BlobServiceClient(account_url=sas_url)
local_file_path = r'G:'+machine_info.pathlang0+r'\Data & Performance\Relatórios de Empresas Parceiras\UNILEVER\unilever_'+str(ad.year_month)+r'.csv'
blob_name = file

blob_client = blob_service_client.get_blob_client(container='envios', blob=blob_name)

try:
    with open(local_file_path, 'rb') as data:
        blob_client.upload_blob(data, overwrite=True)

    print("Unilever sales file succesfully uploaded.")
except Exception as e:
    e6="Unilever sales file didn't uploaded. Details:"+'\n\n'+str(e)
    print(e6)
    send_message(e6,'bot_channel')