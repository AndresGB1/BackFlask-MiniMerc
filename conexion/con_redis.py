import redis

from dotenv import load_dotenv
load_dotenv()

import os



redis =  redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), password=os.environ.get('REDIS_PASSWORD'))
                 


