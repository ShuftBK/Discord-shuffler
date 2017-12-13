import discord
import asyncio
import random
import re
import json
import math

client = discord.Client()

@client.event
async def addme(message, **kwargs):
    users = kwargs.get('users', None)
    name = message.author.name
    level = 1
    users[name] = level
    await client.send_message(message.channel, '{} add shuffle users list.'.format(name))

@client.event
async def addall(message, **kwargs):
    users = kwargs.get('users', None)
    channelid = message.content.split(' ', 1)[1]
    for member in client.get_channel(channelid).voice_members:
        level = 1
        users[member.name] = level

@client.event
async def add(message, **kwargs):
    users = kwargs.get('users', None)
    name = message.content.split(' ', 1)[1]
    level = 1
    users[name] = level
    await client.send_message(message.channel, '{} add shuffle users list.'.format(name))

@client.event
async def flushme(message, **kwargs):
    users = kwargs.get('users', None)
    del users[message.author.name]
    await client.send_message(message.channel, 'flush {} list data.'.format(message.author.name))

@client.event
async def flushall(message, **kwargs):
    users = kwargs.get('users', None)
    users.clear()
    await client.send_message(message.channel, "flush all user list data.")

@client.event
async def flush(message, **kwargs):
    users = kwargs.get('users', None)
    name = message.content.split(' ',1)[1]
    if(name in users.keys()):
        del users[name]
    await client.send_message(message.channel, 'flush {} list data.'.format(name))

@client.event
async def map(message, **kwargs):
    map = kwargs.get('map', None)
    await client.send_message(message.channel, random.choice(map))

@client.event
async def show(message, **kwargs):
    users = kwargs.get('users', None)
    await client.send_message(message.channel, "Total User :" + str(len(users)))
    await client.send_message(message.channel, users)

@client.event
async def testdata(message, **kwargs):
    users = kwargs.get('users', None)
    users.update({"luna":1,"Uroro":1,"kiritan":1,"Qoo":1,"Testudines":1,"homuman":1})

@client.event
async def shuffle(message, **kwargs):
    users = kwargs.get('users', None)
    map = kwargs.get('map', None)
    userlist = list(users.keys())
    random.shuffle(userlist)
    result = "Map : "
    result += random.choice(map) + "\n"
    userlen = len(userlist)
    for i in range(userlen):
        if(i == 0):
            result += "```Blue Team : "
        elif(i == math.floor(userlen / 2)):
            result += "\nOrange Team : "
        result += userlist[i] + ", "

    else:
        result += "```"

    await client.send_message(message.channel, result)

@client.event
async def help(message, **kwargs):
    result = '''
            !add user1 user2 ... \t-> 指定ユーザをリストに追加 \n
            !addme\t-> 自身をリストに追加 \n
            !addall channelid\t-> あるボイスチャンネルにいるすべてのユーザをリストに追加\n
            !flush user1 user2 ...\t-> 指定ユーザをリストから削除 \n
            !flushme\t-> 自身をリストから削除 \n
            !flushall\t-> すべてのユーザをリストから削除\n
            !map\t-> [deprecated] ランダムでマップを出力\n
            !shuffle\t-> チーム分けを行う \n
            !showlist\t-> 現在のリストを出力 \n
            \n
            Debug Commands\n
            !testdata\t-> テストデータを追加
            '''
    await client.send_message(message.channel, result)

commands = {
    'addme' : addme,
    'addall' : addall,
    'add' : add,
    'flushme' : flushme,
    'flushall' : flushall,
    'flush' : flush,
    'map' : map,
    'show' : show,
    'testdata' : testdata,
    'shuffle' : shuffle,
    'help' : help
    }