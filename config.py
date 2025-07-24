from os import getenv


API_ID = int(getenv("API_ID", "27381416"))
API_HASH = getenv("API_HASH", "2233a4c98bcbbe74dbfbaaf1ede5669d")
BOT_TOKEN = getenv("BOT_TOKEN", "7672938818:AAGsvUqtByoD85C1QOas9tpdJY6xhnT7mWE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5284903709").split()))
MONGO_DB = getenv("MONGO_DB", "")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002727252013"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002613730752"))


