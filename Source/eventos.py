import nextcord
from nextcord.ext import commands
from comandos import bot

# Evento

# Cuando pasa algo. Cuando se conecta el Bot, ya que no lo se.

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name='Instagram: @die_libonati'))
    print('EL BOT ARRANCO.')



    
