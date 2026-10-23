from setuptools.command.build_ext import build_ext as __build_ext
from os.path import abspath
from mypy import stubgen
from os import environ
import sys

def gen_stubs(m:str, o:str) -> None:
    environ["STUBGEN"] = "1"
    try:
        stubgen.generate_stubs(stubgen.parse_options([
            '-m', m,
            '-o', abspath(o), 
            '--inspect-mode',
            '--include-private',
        ]))
    finally:
        environ.pop("STUBGEN", None)

class build_ext(__build_ext):
    def run(self) -> None:
        
        super().run()

        sys.path.insert(0, abspath(self.build_lib))

        for ext in self.extensions:

            gen_stubs(m=ext.name, o=self.build_lib)

            gen_stubs(m=ext.name, o='.')

