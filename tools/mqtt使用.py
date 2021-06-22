# -*- coding: utf-8 -*-
# 以下代码在2019年2月28日 python3.6环境下运行通过
import paho.mqtt.client as mqtt
import json
import time

# HOST = "192.168.0.12"
HOST = "localhost"
PORT = 1883
client_id = "1083421xxxxx"                       # 没有就不写，此处部分内容用xxx代替原内容，下同


# 连接 mqtt服务器
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("data/receive")         # 订阅消息

# 消息处理函数
def on_message(client, userdata, msg):
    print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))

# publish 消息
def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)

# 断开连接
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)

data = {
    "type":2,
    "timestamp": time.time(),
    "messageId":"9fcda359-89f5-4933-xxxx",
    "command":"xx/recommend",
    "data":{
        "openId":"xxxx",
        "appId":'xxxx',
        "recommendType":"temRecommend"
    }
}
param = json.dumps(data)
client = mqtt.Client(client_id)
client.username_pw_set("xxxxxx", "xxxxxx")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
client.connect(HOST, PORT, 60)
client.publish("data/send", payload=param, qos=0)     # 发送消息
client.loop_forever()

