from setuptools.command.build_ext import build_ext as __build_ext
from os.path import abspath, join
from lfcrlf import convert_file
from os import environ, getcwd
from mypy import stubgen
import sys

def gen_stubs(m:str, o:str) -> None:

    environ["STUBGEN"] = "1"
    try:
        stubgen.generate_stubs(stubgen.parse_options([
            '-m', m,
            '-o', o, 
            '--inspect-mode',
            '--include-private',
        ]))
    finally:
        environ.pop("STUBGEN", None)
    
    if sys.platform != "win32":
        convert_file(
            join(o, m.replace('.', '/')+'.pyi'), 
            'crlf'
        )

class build_ext(__build_ext):
    def run(self) -> None:
        
        super().run()

        build_lib: str = abspath(self.build_lib)
        sys.path.insert(0, build_lib)

        for ext in self.extensions:

            gen_stubs(m=ext.name, o=build_lib)

            gen_stubs(m=ext.name, o=getcwd())

