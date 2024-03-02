from etltools import FileToGSheets
from reports import MReport63

cupom_all_mx_load = FileToGSheets(MReport63(),'1BCfHxPFKcZiiLL9OeqKR8ALC0Bhni3ClouI8dr3Xsm4','Page1',False)
cupom_all_mx_load.force_load()