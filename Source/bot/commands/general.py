import nextcord
from nextcord.ext import commands
from cfg import cfg
import asyncio
import time
import random 



class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ### COMANDOS Generales ###

    ### Comando Ping ###
    @commands.command(name='ping', description='', help='', aliases=['pi']) # Decorador que permite crear un comando pero con una funcion
    async def _ping(self, ctx):
            async with ctx.typing():
                await asyncio.sleep(0.5)

            await ctx.send('I am working :robot:!')

    ### Comando InformacionServer ###
    @commands.command(name='information', description='', help='', aliases=['info', 'inf'])
    async def _information(self, ctx):
            async with ctx.typing():
                await asyncio.sleep(0.5)
                member=ctx.author
            embed=nextcord.Embed(title='[Die-BOT] Server information :gear:', url='https://www.instagram.com/die_libonati/?hl=es-la', description='Fulbito FC official SERVER by Discord', color=0xe74c3c)
            embed.add_field(name='Server created by ',value=f'{ctx.guild.owner}', inline=False)
            embed.add_field(name='Server created date ', value=f'{ctx.guild.created_at}', inline=False)
            embed.add_field(name='Server member count', value=f'{ctx.guild.member_count}', inline=False)
            embed.set_author(name=member.display_name, icon_url=member.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_image(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text='Command executed by: {}'.format(member.display_name))
            await ctx.send(embed=embed)

    ### Comando Latencia ###
    @commands.command(name='latency', description='', help='', aliases=['Latencia', 'lat'])
    async def _latency(self, ctx, *args):
            async with ctx.typing():
                await asyncio.sleep(0.5)

            inicio=time.time()
            mensaje= await ctx.send('Obtaining Ping')
            await mensaje.edit(content='Obtaining Ping.')
            await mensaje.edit(content='Obtaining Ping..')
            await mensaje.edit(content='Obtaining Ping...')
            await mensaje.edit(content='¡Successful achievement of Ping!')
            fin=time.time()

            embed=nextcord.Embed(title='[Die-BOT] LATENCY :gear:', description='This COMMAND gets the actual latency from WebSocket and Die-BOT API.', color=0xe74c3c)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.add_field(name='LATENCY WEBSOCKET', value=f'{round(self.bot.latency*1000)} MS', inline=True)
            embed.add_field(name='LATENCY API', value=f'{round((fin-inicio)*100)} MS', inline=True)
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')

            await ctx.send(embed=embed)

    ### Comando About ###
    @commands.command(name='about', description='', help='', aliases=['ab'])
    async def _about(self, ctx):
            embed=nextcord.Embed(title='[Die-BOT] About this BOT :gear:', description='Hi, i´m Libonati Diego', color=0xe74c3c)
            embed.add_field(name='Information', value='This bot was created by Libonati Diego. I am from Argentina and i used Python to build this BOT.\n\
            If you need help, type **!d help** and help will arrive to your private messages. Soon you can donate to support this bot.\n\
            **My instagram:** https://www.instagram.com/die_libonati\n\
            **My GitHub:** https://github.com/DiegoLibonati')
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            embed.set_image(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            await ctx.send(embed=embed)

    ### Comando Avatar ###
    @commands.command(name='avatar', description='', help='', aliases=['av'])
    async def _avatar(self, ctx, user:nextcord.User):
            embed=nextcord.Embed(title='[Die-BOT] AVATAR :gear:', color=0xe74c3c)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_image(url=user.avatar)
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)

    ### Comando User-Info ###
    @commands.command(name='userinfo', description='', help='', aliases=['ui', 'useri'])
    async def _userinfo(self, ctx, user:nextcord.User):

            embed=nextcord.Embed(title='[Die-BOT] USER INFORMATION :gear:', color=0xe74c3c)
            embed.add_field(name='User created at', value=user.created_at, inline=False)
            embed.add_field(name='User name', value=user.name, inline=False)
            embed.add_field(name='User ID', value=user.id, inline=False)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_image(url=user.avatar)
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
    
    ### Comando AddBot ###
    @commands.command(name='addbot', description="", help="")
    async def _addbot(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        embed = nextcord.Embed(title='[Die-BOT] Invite :incoming_envelope:', description=cfg.AGREGAR_BOT +  
                                            f" https://discordapp.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot", color=0x8633FF)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
