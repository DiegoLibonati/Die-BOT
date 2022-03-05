import nextcord
from nextcord.ext import commands
import random 
import asyncio

### COMANDOS FUN ###
### Comando 8Ball ###

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='eightball', description='', help='',  aliases=['8ball', '8b'])
    async def _eightball(self, ctx, *, pregunta):
        async with ctx.typing():
            await asyncio.sleep(0.5)

        embed=nextcord.Embed(title='[Die-BOT] 8BALL :video_game:', color=0x00ff00)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777')

        respuestas=['Que se yo rey.',
                'Tu hermana por las dudas.',
                'Si, totalmente',
                'No',
                'La respuesta esta en tu corazon',
                'Quizas']

        #hola=await ctx.send(f':8ball: La pregunta fue: {pregunta}\n:8ball: La respuesta es: {random.choice(respuestas)}')

        embed.add_field(name='Question and Answer', value=f':8ball: The question was: {pregunta}\n:8ball: The answer is: {random.choice(respuestas)}', inline=False)
        embed.set_footer(text='Command executed by: {}'.format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando rock paper o scissors ###
    @commands.command(name='game1', description='', help='', aliases=['g1'])
    async def _game1(self, ctx, usuario):
        async with ctx.typing():
            await asyncio.sleep(0.5)

        lista=['rock', 'paper', 'scissors']

        if usuario not in lista:
            embed=nextcord.Embed(title='[Die-BOT] ROCK, PAPER OR SCISSORS GAME :video_game:', description='Rock, paper, scissors VS IA Command', color=0x00ff00)
            embed.add_field(name='ERROR :cry:', value='The word or letter entered is incorrect.\nOnly allows: rock, paper, scissors.\nRe-enter the command with the correct word.')
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777')
            embed.set_footer(text='Command executed by: {}'.format(ctx.author.display_name))
            await ctx.send(embed=embed)
            #await ctx.send('La palabra o caracteres que introdujo son incorrectos')
            #await ctx.send('Solo se permite: rock, paper o scissors')
            #await ctx.send('Ingrese el comando con su correcta expresion nuevamente')
        else:
            IA=random.choice(lista)

            resultado=nextcord.Embed(title='[Die-BOT] ROCK, PAPER OR SCISSORS GAME :video_game:', description='Rock, paper, scissors VS IA Command', color=0x00ff00)
            resultado.add_field(name='ELECTIONS', value=f'You choice: **{usuario}**\nThe IA choice: **{IA}**', inline=False)
            resultado.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            resultado.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777')
            resultado.set_footer(text='Command executed by: {}'.format(ctx.author.display_name))

            #await ctx.send(f'Vos elegiste: {usuario}\nLa computadora eligio: {IA}')

            ### paper
            if IA=='paper' and usuario=='rock':
                #await ctx.send('The IA WINS')
                resultado.add_field(name='FINAL RESULT', value='**The IA WINS**', inline=False)
            elif IA=='paper' and usuario=='scissors':
                #await ctx.send('You WIN')
                resultado.add_field(name='FINAL RESULT', value='**You WIN**',inline=False)
            elif IA=='paper' and usuario=='paper':
                #await ctx.send('It is a TIE')
                resultado.add_field(name='FINAL RESULT', value='**It is a TIE**',inline=False)

            ### scissors
            if IA=='scissors' and usuario=='rock':
                #await ctx.send('You WIN')
                resultado.add_field(name='FINAL RESULT', value='**You WIN**',inline=False)
            elif IA=='scissors' and usuario=='scissors':
                #await ctx.send('It is a TIE')
                resultado.add_field(name='FINAL RESULT', value='**It is a TIE**',inline=False)
            elif IA=='scissors' and usuario=='paper':
                #await ctx.send('The IA WINS')
                resultado.add_field(name='FINAL RESULT', value='**The IA WINS**',inline=False)

            ### rock
            if IA=='rock' and usuario=='rock':
                #await ctx.send('It is a TIE')
                resultado.add_field(name='FINAL RESULT', value='**It is a TIE**',inline=False)
            elif IA=='rock' and usuario=='scissors':
                #await ctx.send('The IA WINS')
                resultado.add_field(name='FINAL RESULT', value='**The IA WINS**',inline=False)
            elif IA=='rock' and usuario=='paper':
                #await ctx.send('You WIN')
                resultado.add_field(name='FINAL RESULT', value='**You WIN**',inline=False)

            
            await ctx.send(embed=resultado)

    ### Comando adivina el numero ###
    @commands.command(name='game2', description='', help='',  aliases=['g2'])
    async def _game2(self, ctx, min_Num,max_Num, eleccion):

        try:
            num_Oculto_lista=[*range(int(min_Num),int(max_Num),1)]

            num_Oculto=random.choice(num_Oculto_lista)

            int2=int(eleccion)

            if num_Oculto == int2:
                embed=nextcord.Embed(title='[Die-BOT] Guess the Number GAME :video_game:', description='Congratulations, you guessed it', color=0x00ff00)
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
                await ctx.send(embed=embed)

            elif int2 < int(min_Num) or int2 > int(max_Num):
                embed2=nextcord.Embed(title='[Die-BOT] Guess the Number GAME :video_game:', description='Your number selection is less than **num_Min** or greater than **num_Max**.', color=0x00ff00)
                embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
                await ctx.send(embed=embed2)
            
            elif int2 != num_Oculto:
                embed3=nextcord.Embed(title='[Die-BOT] Guess the Number GAME :video_game:', description='You missed, best of luck next time.', color=0x00ff00)
                embed3.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                embed3.set_footer(text=f'Command executed by: {ctx.author.display_name}')
                await ctx.send(embed=embed3)

            else:
                
                embed4=nextcord.Embed(title='[Die-BOT] Guess the Number GAME :video_game:', description='Unexpected ERROR :cry:.', color=0x00ff00)
                embed4.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                embed4.set_footer(text=f'Command executed by: {ctx.author.display_name}')
                await ctx.send(embed=embed4)

        except ValueError:
                embed5=nextcord.Embed(title='[Die-BOT] Guess the Number GAME :video_game:', description='You can only send integer number.', color=0x00ff00)
                embed5.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                embed5.set_footer(text=f'Command executed by: {ctx.author.display_name}')
                await ctx.send(embed=embed5)

    ### Comando Peliculas ###
    @commands.command(name='movie', description='', help='', aliases=['pelicula', 'peli'])
    async def _movie(self, ctx, peli, horario, productor, actores):
        async with ctx.typing():
            await asyncio.sleep(0.5)

        member=ctx.author
        embed=nextcord.Embed(title='Movie of the day', description='Cine Fulbito, presents: **{}**'.format(peli), color=0x00ff00)
        embed.add_field(name='Starting time of the movie: ', value=horario + 'HS', inline=False)
        embed.add_field(name='Productor: ', value=productor, inline=True)
        embed.add_field(name='Principals actors: ', value=actores, inline=True)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777')
        embed.set_footer(text='Command executed by: {}'.format(ctx.author.display_name))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))