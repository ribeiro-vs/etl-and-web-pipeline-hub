from reports import MReport41
from etltools import FileToGSheets 

cupom_all_load = FileToGSheets(MReport41(),'17CFjwuAFKejYNV0mCEIxRcY09vKLPgggveiNLq1TiNI','Input',True)
cupom_all_load.force_load()