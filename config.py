import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "7603458")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "910e420f1f74f40305a684a331dade35") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7439562089:AAHTShMmNnB5gSptlZgrty1pPKqjv6CMaCc") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002075434712') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://sharku:zKKosLfBvResoqhF@cluster0.jped6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SharkEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6066102279")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002368843413')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/Shinobuv3-01-28")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8279"))

    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
