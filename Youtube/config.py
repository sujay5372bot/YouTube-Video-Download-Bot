import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7605940903:AAGo-TL_WBzWjIus2Qjc6mx6ABdghOxgJCc")
    API_ID = int(os.environ.get("API_ID", "24935727"))
    API_HASH = os.environ.get("API_HASH", "3fd33336629324ecd664e9b6894f0909")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002213757803")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
