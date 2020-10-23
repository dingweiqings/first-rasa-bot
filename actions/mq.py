#!/bin/python3
# -*- coding: utf-8 -*-
import pika
credentials = pika.PlainCredentials('guest', 'guest')  # 用户名密码
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '10.10.10.37', 5672, '/', credentials))     #定义连接池
channel = connection.channel()
channel.queue_declare(queue='test')    #声明队列以向其发送消息消息
channel.basic_publish(exchange='', routing_key='test', body='Hello World!')  #注意当未定义exchange时，routing_key需和queue的值保持一致
print('send success msg to rabbitmq')
connection.close()   #关闭连接
