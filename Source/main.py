import asyncio
from turtle import color
from unicodedata import name
from discord import Colour, Permissions, VoiceChannel
import nextcord
from nextcord.ext import commands
import time
from nextcord.ext.commands import has_guild_permissions, MissingPermissions
import random 
import CHelp



intents=nextcord.Intents.default()
intents.members= True



########## PREFIJO Y DESCRIPCION
bot=commands.Bot(command_prefix='!d ', description="Bot created by Diego Libonati", intents=intents)

### Eventos ###

# Cuando pasa algo. Cuando se conecta el Bot, ya que no lo se.

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name='Instagram: @die_libonati'))
    print('EL BOT ARRANCO.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        embed=nextcord.Embed(title="ERROR :cry:", description="You dont have permission to use this **COMMAND**", color=0xe74c3c)
        await ctx.send(embed=embed)
        #await ctx.send("Usted no tiene Permiso para ejecutar este comando")
    else:
        raise error


@bot.event
async def on_message(message):

    msg= message.content

    if msg=="!d help":
        #await message.author.send(*CHelp.Comandos)

        embed=nextcord.Embed(title="HELP COMMAND :gear:", description="Hi, I´m Die-BOT. The help arrived", color=0xe74c3c, url="https://www.instagram.com/die_libonati/?hl=es-la")
        embed.add_field(name="GENERAL COMMANDS", value=", ".join(CHelp.General_Commands), inline=False)
        embed.add_field(name="FUN COMMANDS", value=", ".join(CHelp.Fun_Commands), inline=False)
        embed.add_field(name="MOD COMMANDS - [YOU NEED PERMISSION]", value=", ".join(CHelp.Mod_Commands), inline=False)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_image(url="https://images.pagina12.com.ar/styles/focal_3_2_960x640/public/media/articles/22887/eghudclxuaeddx5.jpg?itok=veQ6beNk")
        await message.author.send(embed=embed)

        embed3=nextcord.Embed(title="Contact :desktop:", description="**IMPORTANT INFORMATION**", color=0xe74c3c, url="https://www.instagram.com/die_libonati/?hl=es-la")
        embed3.add_field(name=". :flag_ar:", value=", ".join(CHelp.Contact), inline=False)
        await message.author.send(embed=embed3)
        
        embed2=nextcord.Embed(title="[Die-BOT] HELP :boomerang:", description=f"Hi **{message.author.display_name}**, i have sent you a private message! :gear:", color=0xe74c3c)
        await message.channel.send(embed=embed2)
    
    else:

        await bot.process_commands(message)


### COMANDOS Generales ###
### Comando Ping ###
@bot.command() # Decorador que permite crear un comando pero con una funcion
async def ping(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    await ctx.send('I am working :robot:!')

### Comando InformacionServer ###
@bot.command(aliases=['info', "informacion", "Info", "Informacion", "Information"])
async def information(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)
        member=ctx.author
    embed=nextcord.Embed(title="[Die-BOT] Server information :gear:", url="https://www.instagram.com/die_libonati/?hl=es-la", description="Fulbito FC official SERVER by Discord", color=0xe74c3c)
    embed.add_field(name="Server created by ",value=f"{ctx.guild.owner}", inline=False)
    embed.add_field(name="Server created date ", value=f"{ctx.guild.created_at}", inline=False)
    embed.add_field(name="Server member count", value=f"{ctx.guild.member_count}", inline=False)
    embed.set_author(name=member.display_name, icon_url=member.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_image(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/266396314_579112456839960_8990358209085441079_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=0debeb&_nc_eui2=AeHeAU6xna0PC5ub_el7KLKk2V4RbXd6khrZXhFtd3qSGmAeypzo65PZkcti0aKTFhNWfwFpO8MYJfpnhdB0PgVv&_nc_ohc=dFedUnuLRkAAX9HO4ke&_nc_ht=scontent.faep27-1.fna&oh=00_AT_gcMS7zGrsc1nOdyipm3dM692pEFxCIepq84prRR0VNQ&oe=6214BBEA")
    embed.set_footer(text="Command executed by: {}".format(member.display_name))
    await ctx.send(embed=embed)

### Comando Latencia ###
@bot.command(aliases=["Latencia", "latencia", "LATENCY", "Latency"])
async def latency(ctx, *args):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    inicio=time.time()
    mensaje= await ctx.send("Obtaining Ping")
    await mensaje.edit(content="Obtaining Ping.")
    await mensaje.edit(content="Obtaining Ping..")
    await mensaje.edit(content="Obtaining Ping...")
    await mensaje.edit(content="¡Successful achievement of Ping!")
    fin=time.time()

    embed=nextcord.Embed(title="[Die-BOT] LATENCY :gear:", description="This COMMAND gets the actual latency from WebSocket and Die-BOT's API.", color=0xe74c3c)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.add_field(name="LATENCY WEBSOCKET", value=f"{round(bot.latency*1000)} MS", inline=True)
    embed.add_field(name="LATENCY API", value=f"{round((fin-inicio)*100)} MS", inline=True)
    embed.set_footer(text=f"Command executed by: {ctx.author.display_name}")

    await ctx.send(embed=embed)
#await ctx.send(f"Mi PING de WebSocket es de: {round(bot.latency*1000)} MS\nMi PING de API es de: {round((fin-inicio)*1000)} MS")

### Comando About ###
@bot.command(aliases=["ABOUT", "About", "acerca", "Acerca"])
async def about(ctx):
    embed=nextcord.Embed(title="[Die-BOT] About this BOT :gear:", description="Hi, i´m Libonati Diego", color=0xe74c3c)
    embed.add_field(name="Information", value="This bot was created by Libonati Diego. I am from Argentina and i used Python to build this BOT.\n\
    If you need help, type **!d help** and help will arrive to your private messages. Soon you can donate to support this bot.\n\
    **My instagram:** https://www.instagram.com/die_libonati\n\
    **My GitHub:** https://github.com/DiegoLibonati")
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text=f"Command executed by: {ctx.author.display_name}")
    embed.set_image(url="https://images.pagina12.com.ar/styles/focal_3_2_960x640/public/media/articles/22887/eghudclxuaeddx5.jpg?itok=veQ6beNk")
    await ctx.send(embed=embed)

### Comando Avatar ###
@bot.command(aliases=["Avatar", "AVATAR"])
async def avatar(ctx, user:nextcord.User):
    embed=nextcord.Embed(title="[Die-BOT] AVATAR :gear:", color=0xe74c3c)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_image(url=user.avatar)
    embed.set_footer(text=f"Command executed by: {ctx.author.display_name}")
    await ctx.send(embed=embed)

### Comando User-Info ###

@bot.command(aliases=["Userinfo", "USERINFO"])
async def userinfo(ctx, user:nextcord.User):

    embed=nextcord.Embed(title="[Die-BOT] USER INFORMATION :gear:", color=0xe74c3c)
    embed.add_field(name="User created at", value=user.created_at, inline=False)
    embed.add_field(name="User name", value=user.name, inline=False)
    embed.add_field(name="User ID", value=user.id, inline=False)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_image(url=user.avatar)
    embed.set_footer(text=f"Command executed by: {ctx.author.display_name}")
    await ctx.send(embed=embed)


### COMANDOS FUN ###
### Comando 8Ball ###

@bot.command(aliases=["8ball", "8b"])
async def eightball(ctx, *, pregunta):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    embed=nextcord.Embed(title="[Die-BOT] 8BALL :video_game:", color=0x00ff00)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")

    respuestas=["Que se yo rey.",
			"Tu hermana por las dudas.",
			"Si, totalmente",
			"No",
			"La respuesta esta en tu corazon",
			"Quizas"]

    #hola=await ctx.send(f':8ball: La pregunta fue: {pregunta}\n:8ball: La respuesta es: {random.choice(respuestas)}')

    embed.add_field(name="Question and Answer", value=f':8ball: The question was: {pregunta}\n:8ball: The answer is: {random.choice(respuestas)}', inline=False)
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando rock paper o scissors ###
@bot.command(aliases=["GAME1", "Game1"])
async def game1(ctx, usuario):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    lista=["rock", "paper", "scissors"]

    if usuario not in lista:
        embed=nextcord.Embed(title="[Die-BOT] ROCK, PAPER OR SCISSORS GAME :video_game:", description="Rock, paper, scissors VS IA Command", color=0x00ff00)
        embed.add_field(name="ERROR :cry:", value="The word or letter entered is incorrect.\nOnly allows: rock, paper, scissors.\nRe-enter the command with the correct word.")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
        #await ctx.send("La palabra o caracteres que introdujo son incorrectos")
        #await ctx.send("Solo se permite: rock, paper o scissors")
        #await ctx.send("Ingrese el comando con su correcta expresion nuevamente")
    else:
        IA=random.choice(lista)

        resultado=nextcord.Embed(title="[Die-BOT] ROCK, PAPER OR SCISSORS GAME :video_game:", description="Rock, paper, scissors VS IA Command", color=0x00ff00)
        resultado.add_field(name="ELECTIONS", value=f"You choice: **{usuario}**\nThe IA choice: **{IA}**", inline=False)
        resultado.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        resultado.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        resultado.set_footer(text="Command executed by: {}".format(ctx.author.display_name))

        #await ctx.send(f"Vos elegiste: {usuario}\nLa computadora eligio: {IA}")

        ### paper
        if IA=="paper" and usuario=="rock":
            #await ctx.send("The IA WINS")
            resultado.add_field(name="FINAL RESULT", value="**The IA WINS**", inline=False)
        elif IA=="paper" and usuario=="scissors":
            #await ctx.send("You WIN")
            resultado.add_field(name="FINAL RESULT", value="**You WIN**",inline=False)
        elif IA=="paper" and usuario=="paper":
            #await ctx.send("It is a TIE")
            resultado.add_field(name="FINAL RESULT", value="**It is a TIE**",inline=False)

        ### scissors
        if IA=="scissors" and usuario=="rock":
            #await ctx.send("You WIN")
            resultado.add_field(name="FINAL RESULT", value="**You WIN**",inline=False)
        elif IA=="scissors" and usuario=="scissors":
            #await ctx.send("It is a TIE")
            resultado.add_field(name="FINAL RESULT", value="**It is a TIE**",inline=False)
        elif IA=="scissors" and usuario=="paper":
            #await ctx.send("The IA WINS")
            resultado.add_field(name="FINAL RESULT", value="**The IA WINS**",inline=False)

        ### rock
        if IA=="rock" and usuario=="rock":
            #await ctx.send("It is a TIE")
            resultado.add_field(name="FINAL RESULT", value="**It is a TIE**",inline=False)
        elif IA=="rock" and usuario=="scissors":
            #await ctx.send("The IA WINS")
            resultado.add_field(name="FINAL RESULT", value="**The IA WINS**",inline=False)
        elif IA=="rock" and usuario=="paper":
            #await ctx.send("You WIN")
            resultado.add_field(name="FINAL RESULT", value="**You WIN**",inline=False)

        
        await ctx.send(embed=resultado)

### Comando adivina el numero ###
@bot.command(aliases=["Game2", "GAME2"])
async def game2(ctx, min_Num,max_Num, eleccion):

    try:
        num_Oculto_lista=[*range(int(min_Num),int(max_Num),1)]

        num_Oculto=random.choice(num_Oculto_lista)

        int2=int(eleccion)

        if num_Oculto == int2:
            await ctx.send("Congratulations, you guessed it")

        elif int2 < int(min_Num) or int2 > int(max_Num):
            await ctx.send("Your number selection is less than **num_Min** or greater than **num_Max**.")
        
        elif int2 != num_Oculto:

            await ctx.send("You missed, best of luck next time.") 
        
        else:

            await ctx.send("Unexpected ERROR :cry:")

    except ValueError:
        await ctx.send("You can only send integer number")



### Comando Peliculas ###
@bot.command(aliases=["pelicula", "Pelicula", "Movie"])
async def movie(ctx, peli, horario, productor, actores):
    async with ctx.typing():
        await asyncio.sleep(0.5)

    member=ctx.author
    embed=nextcord.Embed(title="Movie of the day", description="Cine Fulbito, presents: **{}**".format(peli), color=0x00ff00)
    embed.add_field(name="Starting time of the movie: ", value=horario + "HS", inline=False)
    embed.add_field(name="Productor: ", value=productor, inline=True)
    embed.add_field(name="Principals actors: ", value=actores, inline=True)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)


### COMANDOS MOD ###
### Comando para mover ###
@bot.command(aliases=["Mover", "mover", "Move"])
@has_guild_permissions(move_members=True)
async def move(ctx, member:nextcord.Member, canal:VoiceChannel,*, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
        await member.move_to(canal, reason=reason)
        embed=nextcord.Embed(title="[Die-BOT] MOVE :man_mechanic:", description="This command allows the mod to move users to another channel", color=0x9b59b6)
        embed.add_field(name=f"The user: {ctx.author.display_name}", value=f"move **{member}**", inline=False)
        embed.add_field(name=f"to channel {canal}", value=f"Reason: **{reason}**", inline=False)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
# await ctx.send(f"El usuario **{member.display_name}** movio a **{member}** al canal **{canal}** cuya razon es: **{reason}**")

### Comando para agregar roles ###
@bot.command(aliases=["Rol"])
@has_guild_permissions(manage_roles=True)
async def rol(ctx, member:nextcord.Member, roles:nextcord.Role, reason=None, atomic=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.add_roles(roles, reason=reason)
    embed=nextcord.Embed(title="[Die-BOT] ADD ROL :man_mechanic:", description=f"This command allows the mod to give role to the users.\n\n The user **{ctx.author.display_name}**, give: **{roles}** to **{member}**.\nReason: **{reason}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando para sacar roles ###
@bot.command(aliases=["Drol", "DROL"])
@has_guild_permissions(manage_roles=True)
async def drol(ctx, member:nextcord.Member, roles:nextcord.Role, reason=None, atomic=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.remove_roles(roles, reason=reason)
    embed=nextcord.Embed(title="[Die-BOT] REMOVE ROL :man_mechanic:", description=f"This command allows the mod to unrole the users.\n\n The user **{ctx.author.display_name}**, take out the role: **{roles}** to **{member}**.\nReason: **{reason}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando para Mutear ###
@bot.command(aliases=["Silence", "SILENCE"])
@has_guild_permissions(mute_members=True)
async def silence(ctx, member:nextcord.Member, mute=False):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(mute=True)
    embed=nextcord.Embed(title="[Die-BOT] SILENCE :man_mechanic:", description=f"The user **{member}** was silence by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
    # await ctx.send(f"El usuario {member} fue silenciado por {ctx.author.display_name}")

### Comando para Desmutear ###
@bot.command(aliases=["Desilence", "DESILENCE"])
@has_guild_permissions(mute_members=True)
async def desilence(ctx, member:nextcord.Member, mute=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(mute=False)
    embed=nextcord.Embed(title="[Die-BOT] DESILENCE :man_mechanic:", description=f"The user **{member}** was unsilence by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
    #await ctx.send(f"El usuario {member} fue dessilenciado por {ctx.author.display_name}")

### Comando para ensordecer ###
@bot.command(aliases=["Deafen", "DEAFEN"])
@has_guild_permissions(deafen_members=True)
async def deafen(ctx, member:nextcord.Member, deafen=False):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(deafen=True)
    embed=nextcord.Embed(title="[Die-BOT] DEAFEN :man_mechanic:", description=f"The user **{member}** was deafen by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando para desendordeser ###
@bot.command(aliases=["DEDEAFEN", "Dedeafen"])
@has_guild_permissions(deafen_members=True)
async def dedeafen(ctx, member:nextcord.Member, deafen=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(deafen=False)
    embed=nextcord.Embed(title="[Die-BOT] DEDEAFEN :man_mechanic:", description=f"The user **{member}** now listen by: **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando para ensordecer y silenciar ###
@bot.command(aliases=["SDALL", "Sdall"])
@has_guild_permissions(mute_members=True)
@has_guild_permissions(deafen_members=True)
async def sdall(ctx, member:nextcord.Member, mute=False, deafen=False):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(mute=True, deafen=True)
    embed=nextcord.Embed(title="[Die-BOT] SDALL :man_mechanic:", description=f"The user **{member}** was silenced and muted by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando para que escuchen y hablen ###
@bot.command(aliases=["SDUNALL", "Sdunall"])
@has_guild_permissions(mute_members=True)
@has_guild_permissions(deafen_members=True)
async def sdunall(ctx, member:nextcord.Member, mute=True, deafen=True):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(mute=False, deafen=False)
    embed=nextcord.Embed(title="[Die-BOT] SDUNALL :man_mechanic:", description=f"The user **{member}** now can talk and listen by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando para desconectar ###
@bot.command(aliases=["Disconnect", "DISCONNECT"])
@has_guild_permissions(move_members=True)
async def disconnect(ctx, member:nextcord.Member, voice_channel=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.edit(voice_channel=None)
    embed=nextcord.Embed(title="[Die-BOT] DISCONNECT :man_mechanic:", description=f"The user **{member}**, was disconnected by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
    
### Comando para banear ###

@bot.command(aliases=["BAN", "Ban"])
@has_guild_permissions(ban_members=True)
async def ban(ctx, member:nextcord.Member, delete_message_days=None, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.ban(delete_message_days=delete_message_days, reason=reason)
    embed=nextcord.Embed(title="[Die-BOT] BAN :man_mechanic:", description=f"The user **{member}** was banned by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando para desbanear ###

@bot.command(aliases=["UNBAN", "Unban"])
@has_guild_permissions(ban_members=True)
async def unban(ctx, member:nextcord.Member, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.ban(reason=reason)
    embed=nextcord.Embed(title="[Die-BOT] UNBAN :man_mechanic:", description=f"The user **{member}** was unbanned by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando para kickear ###
@bot.command(aliases=["Kick", "KICK"])
@has_guild_permissions(kick_members=True)
async def kick(ctx, member:nextcord.Member, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.kick(reason=reason)
    embed=nextcord.Embed(title="[Die-BOT] KICK :man_mechanic:", description=f"The user **{member}**, was kicked by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

### Comando para tener Prioridad de habla ### 
@bot.command(aliases=["PTOSPEAK","Ptospeak"])
@has_guild_permissions(priority_speaker=True)
async def ptospeak(ctx, member:nextcord.Member):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await member.request_to_speak()
    embed=nextcord.Embed(title="[Die-BOT] REQUEST TO SPEAK :man_mechanic:", description=f"The user **{member}** now have request to speak by **{ctx.author.display_name}**", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    ctx.send(embed=embed)

### Comando para borrar mensajes ###
@bot.command(aliases=["CLEAR", "Clear"])
@has_guild_permissions(manage_messages=True, read_message_history=True)
async def clear(ctx, canal:nextcord.TextChannel, limit=None):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await canal.purge(limit=int(limit)+1)

    embed=nextcord.Embed(title="[Die-BOT] CLEAR :man_mechanic:", description=f"**{limit}** messages were deleted from the cannel: **{canal}** successfully", color=0x9b59b6)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)







### RUN ###
bot.run('OTM4MjA5MjMzMDAwODgyMTg2.Yfm9cA.eG0ZpaigSx9r6PvELcwat43EvdU')