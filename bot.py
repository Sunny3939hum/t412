import discord
import openai

dc_token="MTA5NTUyOTQ2MjM0MDI1OTk1MA.GZPaLc.U_tWiH_f7YY0atZuIZAJ2QpQsvkxQ44GWQc94A"

intents = discord.Intents.default()
intents.message_content=True
client = discord.Client(intents=intents)


message = [{"role":"system","content":"You are a helpful assistant"}]

@client.event
async def on_ready():
    print("bot is on")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await message.channel.send(message.content)

client.run(dc_token)