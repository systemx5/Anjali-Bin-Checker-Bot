from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21011056"))
    API_HASH = getenv("API_HASH", "696033b1a9c35f0dc027f8ecfbaa9645")
    BOT_TOKEN = getenv("BOT_TOKEN", "6874810677:AAGB-vrroIrrEmkKGpLaN2juKz7hj390UXY")

config = Config()
