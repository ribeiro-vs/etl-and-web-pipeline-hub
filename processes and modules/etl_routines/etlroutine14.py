from reports import MReport61
from etltools import FileToGSheets
import os
from verifiers import send_message

cupom_all_mx_load = FileToGSheets(MReport61(),'1NKbFcNHg13nnxZAt76yOLYKVwxLTG3VirvA33OkYYO8','Input',True)
cupom_all_mx_load.force_load()