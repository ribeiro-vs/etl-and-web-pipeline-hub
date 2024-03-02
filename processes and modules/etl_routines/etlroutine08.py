from reports import MReport41
from etltools import FileToGSheets,PhatomReport
from plconfig import machine_info
from verifiers import send_message
import os
  
key = '15vxsDIcnR-UGxDfpXorf4SqcT-HqhZmuWlLVa5-D4XE'
lg_path= r'G:'+machine_info.pathlang0+r'\Data & Performance\Relatórios\0 - BASES UNIVERSAIS\Base LG\Base LG.xlsx'
 
lg_report = PhatomReport('Base LG',lg_path)
cupom_all_br_load = FileToGSheets(lg_report,'15vxsDIcnR-UGxDfpXorf4SqcT-HqhZmuWlLVa5-D4XE','Base LG',True)
cupom_all_br_load.force_load()