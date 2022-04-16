import pymongo

from dotenv import load_dotenv
load_dotenv()

import os

mongo = pymongo.MongoClient(os.environ.get('URI_MONGODB'))
