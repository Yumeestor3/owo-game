import os
from dotenv import load_dotenv

load_dotenv()

# ============ TELEGRAM CONFIG ============
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_ADMIN_ID = int(os.getenv("TELEGRAM_ADMIN_ID", "0"))

# ============ DATABASE CONFIG ============
DB_PATH = "database/owo_game.db"
CSV_PATH = "data/"

# ============ GAME CONFIG ============
INITIAL_HP = 100
INITIAL_ATK = 10
INITIAL_DEF = 5
INITIAL_KOIN = 0
INITIAL_LEVEL = 1

# ============ LEVEL CONFIG ============
EXP_MULTIPLIER = 1.5
HP_PER_LEVEL = 20
ATK_PER_LEVEL = 5
DEF_PER_LEVEL = 2

# ============ BATTLE CONFIG ============
BATTLE_EXP_BASE = 25
BATTLE_KOIN_BASE = 100

# ============ JELAJAH CONFIG ============
JELAJAH_EXP_MIN = 10
JELAJAH_EXP_MAX = 30
JELAJAH_KOIN_MIN = 50
JELAJAH_KOIN_MAX = 200

# ============ ITEM CONFIG ============
ITEM_SELL_PERCENTAGE = 0.7
RARE_ITEM_DROP_CHANCE = 5
COMMON_ITEM_DROP_CHANCE = 40

# ============ EVENT CHANCES ============
EVENT_HARTA = 40
EVENT_MONSTER = 35
EVENT_ITEM = 15
EVENT_JEBAKAN = 10

# ============ RANKING LIMIT ============
RANKING_LIMIT = 10

# ============ MESSAGE LIMITS ============
MAX_MESSAGE_LENGTH = 200
