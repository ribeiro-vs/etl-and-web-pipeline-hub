from plconfig import MachineInfo as machine_info,SecInfo as sec
from verifiers import send_message
from etltools import SnowFlakeToDF
from datetime import timedelta
from datetime import datetime
from datetimetools import Alternative_date_variables as adv

i=sec()
query = f"""
SELECT * 

FROM {i.a_sales}

WHERE TO_CHAR(TO_DATE("Fecha de entrega", 'MM/DD/YYYY 0:00'), 'YYYY-MM') = '{str(adv().year_hyphen_month)}'

;
"""

file = str(r'G:'+machine_info().pathlang0+r'\Data & Performance\Relatórios de Empresas Parceiras\AMBEV\Detalle de transacci 2024'+str((datetime.today() - timedelta(days=1)).strftime('%m'))+r'.csv')

data = SnowFlakeToDF(query)
data.df_to_csv(file,False)
i=''