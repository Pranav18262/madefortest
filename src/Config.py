import os

class Config:
    aid = int(os.environ.get("7941936")
    ahash = os.environ.get("6db0cab0f0a81879cd82d4fff6b2f608
")
    bot_token = os.environ.get("1846833063:AAH-v4vgsai6dD_akKEhUvR6wjOp86w9MPM")
    sudo = [239508098, 1313665327]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
