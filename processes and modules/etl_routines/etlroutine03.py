import pandas as pd
from reports import MReport41,AReport01,AReport02
from etltools import FileToGSheets
from plconfig import MachineInfo
import os
from verifiers import send_message

# Google Sheets data load

all_bases     = '1QBPcfxqucGalXPUYtetpACbspa58DN1rcaYRVqZHW1Q'
cuponclass_br = '17CFjwuAFKejYNV0mCEIxRcY09vKLPgggveiNLq1TiNI'
android       = '1mlhF7hzp29VGSeP2cj11Cja4a4Rwf5vyXvNw4KPRzQg'
ios           = '1TKE8ZGlX3lE74BkzR2JRwbiAwyMirEHt6apTOLj9LDY'

gsheetsload = [
 [MReport41(),cuponclass_br,'Input',True]
,[AReport01(),android,'android',False]
,[AReport02(),ios,'ios',False]] 

for each in gsheetsload:  
    each = FileToGSheets(each[0],each[1],each[2],each[3])
    each.force_load() 