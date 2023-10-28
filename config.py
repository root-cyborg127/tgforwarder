from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "ff1c4e5d3c139a2aa14ae7681bc9bb06")
      API_ID = int(getenv("API_ID", "13601023"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6980433710:AAEZFkdi8lRJMCTM57MTl0O8OlkPAId-e-w")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002030287366:-1001993131334").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
