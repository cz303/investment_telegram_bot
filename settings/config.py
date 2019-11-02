from settings.logger import set_up_logging, logging

DEBUG = True

# setup loggers
set_up_logging(level=logging.DEBUG)

# bot
PRODUCTION_TOKEN = '1065557544:AAEzzrCLkbLD9ikZDhuJ2_vV80L316frYbw'
TEST_TOKEN = '979472521:AAHW7Csof_4gGjhEx49luK4gkBYwry0ABSE'
API_TOKEN = TEST_TOKEN if DEBUG else PRODUCTION_TOKEN
BOT = 'bitpif_bot' if DEBUG else 'BitpifBot'

# botan
BOTAN_KEY = 'bf7b036e-ed0b-40ea-bba2-ce54b50dcc73'

# webhook
WEBHOOK_HOST = 'bitpif.herokuapp.com'  # old '95.172.133.74'
WEBHOOK_PORT = 'PORT'  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_URL_PATH = f"{API_TOKEN}/"
WEBHOOK_URL_BASE = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}/{WEBHOOK_URL_PATH}"

WEBHOOK = {
    'listen': WEBHOOK_HOST,
    'port': WEBHOOK_PORT,
    'url_path': WEBHOOK_URL_PATH,
}

# database
DATABASE_NAME = 'heroku_6882c2094ce1891' if DEBUG else 'heroku_6882c2094ce1891'
DATABASE_USER = 'bf96087e84c5d4'
DATABASE_HOST = 'eu-cdbr-west-02.cleardb.net'
DATABASE_PASSWORD = 'b4d096d3'

# groups
ADMINS = [677805757]

# nodes
# TODO: сменить порты!!!!!!!!!!!!!
RPC = {
    'btc': {'port': 18332, 'password': 'TuZ0GQ69C8wW'},
    'bch': {'port': 18432, 'password': 'txbZ3YI653PtVbulWZXZoFSbyXuJBrq5'},
    'zec': {'port': 18232, 'password': 'myhkwsH707qObV1592beEv6LvXXvancM'}
}

# formats
CURRENCY_FMT = {
    'rub': 0,
    'usd': 2,
    'btc': 8
}
