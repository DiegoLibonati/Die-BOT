import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
from comandos import bot

# Evento

# Cuando pasa algo. Cuando se conecta el Bot, ya que no lo se.

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name='Instagram: @die_libonati'))
    print('EL BOT ARRANCO.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        embed=nextcord.Embed(title="ERROR :cry:", description="Lo lamento, usted no tiene permisos en este Servidor para ejecutar ese **COMANDO**")
        await ctx.send(embed=embed)
        #await ctx.send("Usted no tiene Permiso para ejecutar este comando")
    else:
        raise error



    
