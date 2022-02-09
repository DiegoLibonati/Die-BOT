import nextcord
from nextcord.ext import commands
import eventos
import comandos


############################## Llamadas a funciones MAIN ##################################

############# EVENTOS
async def on_ready():
    await eventos.on_ready()



########## COMANDOS
async def ping():
    await comandos.ping()

async def informacion():
    await comandos.informacion()

async def eightball():
    await comandos.eightball()

async def pelicula():
    await comandos.pelicula()

async def latencia():
    await comandos.latencia()

async def mover():
    await comandos.mover()

async def rol():
    await comandos.rol()

async def sacarrol():
    await comandos.sacarrol()

################# RUN
comandos.bot.run('OTM4MjA5MjMzMDAwODgyMTg2.Yfm9cA.ANRwzPy6nHjeK7z1OBYokAb8rBI')
