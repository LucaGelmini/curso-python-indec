import subprocess

commands = [
   "conda create -n mi-entorno pip ipykernel",
   "conda activate mi-entorno",
   "pip install pandas",
   "pip install plotly",
   "pip install xlrd",
   "pip install nbformat"
]

# Concatenar todos los comandos en una sola cadena
command_string = " && ".join(commands)

# Ejecutar todos los comandos en un solo proceso
process = subprocess.Popen(command_string, shell=True)
process.wait()
    
#pyinstaller --onefile instalacion_entorno.py