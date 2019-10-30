import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:

    SECRET_KEY = "$#@!@#%&_patinhas*&$5512019euddgeydc"
    MONGO_DBNAME = "lisbrain"
    MONGO_URI = "mongodb://127.0.0.1:27017/lisbrain"


key = Config.SECRET_KEY
