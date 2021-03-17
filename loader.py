from pyrogram import Client, filters, types
from database.dbrequests import DbRequests
from loguru import logger

# init pyrogram client
app = Client("accounts/380630328469")

# init db
db = DbRequests(r'C:\Users\sasha\Desktop\parser\marketingbot\database\database.db')

# logging
logsDirect = "logs/logs.log"
logger.add(logsDirect, format='{message}', enqueue=True, rotation="00:00", compression="zip", level="INFO", catch=True)
