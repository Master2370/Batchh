# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

# One == Physics Wallah (PW)
# Two == ClassPlus (CP)
# Three == Appx

import os

api_id = int(os.environ.get("API_ID", "35401014"))
api_hash = os.environ.get("API_HASH", "dedefdfc7f4837095e425af92a4839d0")
bot_token = os.environ.get("BOT_TOKEN", "8963894435:AAEIlJOL3yhRhTrVsR1GbL8wxU1CG5V1n2I")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "1868792620").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")

# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
