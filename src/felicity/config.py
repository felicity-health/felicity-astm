import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DB Connections
DB_NAME = "astm_results"
DB_USER = "nmrl"
DB_PASSWORD = "password"
DB_HOST = "localhost:3306"

# Forward app settings
SENAITE_HOST = "192.168.0.32:80"
SENAITE_BASE_URL = f"http://{SENAITE_HOST}/senaite"
SENAITE_API_URL = f"{SENAITE_BASE_URL}/@@API/senaite/v1"
SENAITE_USER = "system_daemon"
SENAITE_PASSWORD = "s89Ajs-UIas!3k"

# SENAITE.JSONAPI
SEND_TO_QUEUE = True
API_MAX_ATTEMPTS = 10
API_ATTEMPT_INTERVAL = 30

# If Not SENAITE.JSONAPI a.k.a SEND_TO_QUEUE = True
VERIFY_RESULT = False
SLEEP_SECONDS = 5
# logger every ?
SLEEP_SUBMISSION_COUNT = 10
# check the database every :
POLL_BD_EVERY = 1
# on each check, limit results to
RESULT_SUBMISSION_COUNT = 10


EXCLUDE_RESULTS = ["Invalid", "ValueNotSet"]

# Admin pane
STATIC_DIR = f"{BASE_DIR}/dashboard/static"
TEMPLATE_DIR = f"{BASE_DIR}/dashboard/templates"
