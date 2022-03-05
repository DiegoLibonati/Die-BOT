BOT_TOKEN: str = ""
SPOTIFY_ID: str = ""
SPOTIFY_SECRET: str = ""

BOT_PREFIX = "!d "

EMBED_COLOR = 0x4dd4d0  

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

MAX_SONG_PRELOAD = 5  #maximum of 25

COOKIE = "/cfg/cookies/cookies.txt"

GLOBAL_DISABLE_AUTOJOIN_VC = False

VC_TIEMPOPERDIDO = 600
VC_TIMOUT_DEFAULT = True  
ALLOW_VC_TIMEOUT_EDIT = True  


MENSAJE_INICIO = "Arrancando BOT"
MENSAJE_INICIO_DISCORD = "BOT FUNCIONANDO"

AUSENTE_CANAL = 'Please join a voice channel or enter the command in guild chat'
USER_NO_EN_VC = "Please join the active voice channel to use commands"
CANAL_EQUIVOCADO_MENSAJE = "Please use configured command channel"
MENSAJE_NO_CONECTADO = "Bot not connected to any voice channel"
ALREADY_CONNECTED_MESSAGE = "Already connected to a voice channel"
CANAL_NOENCONTRADO_MENSAJE = "Could not find channel"
CANAL_DEFECTO_ERROR_INICIO = "Could not join the default voice channel"
INVALID_INVITE_MESSAGE = "Invalid invitation link"

ADD_MESSAGE= "To add this bot to your own Server, click [here]" 

INFO_HISTORY_TITLE = "**Songs Played:**"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15



SONGINFO_SECONDS = "s"
SONGINFO_LIKES = "Likes: "
SONGINFO_DISLIKES = "Dislikes: "



AGREGAR_BOT = "Add this Bot to another server"
HELP_ADDBOT_LONG = "Gives you the link for adding this bot to another server of yours."

HELP_SETTINGS_SHORT = "View and set bot settings"
HELP_SETTINGS_LONG = "View and set bot settings in the server. Usage: {}settings setting_name value".format(BOT_PREFIX)

HELP_HISTORY_SHORT = "Show history of songs"
HELP_HISTORY_LONG = "Shows the " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " last played songs."
HELP_YT_SHORT = "Play a supported link or search on youtube"
HELP_YT_LONG = ("$p [link/video title/key words/playlist-link/soundcloud link/spotify link/bandcamp link/twitter link]")


ABSOLUTO = ''