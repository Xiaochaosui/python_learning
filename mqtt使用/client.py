#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: W_H_J
@license: Apache Licence
@contact: 415900617@qq.com
@software: PyCharm
@file: clicentMqttTest.py
@time: 2019/2/22 14:19
@describe: mqtt客户端
"""
import json
import sys
import os
import paho.mqtt.client as mqtt
import time

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")

TASK_TOPIC = 'test'  # 客户端发布消息主题

client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
"""
client_id是连接到代理。如果client_id的长度为零或为零，则行为为由使用的协议版本定义。如果使用MQTT v3.1.1，
那么一个零长度的客户机id将被发送到代理，代理将被发送为客户端生成一个随机变量。如果使用MQTT v3.1，那么id将是
随机生成的。在这两种情况下，clean_session都必须为True。如果这在这种情况下不会产生ValueError。
注意：一般情况下如果客户端服务端启用两个监听那么客户端client_id 不能与服务器相同，如这里用时间"20190222142358"作为它的id，
如果与服务器id相同，则无法接收到消息
"""
client = mqtt.Client(client_id, transport='tcp')
client.connect("127.0.0.1", 1883, 60)  # 此处端口默认为1883，通信端口期keepalive默认60
client.loop_start()


def clicent_main(message: str):
    """
    客户端发布消息
    :param message: 消息主体
    :return:
    """
    time_now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    payload = {"msg": "%s" % message, "data": "%s" % time_now}
    # publish(主题：Topic; 消息内容)
    client.publish(TASK_TOPIC, json.dumps(payload, ensure_ascii=False))
    print("Successful send message!")
    return True


if __name__ == '__main__':
    msg = "我是一条测试数据！"
    clicent_main(msg)