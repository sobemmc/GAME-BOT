from discord.ext import commands
import discord
import asyncio
import random
import os


bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('logged in as \nname: {}\n  id: {}'.format(bot.user.name, bot.user.id))
    print('='*80)

    await bot.change_presence(game=discord.Game(name='$팀짜기 [한 팀당 사람 수]', type=1))

@bot.command(pass_context=True)
async def 팀짜기(ctx, count):
    voice_channel = ctx.message.author.voice.voice_channel

    members = voice_channel.voice_members
    member_names = []
    for member in members:
        member_names.append(member.mention)
    random.shuffle(member_names) #DevSkim: ignore DS148264 until 2021-07-05 

    team = []

    for i in range(0, int(len(member_names)/int(count))):
        temp = []
        for c in range(0, int(count)):
            temp.append(member_names.pop())
        team.append(temp)

    if member_names:
        team.append(member_names)

    for index in range(0, len(team)):
        await bot.say('{} team : {}'.format(index+1, team[index]))


bot.run(os.environ['token'])