import os

import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions

from cfg import cfg
from bot.audiocontroller import AudioController
from bot.settings import Settings
from bot.utils import guild_to_audiocontroller, guild_to_settings
from bot.commands import CHelp




initial_extensions = ['bot.commands.music',
                      'bot.commands.general', 'bot.plugins.button', 'bot.commands.mcommands', 'bot.commands.funcommands', 'bot.commands.modcommands']

intents=nextcord.Intents.default()
intents.members= True

bot = commands.Bot(command_prefix=cfg.BOT_PREFIX, description="Bot created by Diego Libonati",
                   pm_help=True, case_insensitive=True, intents=intents)

if __name__ == '__main__':

    cfg.ABSOLUTO = os.path.dirname(os.path.abspath(__file__))
    cfg.COOKIE = cfg.ABSOLUTO + cfg.COOKIE



    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)

@bot.remove_command('help')

@bot.event

async def on_ready():
    print(cfg.MENSAJE_INICIO)
    await bot.change_presence(activity=nextcord.Game(name=f'Instagram: @die_libonati, type !d help'))

    for discord in bot.guilds:
        await register(discord)
        print(f"Ingrese a:  {discord.name}")

    print(cfg.MENSAJE_INICIO_DISCORD)


@bot.event
async def on_guild_join(discord):
    print(discord.name)
    await register(discord)

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

        embed=nextcord.Embed(title="HELP COMMAND :gear:", description="Hi, I´m Die-BOT. The help arrived", color=0xe74c3c, url="https://www.instagram.com/die_libonati/?hl=es-la")
        embed.add_field(name="GENERAL COMMANDS", value=", ".join(CHelp.General_Commands), inline=False)
        embed.add_field(name="FUN COMMANDS", value=", ".join(CHelp.Fun_Commands), inline=False)
        embed.add_field(name="MUSIC COMMANDS", value=", ".join(CHelp.Music_Commands), inline=False)
        embed.add_field(name="MORE MUSIC COMMANDS", value=", ".join(CHelp.Music_CommandsTwo), inline=False)
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

async def register(discord):

    guild_to_settings[discord] = Settings(discord)
    guild_to_audiocontroller[discord] = AudioController(bot, discord)

    st = guild_to_settings[discord]

    try:
        await discord.me.edit(nick=st.get('default_nickname'))
    except:
        pass

    if cfg.GLOBAL_DISABLE_AUTOJOIN_VC == True:
        return

    vc_cs = discord.voice_channels

    if st.get('vc_timeout') == False:
        if st.get('start_voice_channel') == None:
            try:
                await guild_to_audiocontroller[discord].register_voice_channel(discord.voice_channels[0])
            except Exception as e:
                print(e)

        else:
            for vc in vc_cs:
                if vc.id == st.get('start_voice_channel'):
                    try:
                        await guild_to_audiocontroller[discord].register_voice_channel(vc_cs[vc_cs.index(vc)])
                    except Exception as e:
                        print(e)

bot.run("OTM4MjA5MjMzMDAwODgyMTg2.Yfm9cA.aYP21m-Z_DO6JS8ZCYZRohFFcWo")
