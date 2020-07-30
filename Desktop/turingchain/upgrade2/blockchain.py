#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:47:14 2020

@author: wuhongfei
"""

#引入哈希库
import hashlib as hasher
 #在编写接口传递数据时，往往需要使用JSON对数据进行封装。python和json数据类型的转换，看作为编码与解码。
import json
from time import time
from flask import Flask, jsonify
 #initialize the blockchain
blockchain=[]
 
def hash(index,data,timestamp,previous_hash):
     sha=hasher.sha256()#define the sha256 algorithm in hashlib as sha for convinence
     sha.update("{0}{1}{2}{3}".format(index,data,timestamp,previous_hash).encode("utf8"))
     return sha.hexdigest()
 
 
def make_a_block(index,timestamp,data,previous_hash):
    block={}
    block["index"]=index
    block["timestamp"]=timestamp
    block["data"]=data
    block["previous_hash"]=previous_hash
    block["hash"]=hash(index, data, timestamp, previous_hash)
    return block

def add_a_block(data):
    
    last_block=blockchain[len(blockchain)-1]
    index=last_block["index"]+1
    timestamp=int(round(time()*1000))
    previous_hash=last_block["hash"]
    blockchain.append(make_a_block(index, timestamp, data, previous_hash))
    
def make_a_genesis_block():
    index=0
    timestamp=int(round(time()*1000))
    data="Genesis block"
    previous_hash=0
    blockchain.append(make_a_block(index, timestamp, data, previous_hash))

app=Flask(__name__)

@app.route('/',methods=['GET'])
def get_blockchain():
    return jsonify(blockchain)

@app.route('/say/<string:msg>',methods=['GET'])
def add_blockchain(msg):
    add_a_block(msg)
    return jsonify(blockchain)

    
if __name__=='__main__':
    make_a_genesis_block()
    add_a_block("hello")
    add_a_block("hi~")
    add_a_block("~")
    app.run(debug=True,host='0.0.0.0',port=8080)
    print(json.dumps(blockchain))