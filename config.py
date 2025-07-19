from os import getenv


API_ID = int(getenv("API_ID", "16253557"))
API_HASH = getenv("API_HASH", "81171c25e4cb9062cb10da8b7730432a")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1996039956").split()))
MONGO_DB = getenv("MONGO_DB", "")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002368258171"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002205282436"))


