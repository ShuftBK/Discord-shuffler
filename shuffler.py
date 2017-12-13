import discord
import asyncio
import random
import re
import json
import math
import commands

users = {}
map = []
data = open("data.json","r")
jsonData = json.load(data)
API_Key = jsonData["API_Key"]
Map = jsonData["MAP"]

@commands.client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + commands.client.user.name)
    print('ID: ' + commands.client.user.id)
    for Key,Value in Map.items():
        if  Value == 1:
            map.append(Key)

@commands.client.event
async def on_message(message):
    text = message.content
    print("message : ", text)


    if(text[0] == '$'):
        command = text[1:].split()[0]
        if(command in commands.commands):
            await commands.commands[command](message, users=users, map=map)
            print(users)

commands.client.run(API_Key)