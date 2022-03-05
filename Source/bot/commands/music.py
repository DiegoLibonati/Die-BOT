import asyncio
import nextcord
from cfg import cfg
from nextcord.ext import commands
from bot import linkutils, utils


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play', description="", help="",
                      aliases=['p', 'yt', 'pl'])
    async def _play_song(self, ctx, *, track: str):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        cg = utils.get_guild(self.bot, ctx.message)
        ac = utils.guild_to_audiocontroller[cg]

        if (await utils.is_connected(ctx) == None):
            if await ac.uconnect(ctx) == False:
                return

        if track.isspace() or not track:
            return

        if await utils.play_check(ctx) == False:
            return

        # reset timer
        ac.timer.cancel()
        ac.timer = utils.Timer(ac.timeout_handler)

        if ac.playlist.loop == True:
            embed=nextcord.Embed(title='[Die-BOT] Loop :dvd:', description=f'Loop is enabled in **{ctx.author.voice.channel}**! Use {cfg.BOT_PREFIX} loop to disable' , color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)

            return

        s = await ac.process_song(track)

        if s is None:
            embed2=nextcord.Embed(title='[Die-BOT] Song info ERROR :cry:', description='Unsupported site or age restricted content. To enable age restricted content check the **documentation/wiki**.' , color=0x8633FF)
            embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            await ctx.send(embed=embed2)

            return

        if s.origin == linkutils.Origins.Default:

            if ac.current_song != None and len(ac.playlist.playque) == 0:
                await ctx.send(embed=s.info.format_output("[Die-BOT] Play :dvd:", ctx, "You are listening: "))
            else:
                await ctx.send(embed=s.info.format_output("[Die-BOT] Added to queue :dvd:", ctx, "Song added to Queue: "))

        elif s.origin == linkutils.Origins.Playlist:
            embed3= nextcord.Embed(title='[Die-BOT] Queued playlist :page_with_curl:', description="The playlist was added succesfully :white_check_mark:", color=0x8633FF)
            embed3.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed3.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed3.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed3)

    @commands.command(name='loop', description="", help="", aliases=['l'])
    async def _loop(self, ctx):

        cg = utils.get_guild(self.bot, ctx.message)
        ac = utils.guild_to_audiocontroller[cg]

        if await utils.play_check(ctx) == False:
            return

        if len(ac.playlist.playque) < 1 and cg.voice_client.is_playing() == False:
            embed=nextcord.Embed(title="[Die-BOT] Loop :dvd:", description="No songs in queue.", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return

        if ac.playlist.loop == False:
            ac.playlist.loop = True
            embed2=nextcord.Embed(title="[Die-BOT] Loop :dvd:", description="Loop enabled :arrows_counterclockwise:", color=0x8633FF)
            embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed2)

        else:
            ac.playlist.loop = False
            embed3=nextcord.Embed(title="[Die-BOT] Loop :dvd:", description="Loop disabled :x:", color=0x8633FF)
            embed3.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed3.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed3.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed3)

    @commands.command(name='shuffle', description="", help="",
                      aliases=["sh"])
    async def _shuffle(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)
        ac = utils.guild_to_audiocontroller[cg]

        if await utils.play_check(ctx) == False:
            return

        if cg is None:
            embed=nextcord.Embed(title="[Die-BOT] Suffle :dvd:",description=f"{cfg.AUSENTE_CANAL}", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)

            return
        if cg.voice_client is None or not cg.voice_client.is_playing():
            embed2=nextcord.Embed(title="[Die-BOT] Suffle :dvd:",description="Queue is empty :x:", color=0x8633FF)
            embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed2)
            return

        ac.playlist.shuffle()
        embed3=nextcord.Embed(title="[Die-BOT] Suffle :dvd:",description="Shuffled queue :twisted_rightwards_arrows:", color=0x8633FF)
        embed3.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed3.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed3.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed3)

        for song in list(ac.playlist.playque)[:cfg.MAX_SONG_PRELOAD]:
            asyncio.ensure_future(ac.preload(song))

    @commands.command(name='pause', description="", help="")
    async def _pause(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if cg is None:
            embed=nextcord.Embed(title="[Die-BOT] Pause :dvd:",description=f"{cfg.AUSENTE_CANAL}", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return
        if cg.voice_client is None or not cg.voice_client.is_playing():
            return
        cg.voice_client.pause()
        embed2=nextcord.Embed(title="[Die-BOT] Pause :dvd:",description=f"Song paused by {ctx.author.display_name} :pause_button:", color=0x8633FF)
        embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed2)

    @commands.command(name='queue', description="", help="",
                      aliases=['playlist', 'q'])
    async def _queue(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if cg is None:
            embed=nextcord.Embed(title="[Die-BOT] Queue :dvd:",description=f"{cfg.AUSENTE_CANAL}", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return
        if cg.voice_client is None or not cg.voice_client.is_playing():
            embed2=nextcord.Embed(title="[Die-BOT] Queue :dvd:",description="Queue is empty :x:", color=0x8633FF)
            embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed2)

            return

        playlist = utils.guild_to_audiocontroller[cg].playlist

        # Embeds are limited to 25 fields
        if cfg.MAX_SONG_PRELOAD > 25:
            cfg.MAX_SONG_PRELOAD = 25

        embed3=nextcord.Embed(title="[Die-BOT] Queue :dvd:",description=f"The current **Queue** has **[{len(playlist.playque)}] songs** in the **playlist**", color=0x8633FF)
        embed3.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed3.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed3.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        

        for counter, song in enumerate(list(playlist.playque)[:cfg.MAX_SONG_PRELOAD], start=1):
            if song.info.title is None:
                embed3.add_field(name="{}.".format(str(counter)), value="[{}]({})".format(
                    song.info.webpage_url, song.info.webpage_url), inline=False)
            else:
                embed3.add_field(name="{}.".format(str(counter)), value="[{}]({})".format(
                    song.info.title, song.info.webpage_url), inline=False)

        await ctx.send(embed=embed3)

    @commands.command(name='stop', description="", help="", aliases=['st'])
    async def _stop(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        ac = utils.guild_to_audiocontroller[cg]
        ac.playlist.loop = False
        if cg is None:
            embed=nextcord.Embed(title="[Die-BOT] Stop :dvd:",description=f"{cfg.AUSENTE_CANAL}", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return
        await utils.guild_to_audiocontroller[cg].stop_player()
        embed2=nextcord.Embed(title="[Die-BOT] Stop :dvd:",description="Stopped all sessions :octagonal_sign:", color=0x8633FF)
        embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed2)

    @commands.command(name='movesong', description="", help="", aliases=['mv'])
    async def _movesong(self, ctx, *args):
        if len(args) != 2:
            embed=nextcord.Embed(title="[Die-BOT] Move :dvd:",description="Wrong number of arguments", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return

        try:
            oldindex, newindex = map(int, args)
        except ValueError:
            embed2=nextcord.Embed(title="[Die-BOT] Move :dvd:",description="Wrong argument", color=0x8633FF)
            embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed2)
            return

        cg = utils.get_guild(self.bot, ctx.message)
        ac = utils.guild_to_audiocontroller[cg]
        if cg.voice_client is None or (
                not cg.voice_client.is_paused() and not cg.voice_client.is_playing()):
            embed3=nextcord.Embed(title="[Die-BOT] Move :dvd:",description="Queue is empty :x:", color=0x8633FF)
            embed3.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed3.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed3.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed3)
            return
        try:
            ac.playlist.move(oldindex - 1, newindex - 1)
        except IndexError:
            embed4=nextcord.Embed(title="[Die-BOT] Move :dvd:",description="Wrong position", color=0x8633FF)
            embed4.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed4.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed4.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed4)
            return
        embed5=nextcord.Embed(title="[Die-BOT] Move :dvd:",description="Moved", color=0x8633FF)
        embed5.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed5.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed5.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed5)    

    @commands.command(name='skip', description="", help="", aliases=['s'])
    async def _skip(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        ac = utils.guild_to_audiocontroller[cg]
        ac.playlist.loop = False

        ac.timer.cancel()
        ac.timer = utils.Timer(ac.timeout_handler)

        if cg is None:
            await ctx.send(cfg.AUSENTE_CANAL)
            return
        if cg.voice_client is None or (
                not cg.voice_client.is_paused() and not cg.voice_client.is_playing()):
            embed=nextcord.Embed(title="[Die-BOT] Skip :dvd:",description="Queue is empty :x:", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return
        cg.voice_client.stop()
        embed2=nextcord.Embed(title="[Die-BOT] Skip :dvd:",description="Skipped current song :fast_forward:", color=0x8633FF)
        embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed2)

    @commands.command(name='clear', description="", help="", aliases=['cl'])
    async def _clear(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        ac = utils.guild_to_audiocontroller[cg]
        ac.clear_queue()
        cg.voice_client.stop()
        ac.playlist.loop = False
        embed=nextcord.Embed(title="[Die-BOT] Clear :dvd:",description="Cleared queue :no_entry_sign:", color=0x8633FF)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed)

    @commands.command(name='prev', description="", help="", aliases=['back'])
    async def _prev(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        ac = utils.guild_to_audiocontroller[cg]
        ac.playlist.loop = False

        ac.timer.cancel()
        ac.timer = utils.Timer(ac.timeout_handler)

        if cg is None:
            embed=nextcord.Embed(title="[Die-BOT] Prev :dvd:",description=f"{cfg.AUSENTE_CANAL}", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return
        await utils.guild_to_audiocontroller[cg].prev_song()
        embed2=nextcord.Embed(title="[Die-BOT] Prev :dvd:",description="Playing previous song :track_previous:", color=0x8633FF)
        embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed2)

    @commands.command(name='resume', description="", help="")
    async def _resume(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if cg is None:
            embed=nextcord.Embed(title="[Die-BOT] Resume :dvd:",description=f"{cfg.AUSENTE_CANAL}", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return

        cg.voice_client.resume()
        embed2=nextcord.Embed(title="[Die-BOT] Resume :dvd:",description="Resumed song :arrow_forward:", color=0x8633FF)
        embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed2)

    @commands.command(name='songinfo', description="", help="",
                      aliases=["np"])
    async def _songinfo(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if cg is None:
            embed2=nextcord.Embed(title="[Die-BOT] Song information :dvd:",description=f"{cfg.AUSENTE_CANAL}", color=0x8633FF)
            embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed2)
            return
        s = utils.guild_to_audiocontroller[cg].current_song
        if s is None:
            return
        await ctx.send(embed=s.info.format_output("[Die-BOT] Song information :dvd:", ctx, "Song: "))

    @commands.command(name='history', description="", help="")
    async def _history(self, ctx):
        cg = utils.get_guild(self.bot, ctx.message)

        if await utils.play_check(ctx) == False:
            return

        if cg is None:
            embed=nextcord.Embed(title="[Die-BOT] History :dvd:",description=f"{cfg.AUSENTE_CANAL}", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return
        embed2=nextcord.Embed(title="[Die-BOT] History :dvd:",description=f"{utils.guild_to_audiocontroller[cg].track_history()}", color=0x8633FF)
        embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
        embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
        await ctx.send(embed=embed2)

    @commands.command(name='volume', aliases=["vol"], description="", help="")
    async def _volume(self, ctx, *args):
        if ctx.guild is None:
            embed=nextcord.Embed(title="[Die-BOT] Volume :dvd:",description=f"{cfg.AUSENTE_CANAL}", color=0x8633FF)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed)
            return

        if await utils.play_check(ctx) == False:
            return

        if len(args) == 0:
            embed2=nextcord.Embed(title="[Die-BOT] Volume :dvd:",description=f"Current volume: {utils.guild_to_audiocontroller[ctx.guild]._volume}% :speaker:", color=0x8633FF)
            embed2.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed2.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed2.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed2)
            return

        try:
            volume = args[0]
            volume = int(volume)
            if volume > 100 or volume < 0:
                raise Exception('')
            cg = utils.get_guild(self.bot, ctx.message)

            if utils.guild_to_audiocontroller[cg]._volume >= volume:
                embed3=nextcord.Embed(title="[Die-BOT] Volume :dvd:",description=f"Volume set to {str(volume)}% :sound:", color=0x8633FF)
                embed3.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                embed3.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
                embed3.set_footer(text=f'Command executed by: {ctx.author.display_name}')
                await ctx.send(embed=embed3)
            else:
                embed4=nextcord.Embed(title="[Die-BOT] Volume :dvd:",description=f"Volume set to {str(volume)}% :loud_sound:", color=0x8633FF)
                embed4.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                embed4.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
                embed4.set_footer(text=f'Command executed by: {ctx.author.display_name}')
                await ctx.send(embed=embed4)
            utils.guild_to_audiocontroller[cg].volume = volume
        except:
            embed5=nextcord.Embed(title="[Die-BOT] Volume :dvd:",description=f"Error: Volume must be a number 1-100", color=0x8633FF)
            embed5.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed5.set_thumbnail(url='https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=6Ak8vqbSdSAAX_Zl2MT&_nc_ht=scontent.faep27-1.fna&oh=00_AT8cne-OOMaHpTXgyymA8j_b6BfOmG0-Iog6YV1CEhKmcA&oe=6222AF37')
            embed5.set_footer(text=f'Command executed by: {ctx.author.display_name}')
            await ctx.send(embed=embed5)




def setup(bot):
    bot.add_cog(Music(bot))
