import redis

username = input("Username: ")

r = redis.Redis(host='localhost',port=6379)

r.set('username', username)

print(r.get('username'))
r.flushdb()
