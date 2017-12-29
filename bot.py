#RustyBot by DrawFast

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

#Start message
@bot.event
async def on_ready():
    print ("Started")
#Commands
@bot.command(pass_context=True)
async def wipe(ctx):
    embed    = discord.Embed(title="Wipe info", description="Servers wipe every Thursday at the listed times", color=0x00ff00)
    embed.add_field(name="EST", value="5pm", inline=True)
    embed.add_field(name="CEST", value="11pm", inline=True)
    await bot.say(embed=embed)
    print ("Wipe working")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what i could find.", color=0x00ff00)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role, inline=True)
    embed.add_field(name="Joined",value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    print ("Info working")
    
#Token
bot.run("Mzk2MDE5ODc3NDY4NTY5NjI0.DScj7A.HY69URiQMkcuwJ8l9FAaauEfRcw")
