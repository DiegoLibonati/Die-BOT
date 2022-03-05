import json
import os

import nextcord
from cfg import cfg

dir_path = os.path.dirname(os.path.realpath(__file__))


class Settings():

    def __init__(self, discord):
        self.discord = discord
        self.json_data = None
        self.cfg = None
        self.path = '{}/generated/settings.json'.format(dir_path)

        self.settings_template = {
            "id": 0,
            "default_nickname": "",
            "command_channel": None,
            "start_voice_channel": None,
            "user_must_be_in_vc": True,
            "button_emote": "",
            "default_volume": 100,
            "vc_timeout": cfg.VC_TIMOUT_DEFAULT
        }

        self.reload()
        self.upgrade()

    async def write(self, setting, value, ctx):
        response = await self.process_setting(setting, value, ctx)

        with open(self.path, 'w') as source:
            json.dump(self.json_data, source)
        self.reload()
        return response

    def reload(self):
        source = open(self.path, 'r')
        self.json_data = json.load(source)

        target = None

        for server in self.json_data:
            server = self.json_data[server]

            if server['id'] == self.discord.id:
                target = server

        if target == None:
            self.create()
            return

        self.cfg = target

    def upgrade(self):
        refresh = False
        for key in self.settings_template.keys():
            if not key in self.cfg:
                self.cfg[key] = self.settings_template.get(key)
                refresh = True
        if refresh:
            with open(self.path, 'w') as source:
                json.dump(self.json_data, source)
            self.reload()

    def create(self):

        self.json_data[self.discord.id] = self.settings_template
        self.json_data[self.discord.id]['id'] = self.discord.id

        with open(self.path, 'w') as source:
            json.dump(self.json_data, source)
        self.reload()

    def get(self, setting):
        return self.cfg[setting]

    async def format(self):
        embed = nextcord.Embed(
            title="Settings", description=self.discord.name, color=cfg.EMBED_COLOR)

        embed.set_thumbnail(url=self.discord.icon_url)
        embed.set_footer(
            text="Usage: {}set setting_name value".format(cfg.BOT_PREFIX))

        exclusion_keys = ['id']

        for key in self.cfg.keys():
            if key in exclusion_keys:
                continue

            if self.cfg.get(key) == "" or self.cfg.get(key) == None:

                embed.add_field(name=key, value="Not Set", inline=False)
                continue

            elif key == "start_voice_channel":
                if self.cfg.get(key) != None:
                    found = False
                    for vc in self.discord.voice_channels:
                        if vc.id == self.cfg.get(key):
                            embed.add_field(
                                name=key, value=vc.name, inline=False)
                            found = True
                    if found == False:
                        embed.add_field(
                            name=key, value="Invalid VChannel", inline=False)

                    continue

            elif key == "command_channel":
                if self.cfg.get(key) != None:
                    found = False
                    for chan in self.discord.text_channels:
                        if chan.id == self.cfg.get(key):
                            embed.add_field(
                                name=key, value=chan.name, inline=False)
                            found = True
                    if found == False:
                        embed.add_field(
                            name=key, value="Invalid Channel", inline=False)
                    continue

            embed.add_field(name=key, value=self.cfg.get(key), inline=False)

        return embed

    async def process_setting(self, setting, value, ctx):

        switcher = {
            'default_nickname': lambda: self.default_nickname(setting, value, ctx),
            'command_channel': lambda: self.command_channel(setting, value, ctx),
            'start_voice_channel': lambda: self.start_voice_channel(setting, value, ctx),
            'user_must_be_in_vc': lambda: self.user_must_be_in_vc(setting, value, ctx),
            'button_emote': lambda: self.button_emote(setting, value, ctx),
            'default_volume': lambda: self.default_volume(setting, value, ctx),
            'vc_timeout': lambda: self.vc_timeout(setting, value, ctx),
        }
        func = switcher.get(setting)

        if func is None:
            return None
        else:
            answer = await func()
            if answer == None:
                return True
            else:
                return answer

    # -----setting methods-----

    async def default_nickname(self, setting, value, ctx):

        if value.lower() == "unset":
            self.cfg[setting] = ""
            return

        if len(value) > 32:
            await ctx.send("`Error: Nickname exceeds character limit`\nUsage: {}set {} nickname\nOther options: unset".format(cfg.BOT_PREFIX, setting))
            return False
        else:
            self.cfg[setting] = value
            try:
                await self.discord.me.edit(nick=value)
            except:
                await ctx.send("`Error: Cannot set nickname. Please check bot permissions.")


    async def command_channel(self, setting, value, ctx):

        if value.lower() == "unset":
            self.cfg[setting] = None
            return

        found = False
        for chan in self.discord.text_channels:
            if chan.name.lower() == value.lower():
                self.cfg[setting] = chan.id
                found = True
        if found == False:
            await ctx.send("`Error: Channel name not found`\nUsage: {}set {} channelname\nOther options: unset".format(cfg.BOT_PREFIX, setting))
            return False

    async def start_voice_channel(self, setting, value, ctx):

        if value.lower() == "unset":
            self.cfg[setting] = None
            return

        found = False
        for vc in self.discord.voice_channels:
            if vc.name.lower() == value.lower():
                self.cfg[setting] = vc.id
                self.cfg['vc_timeout'] = False
                found = True
        if found == False:
            await ctx.send("`Error: Voice channel name not found`\nUsage: {}set {} vchannelname\nOther options: unset".format(cfg.BOT_PREFIX, setting))
            return False

    async def user_must_be_in_vc(self, setting, value, ctx):
        if value.lower() == "true":
            self.cfg[setting] = True
        elif value.lower() == "false":
            self.cfg[setting] = False
        else:
            await ctx.send("`Error: Value must be True/False`\nUsage: {}set {} True/False".format(cfg.BOT_PREFIX, setting))
            return False

    async def button_emote(self, setting, value, ctx):

        if value.lower() == "unset":
            self.cfg[setting] = ""
            return

        emoji = nextcord.utils.get(self.discord.emojis, name=value)
        if emoji is None:
            await ctx.send("`Error: Emote name not found on server`\nUsage: {}set {} emotename\nOther options: unset".format(cfg.BOT_PREFIX, setting))
            return False
        else:
            self.cfg[setting] = value

    async def default_volume(self, setting, value, ctx):
        try:
            value = int(value)
        except:
            await ctx.send("`Error: Value must be a number`\nUsage: {}set {} 0-100".format(cfg.BOT_PREFIX, setting))
            return False

        if value > 100 or value < 0:
            await ctx.send("`Error: Value must be a number`\nUsage: {}set {} 0-100".format(cfg.BOT_PREFIX, setting))
            return False

        self.cfg[setting] = value

    async def vc_timeout(self, setting, value, ctx):

        if cfg.ALLOW_VC_TIMEOUT_EDIT == False:
            await ctx.send("`Error: This value cannot be modified".format(cfg.BOT_PREFIX, setting))

        if value.lower() == "true":
            self.cfg[setting] = True
            self.cfg['start_voice_channel'] = None
        elif value.lower() == "false":
            self.cfg[setting] = False
        else:
            await ctx.send("`Error: Value must be True/False`\nUsage: {}set {} True/False".format(cfg.BOT_PREFIX, setting))
            return False
