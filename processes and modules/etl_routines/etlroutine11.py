from reports import MReport47
from etltools import FileToGSheets

cupom_all_load = FileToGSheets(MReport47(),'1A-FQ3NwJ5quBNRllQkUHhtHehjrRPoHgKKRU1tio9nE','gestao_a_vista',False)
cupom_all_load.force_load()