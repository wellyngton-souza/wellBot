import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = discord.Client(intents=intents)

i = 0

@bot.event
async def on_ready():
    print(f'Bot está pronto. Conectado como {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    global i
    i += 1
  
    await message.channel.send(f'Mensagens no chat: {i}')

bot.run("Token")