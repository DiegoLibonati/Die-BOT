import asyncio
from turtle import color
from unicodedata import name
from discord import Permissions, VoiceChannel
import nextcord
from nextcord.ext import commands
import time
from nextcord.ext.commands import has_guild_permissions, MissingPermissions
import random 
import CHelp
from CHelp import Misc_Commands



########## PREFIJO Y DESCRIPCION
bot=commands.Bot(command_prefix='!d ', description="Bot creado por Diego Libonati")

### Eventos ###

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


@bot.event
async def on_message(message):
    msg= message.content

    if msg.startswith("!d help"):
        #await message.author.send(*CHelp.Comandos)

        embed=nextcord.Embed(title="HELP COMMAND", description="Hi, I´m Die-BOT. The help arrived")
        embed.add_field(name="MISC COMMANDS", value=", ".join(CHelp.Misc_Commands), inline=False)
        embed.add_field(name="FUN COMMANDS", value=", ".join(CHelp.Fun_Commands), inline=False)
        embed.add_field(name="MOD COMMANDS - [SE NECESITAN PERMISOS]", value=", ".join(CHelp.Mod_Commands), inline=False)
        await message.author.send(embed=embed)
        
        embed2=nextcord.Embed(title="HELP COMMAND", description=f"Hola **{message.author.display_name}**, te envie un mensaje privado!")
        await message.channel.send(embed=embed2)
        






### COMANDOS MISC ###
### Comando Ping ###
@bot.command() # Decorador que permite crear un comando pero con una funcion
async def ping(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    await ctx.send('Estoy funcionado!')

### Comando InformacionServer ###
@bot.command(aliases=['info', "informacion", "Info", "Informacion", "Information"])
async def information(ctx):
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

### Comando Latencia ###
@bot.command(aliases=["Latencia", "latencia", "Latency"])
async def latency(ctx, *args):
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


### COMANDOS FUN ###
### Comando 8Ball ###

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

### Comando Piedra Papel o Tijera ###
@bot.command(aliases=[])
async def game1(ctx, usuario):

    lista=["piedra", "papel", "tijera"]

    if usuario not in lista:
        embed=nextcord.Embed(title="ROCK, PAPER OR SCISSORS GAME", description="Comando que sirve para jugar a piedra, papel o tijera contra la computadora")
        embed.add_field(name="ERROR :cry:", value="La palabra o caracteres que introdujo son incorrectos.\nSolo se permite: piedra, papel o tijera.\nIngrese el comando con su correcta expresion nuevamente.")
        await ctx.send(embed=embed)
        #await ctx.send("La palabra o caracteres que introdujo son incorrectos")
        #await ctx.send("Solo se permite: piedra, papel o tijera")
        #await ctx.send("Ingrese el comando con su correcta expresion nuevamente")
    else:
        IA=random.choice(lista)

        resultado=nextcord.Embed(title="ROCK, PAPER OR SCISSORS GAME", description="Comando que sirve para jugar a piedra, papel o tijera contra la computadora")
        resultado.add_field(name="ELECCIONES", value=f"Vos elegiste: **{usuario}**\nLa computadora eligio: **{IA}**", inline=False)

        #await ctx.send(f"Vos elegiste: {usuario}\nLa computadora eligio: {IA}")

        ### PAPEL
        if IA=="papel" and usuario=="piedra":
            #await ctx.send("La computadora gana")
            resultado.add_field(name="RESULTADO FINAL", value="**La computadora GANA**", inline=False)
        elif IA=="papel" and usuario=="tijera":
            #await ctx.send("GANASTE")
            resultado.add_field(name="RESULTADO FINAL", value="**GANASTE**",inline=False)
        elif IA=="papel" and usuario=="papel":
            #await ctx.send("Es un EMPATE")
            resultado.add_field(name="RESULTADO FINAL", value="**Es un EMPATE**",inline=False)

        ### TIJERA
        if IA=="tijera" and usuario=="piedra":
            #await ctx.send("GANASTE")
            resultado.add_field(name="RESULTADO FINAL", value="**GANASTE**",inline=False)
        elif IA=="tijera" and usuario=="tijera":
            #await ctx.send("Es un EMPATE")
            resultado.add_field(name="RESULTADO FINAL", value="**Es un EMPATE**",inline=False)
        elif IA=="tijera" and usuario=="papel":
            #await ctx.send("La computadora gana")
            resultado.add_field(name="RESULTADO FINAL", value="**La computadora GANA**",inline=False)

        ### PIEDRA
        if IA=="piedra" and usuario=="piedra":
            #await ctx.send("Es un EMPATE")
            resultado.add_field(name="RESULTADO FINAL", value="**Es un EMPATE**",inline=False)
        elif IA=="piedra" and usuario=="tijera":
            #await ctx.send("La computadora gana")
            resultado.add_field(name="RESULTADO FINAL", value="**La computadora GANA**",inline=False)
        elif IA=="piedra" and usuario=="papel":
            #await ctx.send("GANASTE")
            resultado.add_field(name="RESULTADO FINAL", value="**GANASTE**",inline=False)

        
        await ctx.send(embed=resultado)


### Comando Peliculas ###
@bot.command(aliases=["pelicula", "Pelicula", "Movie"])
async def movie(ctx, peli, horario, productor, actores):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    member=ctx.author
    embed=nextcord.Embed(title="Pelicula del Dia", description="Cine Fulbito, presenta: {}".format(peli), color=0x00ff00)
    embed.add_field(name="Horario de Inicio de la Pelicula: ", value=horario + "HS", inline=False)
    embed.add_field(name="Productor: ", value=productor, inline=True)
    embed.add_field(name="Actores principales: ", value=actores, inline=True)
    embed.set_footer(text="Informacion proporcionada por {}".format(member.display_name))
    await ctx.send(embed=embed)


### COMANDOS MOD ###
### Comando para mover ###
@bot.command(aliases=["Mover", "mover", "Move"])
@has_guild_permissions(move_members=True)
async def move(ctx, member:nextcord.Member, canal:VoiceChannel,*, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
        await member.move_to(canal, reason=reason)
        embed=nextcord.Embed(title="COMANDO MOVER", description="Este comando permite mover personas a otros canales, se necesita permisos", color=16705372)
        embed.add_field(name=f"El usuario: {ctx.author.display_name}", value=f"Movio a **{member}**", inline=False)
        embed.add_field(name=f"Al canal {canal}", value=f"Razon: **{reason}**", inline=False)
        await ctx.send(embed=embed)
# await ctx.send(f"El usuario **{member.display_name}** movio a **{member}** al canal **{canal}** cuya razon es: **{reason}**")

### Comando para agregar roles ###
@bot.command(aliases=["Rol"])
@has_guild_permissions(manage_roles=True)
async def rol(ctx, member:nextcord.Member, roles:nextcord.Role, reason=None, atomic=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.add_roles(roles, reason=reason)
    embed=nextcord.Embed(title="Comando AGREGAR ROL", description=f"Este comando sirve para dar ROLES, se necesitan permisos\n\n El usuario **{ctx.author.display_name}**, dio el rol: **{roles}** a **{member}**.\nRazon: **{reason}**", color=16705372)
    embed.set_footer(text=f"Comando ejecutado por: {ctx.author.display_name}")
    await ctx.send(embed=embed)

### Comando para sacar roles ###
@bot.command(aliases=["Drol", "DROL"])
@has_guild_permissions(manage_roles=True)
async def drol(ctx, member:nextcord.Member, roles:nextcord.Role, reason=None, atomic=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.remove_roles(roles, reason=reason)
    embed=nextcord.Embed(title="Comando SACAR ROL", description=f"Este comando sirve para sacar ROLES, se necesitan permisos\n\n El usuario **{ctx.author.display_name}**, le saco el rol: **{roles}** a **{member}**.\nRazon: **{reason}**", color=16705372)
    embed.set_footer(text=f"Comando ejecutado por: {ctx.author.display_name}")
    await ctx.send(embed=embed)

### Comando para Mutear ###
@bot.command(aliases=["Silence", "SILENCE"])
@has_guild_permissions(mute_members=True)
async def silence(ctx, member:nextcord.Member, mute=False):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(mute=True)
    embed=nextcord.Embed(title="Comando SILENCE", description=f"El usuario **{member}** fue silenciado por **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejecutador por {ctx.author.display_name}")
    await ctx.send(embed=embed)
    # await ctx.send(f"El usuario {member} fue silenciado por {ctx.author.display_name}")

### Comando para Desmutear ###
@bot.command(aliases=["Desilence", "DESILENCE"])
@has_guild_permissions(mute_members=True)
async def desilence(ctx, member:nextcord.Member, mute=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(mute=False)
    embed=nextcord.Embed(title="Comando DESILENCE", description=f"El usuario **{member}** fue dessilenciado por **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejecutador por {ctx.author.display_name}")
    await ctx.send(embed=embed)
    #await ctx.send(f"El usuario {member} fue dessilenciado por {ctx.author.display_name}")

### Comando para ensordecer ###
@bot.command(aliases=["Deafen", "DEAFEN"])
@has_guild_permissions(deafen_members=True)
async def deafen(ctx, member:nextcord.Member, deafen=False):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(deafen=True)
    embed=nextcord.Embed(title="Command DEAFEN", description=f"El usuario **{member}** fue ensordecido por **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejecutado por: {ctx.author.display_name}")
    await ctx.send(embed=embed)

### Comando para desendordeser ###
@bot.command(aliases=["DEDEAFEN", "Dedeafen"])
@has_guild_permissions(deafen_members=True)
async def dedeafen(ctx, member:nextcord.Member, deafen=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(deafen=False)
    embed=nextcord.Embed(title="Command DEDEAFEN", description=f"El usuario **{member}** ahora escucha gracias a: **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejecutado por: {ctx.author.display_name}")
    await ctx.send(embed=embed)

### Comando para ensordecer y silenciar ###
@bot.command(aliases=["SDALL", "Sdall"])
@has_guild_permissions(mute_members=True)
@has_guild_permissions(deafen_members=True)
async def sdall(ctx, member:nextcord.Member, mute=False, deafen=False):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(mute=True, deafen=True)
    embed=nextcord.Embed(title="Command SDALL", description=f"El usuario **{member}** fue silenciado y ensordecido por **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejecutado por {ctx.author.display_name}")
    await ctx.send(embed=embed)

### Comando para que escuchen y hablen ###
@bot.command(aliases=["SDUNALL", "Sdunall"])
@has_guild_permissions(mute_members=True)
@has_guild_permissions(deafen_members=True)
async def sdunall(ctx, member:nextcord.Member, mute=True, deafen=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(mute=False, deafen=False)
    embed=nextcord.Embed(title="Command SDUNALL", description=f"El usuario **{member}** fue dessilenciado y tambien ahora escucha gracias a **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejecutado por {ctx.author.display_name}")
    await ctx.send(embed=embed)

### Comando para desconectar ###
@bot.command(aliases=["Disconnect", "DISCONNECT"])
@has_guild_permissions(move_members=True)
async def disconnect(ctx, member:nextcord.Member, voice_channel=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(voice_channel=None)
    embed=nextcord.Embed(title="Command DISCONNECT", description=f"El usuario {member}, fue desconectado por: {ctx.author.display_name}")
    embed.set_footer(text=f"Comando ejecutado por {ctx.author.display_name}")
    await ctx.send(embed=embed)
    
### Comando para banear ###

@bot.command(aliases=["BAN", "Ban"])
@has_guild_permissions(ban_members=True)
async def ban(ctx, member:nextcord.Member, delete_message_days=None, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.ban(delete_message_days=delete_message_days, reason=reason)
    embed=nextcord.Embed(title="BAN Command", description=f"El usuario **{member}** fue baneado por **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejecutado por **{ctx.author.display_name}**")
    await ctx.send(embed=embed)

### Comando para desbanear ###

@bot.command(aliases=["UNBAN", "Unban"])
@has_guild_permissions(ban_members=True)
async def unban(ctx, member:nextcord.Member, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.ban(reason=reason)
    embed=nextcord.Embed(title="UNBAN Command", description=f"El usuario **{member}** fue desbaneado por **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejecutado por **{ctx.author.display_name}**")
    await ctx.send(embed=embed)

### Comando para kickear ###
@bot.command(aliases=["Kick", "KICK"])
@has_guild_permissions(kick_members=True)
async def kick(ctx, member:nextcord.Member, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.kick(reason=reason)
    embed=nextcord.Embed(title="KICK Command", description=f"El usuario **{member}**, fue kickeado por **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejectuado por {ctx.author.display_name}")
    await ctx.send(embed=embed)

### Comando para tener Prioridad de habla ### 
@bot.command(aliases=["PTOSPEAK","Ptospeak"])
@has_guild_permissions(priority_speaker=True)
async def ptospeak(ctx, member:nextcord.Member):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.request_to_speak()
    embed=nextcord.Embed(title="REQUEST TO SPEAK Command", description=f"El usuario **{member}** ahora tiene PRIORIDAD PARA HABLAR gracias a **{ctx.author.display_name}**")
    embed.set_footer(text=f"Comando ejecutado por {ctx.author.display_name}")
    ctx.send(embed=embed)

### RUN ###
bot.run('OTM4MjA5MjMzMDAwODgyMTg2.Yfm9cA.XrAO5_4EUMOh3eKf9VfyXifxMtI')