import discord
import asyncio
import random
import re
import json
import math

client = discord.Client()
userdict = {}
map = []
data = open("data.json","r")
jsonData = json.load(data)
API_Key = jsonData["API_Key"]
Map = jsonData["MAP"]

for Key,Value in jsonData["MAP"].items():
    if  Value == 1:
        map.append(Key)
print(map)

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


@client.event
async def on_message(message):
    global userdict
    global map
    print("message : ",message.content)

    if message.content.startswith('!addme'):
        username = message.author.name
        level = 1
        userdict.update({username:level})
        await client.send_message(message.channel, '{} add shuffle users list.'.format(username))
        print(userdict)

    elif message.content.startswith('!addall'):
        channelid = message.content.split(' ',1)[1]
        for member in client.get_channel(channelid).voice_members:
            level = 1
            userdict.update({member.name:level})
            print(member.name)

    elif message.content.startswith('!add'):
        username = message.content.split(' ',1)[1]
        level = 1
        print(username)
        userdict.update({username:level})
        await client.send_message(message.channel, '{} add shuffle users list.'.format(username))
        print(userdict)

    elif message.content.startswith('!flushme'):
        del userdict[message.author.name]
        await client.send_message(message.channel, 'flush {} list data.'.format(message.author.name))
        print(userdict)

    elif message.content.startswith('!flushall'):
        userdict.clear()
        await client.send_message(message.channel, "flush all user list data.")
        print(userdict)

    elif message.content.startswith('!flush'):
        username = message.content.split(' ',1)[1]
        del userdict[message.author.name]
        await client.send_message(message.channel, 'flush {} list data.'.format(message.author.name))
        print(userdict)

    elif message.content.startswith('!map'):
         await client.send_message(message.channel, random.choice(map))

    elif message.content.startswith('!show'):
        await client.send_message(message.channel, "Total User :" + str(len(userdict)))
        await client.send_message(message.channel, userdict)
        print(userdict)

    elif message.content.startswith('!testpro'):
        userdict.update({"luna":1,"Uroro":1,"kiritan":1,"Qoo":1,"Testudines":1,"homuman":1})
        print(userdict)

    elif message.content.startswith('!testdata'): 
        userdict.update({"sukeil":0,"Olympia":0,"dottonandana":0})
        print(userdict)

    elif message.content.startswith('!shuffle'):
        userlist = list(userdict.keys())
        random.shuffle(userlist)
        print(userlist)
        desc = "Map : "
        desc = desc + random.choice(map) + "\n"
        # desc = "Blue Team\t\t\t|\t\t\t Orange Team\n"
        
        userlen = len(userlist)
        for i in range(userlen):
            if(i == 0):
                desc += "```Blue Team : "
            elif(i == math.floor(userlen/2)):
                desc += "\nOrange Team : "
            desc += userlist[i] + ", "

        else:
            desc += "```"

        await client.send_message(message.channel, desc)

    elif message.content.startswith('!yo'):
        await client.send_message(message.channel, 'yo')

    elif message.content.startswith('!help'):
        desc = "!addme\t-> add list \n!flush\t\t-> delete list \n!flushall\t-> delete all user\n!map\t-> choice map\n!shuffle\t-> shuffle list and display result \n!showlist\t-> show user list \n\n Debug Commands\n!testdata\t-> insert test data to list"
        em = discord.Embed(title='Shuffler Help Command List', type="rich",description=desc, colour=0xDEADBF)
        em.set_author(name='Someone', icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
     
    elif message.content.startswith('!test'):
        print(message.content.split(' ',1))
        messagesplit = message.content.split(' ',1)
        commasplit = messagesplit[1]
        addlist = commasplit.split(',')
        random.shuffle(addlist)
        print("list : ",addlist)

        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, addlist)

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(API_Key)