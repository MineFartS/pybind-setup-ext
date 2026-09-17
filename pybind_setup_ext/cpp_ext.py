from pybind11 import get_include
from typing import Literal
from copy import deepcopy
from sys import platform
from pathlib import Path
import setuptools as st
from glob import glob

_plats = Literal['win32', 'linux', 'darwin']

_kw_templ = {

    'include_dirs': [
        get_include(),
    ],

    "extra_objects": [],

    'language': 'c++',

}

if platform == "win32":
    _kw_templ['extra_compile_args'] = ["/std:c++20", "/EHsc"]
else:
    _kw_templ['extra_compile_args'] = ["-std=c++20", "-fvisibility=hidden"]

class cpp_ext(st.Extension):

    def __init__(self,
        cpp_path: str|Path,
        *,
        platforms: list[_plats] = ['win32', 'linux', 'darwin'],
        extra_objects: list[str] = [],
        include_dirs: list[str] = [],
        sources: list[str] = [],
    ) -> None:

        self.platforms = platforms

        if not isinstance(cpp_path, Path):
            cpp_path = Path(cpp_path)

        _kw = deepcopy(_kw_templ)

        _kw['name'] = cpp_path.as_posix().rsplit('.', 1)[0].replace('/', '.')

        _kw['sources'] = [
            cpp_path.as_posix(),
            *sources
        ]

        _kw['include_dirs'] += [
            cpp_path.parent.as_posix(),
            *include_dirs,
        ]

        for pattern in extra_objects:
            _kw['extra_objects'] += glob(pattern)

        super().__init__(**_kw)

    def __bool__(self) -> bool:
        return platform in self.platforms

