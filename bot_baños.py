# archivo: bot_banos.py
import os
from discord.ext import commands
from dotenv import load_dotenv
from gestion_banos import obtener_banos_disponibles

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configurar sectores y baños
sectores_baños = [
    ["Sector ED", ["Baño 1er piso(ED)", "Baño 2do piso(ED)"]],
    ["Sector EAO", ["Baño 1(EAO)", "Baño 2(EAO)"]],
    ["Sector Biblioteca Central", ["Baño Biblioteca Central"]],
    ["Sector Departamento de Física", ["Baño 1er piso(Dep.Física)", "Baño 2do piso(Dep.Física)"]],
]

# Inicializar bot
bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("¡Bot conectado como " + bot.user.name + "!")

@bot.command(name="baños")
async def banos_disponibles(ctx, *sectores_afectados):
    """
    Comando que devuelve los baños disponibles según los sectores afectados.
    """
    sectores_afectados = [sector.strip() for sector in sectores_afectados]
    afectados = [[sector, []] for sector in sectores_afectados if sector in [s[0] for s in sectores_baños]]
    baños_disponibles = obtener_banos_disponibles(afectados, sectores_baños)

    mensaje = ""
    for sector, baños in baños_disponibles:
        if "No hay baños disponibles" in baños:
            mensaje += sector + ": No hay baños disponibles.\n"
        else:
            mensaje += sector + ": " + ", ".join(baños) + "\n"
    
    await ctx.send(mensaje if mensaje else "No se encontraron sectores válidos.")

# Ejecutar bot
bot.run(TOKEN)
