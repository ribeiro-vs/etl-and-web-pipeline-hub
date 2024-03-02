# libraries/modules
import pyautogui
import pyperclip
import os
import shutil
from plconfig import MachineInfo
import time
from pytesseract import pytesseract
import time
from verifiers import process_registrant
from datetimetools import Timer
from webactions import Extractor
from datetimetools import Alternative_date_variables
from etltools import FileTransformer

pyautogui.FAILSAFE = False

"""
    It is strictly for the purposes of:
        - Define the steps for performing the extractions.
"""

class ProcessRunner:
    def __init__(self, element):

        self.timer = Timer()
        self.machine_info = MachineInfo()
        self.report = element
        self.name = self.report.name
        self.link = self.report.link
        self.limit_time = self.report.limit_time
        self.original_file = self.report.original_file_name
        self.destination_list = self.report.default_destination_path
        self.error = False
        self.origin = ""
        self.destination = ""
        self.timer.start_count()
        self.first_element = self.destination_list[0]
        _, self.file_format = os.path.splitext(self.first_element)
        
        class_name = type(self.report).__name__
        self.first_class_letter = class_name[0]

    def check_old_files(self):

        sourceLoc = (
            r"C:/Users/" + self.machine_info.win_user_with_path_string + r"/Downloads/"
        )
        
        searchStr = self.original_file
        direc = os.listdir(sourceLoc)

        fileList = []

        for file in direc:

            if file.startswith(searchStr) and file.endswith(self.file_format):
                f = open(sourceLoc + file, "r")
                fileList.append(sourceLoc + file)
                f.close()

        filewpath = "".join(fileList)

        try:
            os.remove(filewpath)

        except:
            pass
        
    def download_gsheets(self):

        try: 
         
            ext = Extractor(self.limit_time,self.link,self.destination_list)
            ext.extract_gs_data()

        except Exception as e:

            process_registrant.register_error('download_gsheets from ProcessRunner: '+str(e))
 
    def download_metabase(self):
        try:   
            ext = Extractor(self.limit_time,self.link,self.destination_list)
            ext.extract_mb_data()    
        except:
            pass
    
    def download_lg(self):
        try:   
            ext = Extractor(self.limit_time,self.link,self.destination_list)
            ext.generate_lg_data()    
        except Exception as e:
            print(str(e))

    def send(self):
        for each_path in self.destination_list:
            try:
                time.sleep(2)
                self.destination = each_path
                shutil.copy(self.origin, self.destination)
            except Exception as e:
                print("ProcessRunner: Error transfering: "+str(e))

    def close_browser(self):
        try:
            time.sleep(2)
            pyautogui.getWindowsWithTitle("Chrome")[0].close()
        except:
            pass

    def check_error(self):
        if self.error:
            self.timer.finish_count()
            errr1 = (
                "ProcessRunner: Error for "
                + self.name
                + f" in (Metabase Script). Execution time: {int(self.timer.minutes)} minutes and {int(self.timer.seconds)} seconds. Started at "
                + self.timer.start
                + " and finished at "
                + self.timer.finish
                + "."
            )
            process_registrant.register_error(errr1)

        else:
            self.timer.finish_count()
            finish_message = (
                "ProcessRunner: "
                + self.name
                + " extraction started at "
                + self.timer.start
                + " finished at "
                + self.timer.finish
                + f". Execution time: {int(self.timer.minutes)} minutes and {int(self.timer.seconds)} seconds."
            )
            process_registrant.register_info(finish_message)
            
    def download_locus(self):
        pass
        
    def download_playvox(self):
        pass

    def download_zendesk(self):
        try: 
         
            ext = Extractor(self.limit_time,self.link,self.destination_list)
            ext.extract_zk_data()
        
        except Exception as e:

            process_registrant.register_error('download_zendesk from ProcessRunner: '+str(e))

    def download_extranet(self):
        pass
             
    def process_sorting(self):
        
        self.process_runner=ProcessRunner(self.report)
        time.sleep(4)
        self.process_runner.timer.start_count()
        if  self.process_runner.error == False and self.first_class_letter   == 'M':
            self.process_runner.download_metabase()
        elif self.process_runner.error  == False and self.first_class_letter == 'G':
            self.process_runner.download_gsheets()
        elif self.process_runner.error == False and self.first_class_letter  == 'P': 
            self.process_runner.download_playvox()
        elif self.process_runner.error == False and self.first_class_letter  == 'L':
            self.process_runner.download_locus()
        elif self.process_runner.error == False and self.first_class_letter  == 'Z':
            self.process_runner.download_zendesk()
        elif self.process_runner.error == False and self.first_class_letter  == 'E':
            self.process_runner.download_extranet() 
        elif self.process_runner.error == False and self.first_class_letter  == 'B':
            self.process_runner.download_lg() 

        self.process_runner.close_browser()      
        self.process_runner.check_old_files()
            
        if self.process_runner.error == False:
            self.process_runner.close_browser()
            self.process_runner.check_old_files()
            
        self.process_runner.check_error() 