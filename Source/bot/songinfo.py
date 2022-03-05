from contextvars import Context
import datetime
import nextcord
from cfg import cfg


class Song():
    def __init__(self, origin, host, base_url=None, uploader=None, title=None, duration=None, webpage_url=None, thumbnail=None):
        self.host = host
        self.origin = origin
        self.base_url = base_url
        self.info = self.Sinfo(uploader, title, duration,
                               webpage_url, thumbnail)

    class Sinfo:
        def __init__(self, uploader, title, duration, webpage_url, thumbnail):
            self.uploader = uploader
            self.title = title
            self.duration = duration
            self.webpage_url = webpage_url
            self.image = thumbnail
            self.output = ""
            
        

        def format_output(self, playtype, ctx, pasando):

            embed = nextcord.Embed(title=playtype, description=f"{pasando} [{self.title}]({self.webpage_url})", color=0x8633FF)
            embed.set_thumbnail(url="https://clicklo.net/h2d89")

            if self.image is not None:
                embed.set_image(url=self.image)

            embed.add_field(name="Author: ",
                            value=self.uploader, inline=True)

            if self.duration is not None:
                embed.add_field(name="Duration: ",
                                value=f"{str(datetime.timedelta(seconds=self.duration))}", inline=True)
            else:
                embed.add_field(name="Duration: ",
                                value="Unknown duration" , inline=True)
            
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_footer(text=f'Command executed by: {ctx.author.display_name}')

            
           

            return embed
