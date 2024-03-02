from reports import EReport01,EReport02
from etltools import FileToGSheets
import os
from verifiers import send_message

# Google Sheets data load - Ifood Product

keysd      = '1F-BgBPVjqcA4ml3Xdzpo8ZXkrnUT6Yxb0o1K4Tji1bw'
keynm      = '11Wmn2c94zY8iTDNXCt_cEcYXpGh-yEH8CohBQNwNaXQ'

gsheetsload = [[EReport01(),keysd,'SD',True],[EReport02(),keynm,'NM',True]] 

for each in gsheetsload:  
    each = FileToGSheets(each[0],each[1],each[2],each[3])
    each.force_load() 