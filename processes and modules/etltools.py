import pandas as pd
import os
import shutil
from verifiers import process_registrant
import gspread 
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials
import pyodbc
from plconfig import SecInfo as sec

"""
    It is strictly for the purposes of:
        - Store time-related classes.
"""

class GSheetDataLoader:

    def __init__(self,key,sheet):
        self.data = None
        self.name = None
        self.key = key
        self.sheet = sheet
        self.service_account = r'G:\Meu Drive\API KEYS\Google Cloud\titanium-cacao-363112-81ea07cec0ec.json'

    def load_to_gsheets(self):
        try:
            SCOPES = ['https://www.googleapis.com/auth/cloud-platform','https://www.googleapis.com/auth/drive',]

            credentials = ServiceAccountCredentials.from_json_keyfile_name(self.service_account,SCOPES)

            gc = gspread.authorize(credentials)

            wks = gc.open_by_key(self.key)
            
            worksheet = wks.worksheet(self.sheet)
                
            worksheet.clear()
            
            worksheet.update('A1', 'data')

            v = [e[0:1] for e in worksheet.get_all_values()] 

            updated = self.data

            gd.set_with_dataframe(worksheet, updated)

            process_registrant.register_info(f'load_to_gsheets from GSheetDataLoader: {self.name} data was successfully loaded to Google Sheet.')

        except Exception as e:
            process_registrant.register_error(f'load_to_gsheets from GSheetDataLoader: {e}.')

class FileToGSheets(GSheetDataLoader):

    def __init__(self,element,key,sheet,drop_duplicates=False): 
            super().__init__(key,sheet) # Initiating common attributes on the superclass by instantiating the superclass
            self.report = element
            self.name = self.report.name
            self.path = self.report.default_destination_path[0]
            _, self.format = os.path.splitext(self.path)
            self.duplicates_elimination = drop_duplicates

    def read_file(self):
        if self.format == '.csv':
            try:
                self.data = pd.read_csv(self.path,sep=',')
                return self.data
            except Exception as e:
                process_registrant.register_error(f'read_file from FileToGSheets: {e}')  

        elif self.format != '.csv':
            try:
                self.data = pd.read_excel(self.path)
                return self.data
            except Exception as e:
                return process_registrant.register_error(f'read_file method from GSheetDataLoader: : {e}') 
        else:
            return process_registrant.register_error(f'read_file method from GSheetDataLoader: : {e}')
            
    def prepare_data(self):
        try:
            if self.duplicates_elimination:
                self.data.drop_duplicates(inplace=True)
        except Exception as e:
            process_registrant.register_error(f'prepare_data method from GSheetDataLoader: : {e}')

    def force_load(self):
        self.read_file()
        self.prepare_data()
        self.load_to_gsheets()


class PhatomReport:

    def __init__(self,name,path):
        self.name = name
        self.default_destination_path = [path]

class SnowFlakeToDF:

    def __init__(self,query):
        self.query=query

    def connect_to_sf(self):
        conn_str = f"DSN=Snowflake;UID=VINICIUS_RIBEIRO;PWD={sec().snf_pss};"
        try:
            conn = pyodbc.connect(conn_str)
            return conn
        except Exception as e:
            process_registrant.register_error(f'connect_to_sf method from SnowFlakeToDF: : {e}')
            return None

    def create_df(self):
        conn = self.connect_to_sf()
        if conn is not None:
            try:
                df = pd.read_sql(self.query,conn)
                return df
            except Exception as e:
                process_registrant.register_error(f'create_df method from SnowFlakeToDF: {e}')
                return None
        else:
            return None
    
    def df_to_csv(self,file,index=False,separator=None):
        df = self.create_df()
        if df is not None:
            if separator == ';':
                df.to_csv(file, sep=';', index=index)
            else:
                df.to_csv(file,index=index) 
        else:
            process_registrant.register_error(f'df_to_csv method from SnowFlakeToDF: Dataframe is none')