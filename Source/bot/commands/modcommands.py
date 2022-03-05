import nextcord
from nextcord.ext import commands
import asyncio
from nextcord.ext.commands import has_guild_permissions

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ### COMANDOS MOD ###
    ### Comando para mover ###
    @commands.command(name='move', description="", help="", aliases=["mover"])
    @has_guild_permissions(move_members=True)
    async def _move(self, ctx, member:nextcord.Member, canal:nextcord.VoiceChannel,*, reason=None):
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

    ### Comando para agregar roles ###
    @commands.command(name='rol', description="", help="", aliases=["rl"])
    @has_guild_permissions(manage_roles=True)
    async def _rol(self, ctx, member:nextcord.Member, roles:nextcord.Role, reason=None, atomic=True):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.add_roles(roles, reason=reason)
        embed=nextcord.Embed(title="[Die-BOT] ADD ROL :man_mechanic:", description=f"This command allows the mod to give role to the users.\n\n The user **{ctx.author.display_name}**, give: **{roles}** to **{member}**.\nReason: **{reason}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para sacar roles ###
    @commands.command(name='drol', description="", help="", aliases=["drl"])
    @has_guild_permissions(manage_roles=True)
    async def _drol(self, ctx, member:nextcord.Member, roles:nextcord.Role, reason=None, atomic=True):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.remove_roles(roles, reason=reason)
        embed=nextcord.Embed(title="[Die-BOT] REMOVE ROL :man_mechanic:", description=f"This command allows the mod to unrole the users.\n\n The user **{ctx.author.display_name}**, take out the role: **{roles}** to **{member}**.\nReason: **{reason}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para Mutear ###
    @commands.command(name='silence', description="", help="", aliases=["sil"])
    @has_guild_permissions(mute_members=True)
    async def _silence(self, ctx, member:nextcord.Member, mute=False):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.edit(mute=True)
        embed=nextcord.Embed(title="[Die-BOT] SILENCE :man_mechanic:", description=f"The user **{member}** was silence by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)


    ### Comando para Desmutear ###
    @commands.command(name='desilence', description="", help="", aliases=["desil"])
    @has_guild_permissions(mute_members=True)
    async def _desilence(self, ctx, member:nextcord.Member, mute=True):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.edit(mute=False)
        embed=nextcord.Embed(title="[Die-BOT] DESILENCE :man_mechanic:", description=f"The user **{member}** was unsilence by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para ensordecer ###
    @commands.command(name='deafen', description="", help="", aliases=["df"])
    @has_guild_permissions(deafen_members=True)
    async def _deafen(self, ctx, member:nextcord.Member, deafen=False):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.edit(deafen=True)
        embed=nextcord.Embed(title="[Die-BOT] DEAFEN :man_mechanic:", description=f"The user **{member}** was deafen by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para desendordeser ###
    @commands.command(name='dedeafen', description="", help="", aliases=["dedf"])
    @has_guild_permissions(deafen_members=True)
    async def _dedeafen(self, ctx, member:nextcord.Member, deafen=True):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.edit(deafen=False)
        embed=nextcord.Embed(title="[Die-BOT] DEDEAFEN :man_mechanic:", description=f"The user **{member}** now listen by: **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para ensordecer y silenciar ###
    @commands.command(name='sdall', description="", help="", aliases=["sdal"])
    @has_guild_permissions(mute_members=True)
    @has_guild_permissions(deafen_members=True)
    async def _sdall(self, ctx, member:nextcord.Member, mute=False, deafen=False):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.edit(mute=True, deafen=True)
        embed=nextcord.Embed(title="[Die-BOT] SDALL :man_mechanic:", description=f"The user **{member}** was silenced and muted by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para que escuchen y hablen ###
    @commands.command(name='sdunall', description="", help="", aliases=["sdunal"])
    @has_guild_permissions(mute_members=True)
    @has_guild_permissions(deafen_members=True)
    async def _sdunall(self, ctx, member:nextcord.Member, mute=True, deafen=True):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.edit(mute=False, deafen=False)
        embed=nextcord.Embed(title="[Die-BOT] SDUNALL :man_mechanic:", description=f"The user **{member}** now can talk and listen by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para desconectar ###
    @commands.command(name='disconnect', description="", help="", aliases=["dis"])
    @has_guild_permissions(move_members=True)
    async def _disconnect(self, ctx, member:nextcord.Member, voice_channel=None):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.edit(voice_channel=None)
        embed=nextcord.Embed(title="[Die-BOT] DISCONNECT :man_mechanic:", description=f"The user **{member}**, was disconnected by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
        
    ### Comando para banear ###

    @commands.command(name='ban', description="", help="", aliases=["b"])
    @has_guild_permissions(ban_members=True)
    async def _ban(self, ctx, member:nextcord.Member, delete_message_days=None, reason=None):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.ban(delete_message_days=delete_message_days, reason=reason)
        embed=nextcord.Embed(title="[Die-BOT] BAN :man_mechanic:", description=f"The user **{member}** was banned by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para desbanear ###

    @commands.command(name='unban', description="", help="", aliases=["unb"])
    @has_guild_permissions(ban_members=True)
    async def _unban(self, ctx, member:nextcord.Member, reason=None):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.ban(reason=reason)
        embed=nextcord.Embed(title="[Die-BOT] UNBAN :man_mechanic:", description=f"The user **{member}** was unbanned by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para kickear ###
    @commands.command(name='kick', description="", help="", aliases=["k"])
    @has_guild_permissions(kick_members=True)
    async def _kick(self, ctx, member:nextcord.Member, reason=None):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.kick(reason=reason)
        embed=nextcord.Embed(title="[Die-BOT] KICK :man_mechanic:", description=f"The user **{member}**, was kicked by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    ### Comando para tener Prioridad de habla ### 
    @commands.command(name='ptospeak', description="", help="", aliases=["ptos"])
    @has_guild_permissions(priority_speaker=True)
    async def _ptospeak(self, ctx, member:nextcord.Member):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await member.request_to_speak()
        embed=nextcord.Embed(title="[Die-BOT] REQUEST TO SPEAK :man_mechanic:", description=f"The user **{member}** now have request to speak by **{ctx.author.display_name}**", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        ctx.send(embed=embed)

    ### Comando para borrar mensajes ###
    @commands.command(name='purge', description="", help="", aliases=["prg"])
    @has_guild_permissions(manage_messages=True, read_message_history=True)
    async def _purge(self, ctx, canal:nextcord.TextChannel, limit=None):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        await canal.purge(limit=int(limit)+1)

        embed=nextcord.Embed(title="[Die-BOT] CLEAR CHAT :man_mechanic:", description=f"**{limit}** messages were deleted from the cannel: **{canal}** successfully", color=0x9b59b6)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://scontent.faep27-1.fna.fbcdn.net/v/t39.30808-6/272969632_5390252007663516_955583038628786681_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeELecj1C0fnQYabp1MQUY_pHhRxlOGRhiYeFHGU4ZGGJsWxTWTjuWrUKmP3NQ3Rgjl41K9wDEDpo8JeRS-qUkRP&_nc_ohc=IwX3gRujH8cAX8zVbIy&_nc_ht=scontent.faep27-1.fna&oh=00_AT9Hm7_EFJDbycE2gAWpmPdUqRHPSgHG__WaSmwkU2RmZA&oe=6214D777")
        embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Mod(bot))