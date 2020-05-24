#!/usr/bin/python
# Auther: hexh
# Contact: 1282037943@qq.com
# Date: 20200523

from rediscluster import RedisCluster
import sys

class redisClusterHelper():
    def __init__(self,startup_nodes):
        try:
            self.redisconn = RedisCluster(startup_nodes=startup_nodes,password='123456',decode_responses=True)
        except Exception as e:
            print("Connect Error: {0}".format(e))
            sys.exit()
    def set_key(self,key,value):
        return self.redisconn.set(key,value)
    def get_key(self,key):
        return self.redisconn.get(key)

if __name__ == '__main__':
    startup_nodes = [
        {'host': '192.168.0.32', 'port': 6379},
        {'host': '192.168.0.34', 'port': 6379},
        {'host': '192.168.0.32', 'port': 6380}
    ]
    rch = redisClusterHelper(startup_nodes)
    count = 0
    while count < 1000000:
        rch.set_key("name" + str(count), 'admin' + str(count))
        print(rch.get_key('name'+ str(count)))
        count = count + 1