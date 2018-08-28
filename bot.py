import discord
import asyncio
import os
import sys
import time
import logging
from watchgod import awatch
path = "e:/SteamLibrary/steamapps/common/Stardew Valley/Mods/Always On Server/"
filename = "InviteCode.txt"
client = discord.Client()      

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    async for changes in awatch(path):
        inviteCodeFile = open(path+filename,'r')
        await client.send_message(discord.Object(id="483765411490431007"), "Current Invite Code: " + inviteCodeFile.read())


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!hi'):
        await client.send_message(message.channel, 'Hi there, ${message.author}')

client.run('token')