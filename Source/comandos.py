import asyncio
from turtle import color
from unicodedata import name
from discord import VoiceChannel
import nextcord
from nextcord.ext import commands
import time

########## PREFIJO Y DESCRIPCION
bot=commands.Bot(command_prefix='!d ', description="Bot creado por Diego Libonati")


############ Comando PING
@bot.command() # Decorador que permite crear un comando pero con una funcion

async def ping(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    await ctx.send('Estoy funcionado!')

############### Comando Informacion
@bot.command(aliases=['info'])

async def informacion(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)
        member=ctx.author
    embed=nextcord.Embed(title="Informacion del Server", url="https://www.instagram.com/fulbitofcf7/", description="Server OFICIAL de FULBITO FC perteneciente a DISCORD", color=255)
    embed.set_author(name=member.display_name, icon_url=member.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/266396314_579112456839960_8990358209085441079_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=0debeb&_nc_ohc=-1XLNJuraqkAX9CgaRP&_nc_ht=scontent.faep27-1.fna&oh=00_AT_H1uS8VZ4lDhNDUQKHWDvAdXxb5UtoB6RbRSsYhau9aw&oe=61FEFB2A")
    #embed.add_field(name="probando", value="probando", inline=False)
    #embed.add_field(name="probando2", value="probando2", inline=True)
    #embed.add_field(name="probando3", value="probando3", inline=True)
    embed.set_footer(text="Informacion requerida por: {}".format(member.display_name))
    await ctx.send(embed=embed)


### Comando 8Ball ###
import random 

@bot.command(aliases=["8ball", "8b"])

async def eightball(ctx, *, pregunta):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    embed=nextcord.Embed(title="Comando 8 BALL", color=0x00ff00)

    respuestas=["Que se yo rey.",
			"Tu hermana por las dudas.",
			"Si, totalmente",
			"No",
			"La respuesta esta en tu corazon",
			"Quizas"]

    #hola=await ctx.send(f':8ball: La pregunta fue: {pregunta}\n:8ball: La respuesta es: {random.choice(respuestas)}')

    embed.add_field(name="Pregunta y Respuesta", value=f':8ball: La pregunta fue: {pregunta}\n:8ball: La respuesta es: {random.choice(respuestas)}', inline=False)
    await ctx.send(embed=embed)


### Comando Peliculas ###
@bot.command()
async def pelicula(ctx, peli, horario, productor, actores):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    member=ctx.author
    embed=nextcord.Embed(title="Pelicula del Dia", description="Cine Fulbito, presenta: {}".format(peli), color=0x00ff00)
    embed.add_field(name="Horario de Inicio de la Pelicula: ", value=horario + "HS", inline=False)
    embed.add_field(name="Productor: ", value=productor, inline=True)
    embed.add_field(name="Actores principales: ", value=actores, inline=True)
    embed.set_footer(text="Informacion proporcionada por {}".format(member.display_name))
    await ctx.send(embed=embed)


### Comando Latencia ###

@bot.command(aliases=["Latencia"])
async def latencia(ctx, *args):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    inicio=time.time()
    mensaje= await ctx.send("Obteniendo Ping")
    await mensaje.edit(content="Obteniendo Ping.")
    await mensaje.edit(content="Obteniendo Ping..")
    await mensaje.edit(content="Obteniendo Ping...")
    await mensaje.edit(content="¡PING OBTENIDO CON EXITO!")
    fin=time.time()

    embed=nextcord.Embed(title="Comando LATENCIA", description="Este COMANDO obtiene la latencia actual del WebSocket y API de Die BOT", color=16705372)
    embed.add_field(name="LATENCIA WEBSOCKET", value=f"{round(bot.latency*1000)} MS", inline=True)
    embed.add_field(name="LATENCIA API", value=f"{round((fin-inicio)*100)} MS", inline=True)
    embed.set_footer(text=f"Informacion requerida por {ctx.author.display_name}")

    await ctx.send(embed=embed)
    #await ctx.send(f"Mi PING de WebSocket es de: {round(bot.latency*1000)} MS\nMi PING de API es de: {round((fin-inicio)*1000)} MS")

### Comando para mover ###
@bot.command()
async def mover(ctx, member:nextcord.Member, canal:VoiceChannel,*, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.move_to(canal, reason=reason)
    embed=nextcord.Embed(title="COMANDO MOVER", description="Este comando permite mover personas a otros canales, se necesita permisos", color=16705372)
    embed.add_field(name=f"El usuario: {ctx.author.display_name}", value=f"Movio a **{member}**", inline=False)
    embed.add_field(name=f"Al canal {canal}", value=f"Razon: **{reason}**", inline=False)
    await ctx.send(embed=embed)
    # await ctx.send(f"El usuario **{member.display_name}** movio a **{member}** al canal **{canal}** cuya razon es: **{reason}**")

### Comando para agregar roles ###

@bot.command()

async def rol(ctx, member:nextcord.Member, roles:nextcord.Role, reason=None, atomic=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.add_roles(roles, reason=reason)
    embed=nextcord.Embed(title="Comando AGREGAR ROL", description=f"Este comando sirve para dar ROLES, se necesitan permisos\n\n El usuario **{ctx.author.display_name}**, dio el rol: **{roles}** a **{member}**.\nRazon: **{reason}**", color=16705372)
    embed.set_footer(text=f"Comando ejecutado por: {ctx.author.display_name}")
    await ctx.send(embed=embed)

### Comando para sacar roles ###

@bot.command()

async def sacarrol(ctx, member:nextcord.Member, roles:nextcord.Role, reason=None, atomic=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.remove_roles(roles, reason=reason)
    embed=nextcord.Embed(title="Comando SACAR ROL", description=f"Este comando sirve para sacar ROLES, se necesitan permisos\n\n El usuario **{ctx.author.display_name}**, le saco el rol: **{roles}** a **{member}**.\nRazon: **{reason}**", color=16705372)
    embed.set_footer(text=f"Comando ejecutado por: {ctx.author.display_name}")
    await ctx.send(embed=embed)
