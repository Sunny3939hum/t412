import discord
import openai

dc_token="MTA5NTUyOTQ2MjM0MDI1OTk1MA.GZPaLc.U_tWiH_f7YY0atZuIZAJ2QpQsvkxQ44GWQc94A"

intents = discord.Intents.default()
intents.message_content=True
client = discord.Client(intents=intents)


messages = [{"role":"system","content":"You are a helpful assistant"}]
openai.api_key ="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"
@client.event
async def on_ready():
    print("bot is on")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user_input = message.content
    messages.append({"role":"user","content":user_input})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    chat_response=completion.choices[0].message.content
    await message.channel.send(chat_response)

client.run(dc_token)