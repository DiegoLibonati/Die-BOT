import nextcord
from cfg import cfg
from nextcord.ext import commands
from bot import utils
from bot.audiocontroller import AudioController
from bot.utils import guild_to_audiocontroller, guild_to_settings
from nextcord.ext.commands import has_guild_permissions
import asyncio

# Comandos de Generales de Musica

class M(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
   
    @commands.command(name='connect', description="", help="", aliases=['c'])
    async def _connect(self, ctx):  
        async with ctx.typing():
            await asyncio.sleep(0.5)
        cg = utils.get_guild(self.bot, ctx.message)
        ac = utils.guild_to_audiocontroller[cg]
        await ac.uconnect(ctx)

        embed=nextcord.Embed(title='[Die-BOT] Bot connected :dvd:', description=f'Connect to **{ctx.author.voice.channel}** by **{ctx.author.display_name}**', color=0x8633FF)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed)

    @commands.command(name='leave', description="", help="", aliases=['le'])
    async def _leave(self, ctx, guild=False):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        cg = utils.get_guild(self.bot, ctx.message)
        ac = utils.guild_to_audiocontroller[cg]
        await ac.udisconnect()

        embed=nextcord.Embed(title='[Die-BOT] Bot leave :dvd:', description=f'Leave from **{ctx.author.voice.channel}** by **{ctx.author.display_name}**', color=0x8633FF)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed)

    @commands.command(name='reset', description="", help="", aliases=['rs', 'restart'])
    async def _reset(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        cg = utils.get_guild(self.bot, ctx.message)

        if cg is None:
            await ctx.send(cfg.AUSENTE_CANAL)
            return
        await utils.guild_to_audiocontroller[cg].stop_player()
        await cg.voice_client.disconnect(force=True)

        guild_to_audiocontroller[cg] = AudioController(
            self.bot, cg)
        await guild_to_audiocontroller[cg].register_voice_channel(ctx.author.voice.channel)

        embed=nextcord.Embed(title='[Die-BOT] Bot reset :dvd:', description=f'Reset in **{ctx.author.voice.channel}** by **{ctx.author.display_name} ** successfully', color=0x8633FF)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed)

    @commands.command(name='changechannel', description="", help="", aliases=['cc'])
    async def _change_channel(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)

        cg = utils.get_guild(self.bot, ctx.message)

        vc = await utils.is_connected(ctx)

        if vc == ctx.author.voice.channel:
            embed=nextcord.Embed(title='[Die-BOT] Bot change channel :dvd:', description=f'Already connected to **{ctx.author.voice.channel}**' , color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return

        if cg is None:
            await ctx.send(cfg.AUSENTE_CANAL)
            return
        await utils.guild_to_audiocontroller[cg].stop_player()
        await cg.voice_client.disconnect(force=True)

        guild_to_audiocontroller[cg] = AudioController(
            self.bot, cg)
        await guild_to_audiocontroller[cg].register_voice_channel(ctx.author.voice.channel)

        embed2=nextcord.Embed(title='[Die-BOT] Bot change channel :dvd:', description=f'Switched to **{ctx.author.voice.channel}**' , color=0x8633FF)
        embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed2)

    @commands.command(name='setting', description="", help="", aliases=['settings', 'set'])
    @has_guild_permissions(administrator=True)
    async def _settings(self, ctx, *args):
        async with ctx.typing():
            await asyncio.sleep(0.5)

        sett = guild_to_settings[ctx.guild]

        if len(args) == 0:
            await ctx.send(embed=await sett.format())
            return

        args_list = list(args)
        args_list.remove(args[0])

        response = await sett.write(args[0], ' '.join(args_list), ctx)

        if response is None:
            embed=nextcord.Embed(title='[Die-BOT] Settings ERROR :dvd:', description=f'Setting not found :cry:' , color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
        elif response is True:
            embed=nextcord.Embed(title='[Die-BOT] Settings :white_check_mark: :dvd:', description=f'Setting updated :smile:' , color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(M(bot))