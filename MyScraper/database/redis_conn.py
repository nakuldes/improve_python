import redis

class URLCache():
    def __init__(self):
        self.r = redis.Redis()

    def setting_value_to_redis(self, url, val)->bool:
        self.r.set(url, val)
        return True

    def getting_value_from_redis(self, url):
        val = self.r.get(url)
        return val


# val = '1'
# if (r.get(val)) != None:
#     print('Hit')
#     print(str(r.get(val)))