from pybind11 import get_include
from typing import Literal
from sys import platform
from pathlib import Path
import setuptools as st
from glob import glob

#========================================================

_platforms = Literal['win32', 'linux', 'darwin']

#========================================================

_extra_compile_args: list[str]
if platform == "win32":
    _extra_compile_args = ["/std:c++20", "/EHsc"]
else:
    _extra_compile_args = ["-std=c++20", "-fvisibility=hidden"]

#========================================================

_extra_objects: list[str] = []

#========================================================

_include_dirs: list[str] = [
    get_include(),
    st.find_packages('.')[0],
]

#========================================================

class cpp_ext(st.Extension):

    def __init__(self,
        cpp_path: str|Path,
        *,
        platforms: list[_platforms] = ['win32', 'linux', 'darwin'],
        extra_objects: list[str] = [],
        include_dirs: list[str] = [],
        sources: list[str] = [],
        extra_link_args: list[str] = [],
    ) -> None:

        self.platforms = platforms

        if not isinstance(cpp_path, Path):
            cpp_path = Path(cpp_path)

        super().__init__(

            name = cpp_path.as_posix().rsplit('.', 1)[0].replace('/', '.'),

            sources = [cpp_path.as_posix()] + sources,

            extra_objects = [glob(pat) for pat in extra_objects] + _extra_objects,

            include_dirs = [cpp_path.parent.as_posix()] + include_dirs + _include_dirs,

            extra_compile_args = _extra_compile_args,
            extra_link_args = extra_link_args,
            language = 'c++',

        )

    def __bool__(self) -> bool:
        return platform in self.platforms

#========================================================

