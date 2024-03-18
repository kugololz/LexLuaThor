from cx_Freeze import setup, Executable

setup(

       name="LexLuaThor",

       version="1.0",

       description="Lua lexer made in Python by JE",

       executables=[Executable("gui.py")],

   )   