from cx_Freeze import setup, Executable

base = None    

executables = [Executable("generate_html.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "ECO HTML GENERATOR",
    options = options,
    version = "1.1",
    description = 'Exe to generate html file',
    executables = executables
)