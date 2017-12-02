import discord
import asyncio
import random
import re

client = discord.Client()
userdict = {}

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


@client.event
async def on_message(message):
    global userdict
    print("message : ",message.content)
    if message.content.startswith('!addme'):
        messagesplit = message.content.split(' ',1)
        username = message.author.name
        level = 0
        if messagesplit[1] == 'pro':
          level = 1
          userdict.update({username:level})
          await client.send_message(message.channel, '{} add shuffle users list.'.format(message.author.name))
        else:
          await client.send_message(message.channel, '\'!addme\' or \'!addme pro\' only can use.')
        print(userdict)

    elif message.content.startswith('!flushme'):
        del userdict[message.author.name]
        await client.send_message(message.channel, 'flush {} list data.'.format(message.author.name))
        print(userdict)

    elif message.content.startswith('!flushall'):
        userdict.clear()
        await client.send_message(message.channel, "flush all user list data.")
        print(userdict)

    elif message.content.startswith('!showlist'):
        await client.send_message(message.channel, userdict)
        print(userdict)

    elif message.content.startswith('!testpro'):
        userdict.update({"luna":1,"Uroro":1,"kiritan":1,"Qoo":1,"eigo":1,"homuman":1})
        print(userdict)

    elif message.content.startswith('!testdata'): 
        userdict.update({"sukeil":0,"Olympia":0,"dottonandana":0})
        print(userdict)

    elif message.content.startswith('!shuffle'):
        userlist = list(userdict.keys())
        random.shuffle(userlist)
        print(userlist)
        desc = ""
        if len(userlist) % 2 == 0:
          for x in range(0,len(userlist),2):
            desc = desc + str(userlist[x])
            desc = desc + "\t\t\t\t\t"
            desc = desc + "|\t"
            desc = desc + userlist[x+1] + "\n"
            
          em = discord.Embed(title='Team Death Match Custom Game Shuffle Result', type="rich",description=desc, colour=0xDEADBF)
          em.set_author(name='Someone', icon_url=client.user.default_avatar_url)
          await client.send_message(message.channel, embed=em)

        else:
          for x in range(0,len(userlist),2):
            desc = desc + str(userlist[x])
            desc = desc + "\t\t\t\t\t"
            desc = desc + "|\t"
            if(x != len(userlist)-1):
              desc = desc + userlist[x+1] + "\n"
            else:
              desc = desc + ""
            
          em = discord.Embed(title='Team Death Match Custom Game Shuffle Result', type="rich",description=desc, colour=0xDEADBF)
          em.set_author(name='Someone', icon_url=client.user.default_avatar_url)
          await client.send_message(message.channel, embed=em)

    elif message.content.startswith('!yo'):
        await client.send_message(message.channel, 'yo')

    elif message.content.startswith('!help'):
        desc = "!addme\t-> add list \n!flush\t\t-> delete list \n!flushall\t-> delete all user\n!shuffle\t-> shuffle list and display result \n!showlist\t-> show user list \n\n Debug Commands\n!testdata\t-> insert test data to list"
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


client.run('API_Key')