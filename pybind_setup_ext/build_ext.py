from setuptools.command.build_ext import build_ext as __build_ext
from mypy.stubgen import stubgen
from os.path import abspath
import sys

def gen_stubs(m:str, o:str) -> None:
    stubgen([
        '-m', m,
        '-o', abspath(o), 
        '--inspect-mode',
        '--include-private',
    ])

class build_ext(__build_ext):
    def run(self) -> None:
        
        super().run()

        sys.path.insert(0, abspath(self.build_lib))

        for ext in self.extensions:

            gen_stubs(m=ext.name, o=self.build_lib)

            gen_stubs(m=ext.name, o='.')

