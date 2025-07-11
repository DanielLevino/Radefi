import sys
from cx_Freeze import setup, Executable
from pygame import *
from pygame_functions import *

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Radefi.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["pygame"],
        include_files = [],
        excludes = []
)




setup(
    name = "Radefi",
    version = "1.00.01",
    description = "Software de questionário para Rápida Avaliação de Desempenho do Idoso",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
