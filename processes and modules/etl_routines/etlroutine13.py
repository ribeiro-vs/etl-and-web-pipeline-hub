from reports import AReport01,AReport02
import requests
from verifiers import send_message
from datetimetools import Metabase_date_format as mbdf

# Google Sheets data load

mbdf = mbdf()

re1 =[AReport01().name,AReport01().default_destination_path[0],'https://hq1.appsflyer.com/api/agg-data/export/app/mx.justo.android/geo_by_date_report/v5?from='+mbdf.past_month_first_day+'&to='+mbdf.today,"Bearer eyJhbGciOiJBMjU2S1ciLCJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwidHlwIjoiSldUIiwiemlwIjoiREVGIn0.yvc1-Cy2oLB_lLOBJbK3UO7DD1wVL-S-HKvvFEQkgT3NhkQawD_iLQ.xOnSJycFBo69fTAg.BXAgU_1Mtm4z1a9QiOFjfXEc5Q2A0OnLr5QTPDJKx7Sq2DjKP0ThYYoyYml94yt_saPN-WAN5JqzkzNOV2ztiEZD7Tk1QZthWO6nibiUz7pwj13C897LN26GAqPV-O8XsZCOrV_glAf9Nb55-hpl_yIFqtdO810K_kD1peaSKx9sfUmnJPWT0UtFesIyRhEFA9Wd7qu8GTjOvWzZPALLaVgWpx9J4U1nbOxKRInQy3Eq520Lg56Thgp5Mq3RmeIgzacymg8z_oIof1mJWpKiKwEuOopYr4MNVcIKxkYmfxUpLrhFoenQzgsA4ex5Y3e5HSQxR54AACZ6iEMpWR4Uv9L5QuclDAcYUtWA1FWUUTpdD12sz78GIjIl0FsyuZ51g2VAP71gxImKn8u-ZL3qKHh-j92CMBh_dsQfECahcU7F_GixH8EX9wSh7ksFtot5vOcNIc9ymelw-QM8FJQK3c_2vM4JQPFv3sBmB44tHOpvAdF4FdA4UojO1JEwiEkAwyRc3UCq4mpvypPE1VpGsFXF.XlaroQhy2Ya1v_LQJoUHgw"]
re2 =[AReport02().name,AReport02().default_destination_path[0],'https://hq1.appsflyer.com/api/agg-data/export/app/id1491969468/geo_by_date_report/v5?from='+mbdf.past_month_first_day+'&to='+mbdf.today,"Bearer eyJhbGciOiJBMjU2S1ciLCJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwidHlwIjoiSldUIiwiemlwIjoiREVGIn0.yvc1-Cy2oLB_lLOBJbK3UO7DD1wVL-S-HKvvFEQkgT3NhkQawD_iLQ.xOnSJycFBo69fTAg.BXAgU_1Mtm4z1a9QiOFjfXEc5Q2A0OnLr5QTPDJKx7Sq2DjKP0ThYYoyYml94yt_saPN-WAN5JqzkzNOV2ztiEZD7Tk1QZthWO6nibiUz7pwj13C897LN26GAqPV-O8XsZCOrV_glAf9Nb55-hpl_yIFqtdO810K_kD1peaSKx9sfUmnJPWT0UtFesIyRhEFA9Wd7qu8GTjOvWzZPALLaVgWpx9J4U1nbOxKRInQy3Eq520Lg56Thgp5Mq3RmeIgzacymg8z_oIof1mJWpKiKwEuOopYr4MNVcIKxkYmfxUpLrhFoenQzgsA4ex5Y3e5HSQxR54AACZ6iEMpWR4Uv9L5QuclDAcYUtWA1FWUUTpdD12sz78GIjIl0FsyuZ51g2VAP71gxImKn8u-ZL3qKHh-j92CMBh_dsQfECahcU7F_GixH8EX9wSh7ksFtot5vOcNIc9ymelw-QM8FJQK3c_2vM4JQPFv3sBmB44tHOpvAdF4FdA4UojO1JEwiEkAwyRc3UCq4mpvypPE1VpGsFXF.XlaroQhy2Ya1v_LQJoUHgw"]

appsflyer = [re1,re2]

for each in appsflyer:

    url = each[2]
    headers = {
        "accept": "text/csv",
        "authorization": each[3]
    }
    response = requests.get(url, headers=headers)

    try:
        with open(each[1], 'w', encoding='utf-8') as f:
            f.write(response.text)
    except Exception as e:
        err='<!channel> Error while downloading '+each[1]+' report.'
        print(err)
        send_message(err,'bot_channel')