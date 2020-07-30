#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:30:04 2020

@author: wuhongfei
"""

#引入哈希库
import hashlib as hasher
 #在编写接口传递数据时，往往需要使用JSON对数据进行封装。python和json数据类型的转换，看作为编码与解码。
import json
 #initialize the blockchain
blockchain=[]
 
def hash(data,previous_hash):
     sha=hasher.sha256()#define the sha256 algorithm in hashlib as sha for convinence
     sha.update("{0}{1}".format(data, previous_hash).encode("utf8"))
     return sha.hexdigest()
 
 
def make_a_block(data,previous_hash):
    block={}
    block["data"]=data
    block["previous_hash"]=previous_hash
    block["hash"]=hash(data,previous_hash)
    return block

def add_a_block(data):
    
    last_block=blockchain[len(blockchain)-1]
    previous_hash=last_block["hash"]
    blockchain.append(make_a_block(data, previous_hash))
    
def make_a_genesis_block():
    data="this is the genesis block"
    previous_hash=0
    blockchain.append(make_a_block(data, previous_hash))
    
if __name__=='__main__':
    make_a_genesis_block()
    add_a_block("this is block 1")
    add_a_block("this is block 2")
    add_a_block("this is block 3")
    print(json.dumps(blockchain))
    