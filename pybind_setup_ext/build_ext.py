from setuptools2.command.build_ext import build_ext as __build_ext
from os.path import abspath
from os import getcwd
import sys

class build_ext(__build_ext):
    def run(self) -> None:
        
        super().run()

        sys.path.insert(0, abspath(self.build_lib))

        for ext in self.extensions:
            ext._stubgen(getcwd())

