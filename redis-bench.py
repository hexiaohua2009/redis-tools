#!/usr/bin/python
# Auther: hexh
# Contact: 1282037943@qq.com
# Date: 20200523

from rediscluster import RedisCluster
import sys

# 封装redis cluster对象
class redisClusterHelper():
    def __init__(self,startup_nodes,password):
        try:
            self.redisconn = RedisCluster(startup_nodes=startup_nodes,password=password,decode_responses=True)
        except Exception as e:
            print("Connect Error: {0}".format(e))
            sys.exit()
    def set_key(self,key,value):
        return self.redisconn.set(key,value)
    def get_key(self,key):
        return self.redisconn.get(key)

if __name__ == '__main__':
    # 配置redis cluster中的master节点
    startup_nodes = [
        {'host': '192.168.0.32', 'port': 6379},
        {'host': '192.168.0.34', 'port': 6379},
        {'host': '192.168.0.32', 'port': 6380}
    ]
    # 创建实例
    rch = redisClusterHelper(startup_nodes,'123456')
    # 插入数据
    count = 0
    kvs = 1000000
    while count < kvs:
        rch.set_key("name" + str(count), 'admin' + str(count))
        print(rch.get_key('name'+ str(count)))
        count = count + 1