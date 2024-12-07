from urllib.request import urlretrieve
from py7zr import SevenZipFile
from os import remove

url = "https://github.com/Wyxemon/MinecraftLauncher.github.io/raw/main/Minecraft%20Launcher.7z"
archivo_destino = "Minecraft_Launcher.7z"

print("Instalado...")

# Descarga el archivo .7z
urlretrieve(url, archivo_destino)
print("Instalado :)")

# Directorio donde deseas extraer los archivos
destino_directorio = "update/"

# Descomprimir el archivo .7z
with SevenZipFile(archivo_destino, mode='r') as zip:
    zip.extractall(path=destino_directorio)

remove("Minecraft_Launcher.7z")
