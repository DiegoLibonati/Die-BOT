import asyncio
from cfg import cfg


guild_to_audiocontroller = {}


guild_to_settings = {}


def get_guild(bot, command):
   
    if command.guild is not None:
        return command.guild
    for guild in bot.guilds:
        for channel in guild.voice_channels:
            if command.author in channel.members:
                return guild
    return None


async def connect_to_channel(guild, dest_channel_name, ctx, switch=False, default=True):
 
    for channel in guild.voice_channels:
        if str(channel.name).strip() == str(dest_channel_name).strip():
            if switch:
                try:
                    await guild.voice_client.disconnect()
                except:
                    await ctx.send(cfg.MENSAJE_NO_CONECTADO)

            await channel.connect()
            return

    if default:
        try:
            await guild.voice_channels[0].connect()
        except:
            await ctx.send(cfg.CANAL_DEFECTO_ERROR_INICIO)
    else:
        await ctx.send(cfg.CANAL_NOENCONTRADO_MENSAJE + str(dest_channel_name))


async def is_connected(ctx):
    try:
        voice_channel = ctx.guild.voice_client.channel
        return voice_channel
    except:
        return None


async def play_check(ctx):

    sett = guild_to_settings[ctx.guild]

    cm_channel = sett.get('command_channel')
    vc_rule = sett.get('user_must_be_in_vc')

    if cm_channel != None:
        if cm_channel != ctx.message.channel.id:
            await ctx.send(cfg.CANAL_EQUIVOCADO_MENSAJE)
            return False

    if vc_rule == True:
        author_voice = ctx.message.author.voice
        bot_vc = ctx.guild.voice_client.channel
        if author_voice == None:
            await ctx.send(cfg.USER_NO_EN_VC)
            return False
        elif ctx.message.author.voice.channel != bot_vc:
            await ctx.send(cfg.USER_NO_EN_VC)
            return False


class Timer:
    def __init__(self, callback):
        self._callback = callback
        self._task = asyncio.create_task(self._job())

    async def _job(self):
        await asyncio.sleep(cfg.VC_TIEMPOPERDIDO)
        await self._callback()

    def cancel(self):
        self._task.cancel()
