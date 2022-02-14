import nextcord
from nextcord.ext import commands
import eventos
import comandos


############################## Llamadas a funciones MAIN ##################################

############# EVENTOS
async def on_ready():
    await eventos.on_ready()

async def on_command_error():
    await eventos.on_command_error()


### COMANDOS ###
### COMANDOS MISC ###
async def ping():
    await comandos.ping()

async def informacion():
    await comandos.information()

async def latencia():
    await comandos.latency()

 
### COMANDOS FUN ###
async def eightball():
    await comandos.eightball()

async def pelicula():
    await comandos.movie()

### COMANDOS MOD ###
async def mover():
    await comandos.move()

async def rol():
    await comandos.rol()

async def sacarrol():
    await comandos.drol()

async def silence():
    await comandos.silence()

async def desilence():
    await comandos.desilence()

async def deafen():
    await comandos.deafen()

async def dedeafen():
    await comandos.dedeafen()

async def sdall():
    await comandos.sdall()

async def sdunall():
    await comandos.sdunall()

async def disconnect():
    await comandos.disconnect() 
################# RUN
comandos.bot.run('OTM4MjA5MjMzMDAwODgyMTg2.Yfm9cA.ANRwzPy6nHjeK7z1OBYokAb8rBI')
