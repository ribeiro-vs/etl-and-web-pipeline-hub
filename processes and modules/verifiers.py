import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime, timedelta
import shutil
import logging
from plconfig import MachineInfo

"""
    It is strictly for the purposes of:
        - Slack bot configuraton, alerting, and logging with environmental configuration and system-specific settings.
"""
machine_info = MachineInfo()
env_path = Path(r'G:'+machine_info.pathlang3+r'\API KEYS\Slack Bot - Files\.env.txt')
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['PRODUCTION_SLACK_TOKEN'])

def inst_verify(list_of_paths,channel_name=None):
    message_format ='\n    - '
    mini_list = []

    for each in list_of_paths:
        with_extension = os.path.basename(each)
        report_name = os.path.splitext(with_extension)[0]
        msg = message_format+report_name

        try:
            each.stat()
            res = each.stat().st_mtime
            datetime.fromtimestamp(res).isoformat()
            file_lastmod_time = datetime.fromtimestamp(res)
            now = datetime.now()
            timesubtraction = now - file_lastmod_time

            if timesubtraction < timedelta(hours = 0.5):
                pass

            else:                
                mini_list.append(msg)

        except:
            print('Path verifier message: Error while verifying :'+msg)
            mini_list.append(msg)

    if mini_list == []:
        return True
    
    else:
        all=""

        for each in mini_list:

            all = all+each 

        message = "Olá <!channel> essas bases tiveram falhas em suas extrações:"
        message = message + all

        if channel_name:
            client.chat_postMessage(link_names=1, channel = channel_name,  text = message)
            return False
        
        return False

def send_message(message,channel_name):
    try:
        client.chat_postMessage(link_names=1, channel = channel_name,  text = message)
    except Exception as e:
        print(message+' '+ str(e))

class ProcessRegistrant:

    def __init__(self): 

        self.src = r'log_file.log'
        self.des = r'G:'+machine_info.pathlang0+r'\Data & Performance\Relatórios\Log Diário - Automação\log_file.log'

        # Logger config
        self.logger = logging.getLogger('Guardian:')
        self.logger.setLevel(logging.INFO)

        # Handler to write in file
        file_handler = logging.FileHandler("log_file.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))

        # Handler to display info in terminal
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # Both handles in logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

        if not machine_info.win_user_with_path_string == r'\\Dashboard':
            self.machine='Dante'
        else:
            self.machine='Da Vinci'

        self.crt = "A automação do "+self.machine+" parou."

    def call_critical(self):
        self.logger.critical(self.crt)
        send_message('CRITICAL ERROR - The process automation management has stopped  <!channel> .', 'bot_channel')

    def register_info(self, info):
        self.logger.info(info)
        shutil.copy(self.src, self.des)

    def register_error(self, error):
        self.logger.error(error)
        shutil.copy(self.src, self.des)
        send_message(error+'\n <!channel>', 'bot_channel')

process_registrant = ProcessRegistrant()