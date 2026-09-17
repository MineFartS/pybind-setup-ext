from pybind11 import get_include
from copy import deepcopy
from sys import platform
from pathlib import Path
import setuptools as st
from glob import glob

_kw_templ = {

    'include_dirs': [
        get_include(),
    ],

    'language': 'c++',

}

if platform == "win32":
    _kw_templ['extra_compile_args'] = ["/std:c++20", "/EHsc"]
else:
    _kw_templ['extra_compile_args'] = ["-std=c++20", "-fvisibility=hidden"]

class cpp_ext(st.Extension):

    def __init__(self,
        cpp_path: str|Path,
        extra_objects: str = None,
        include_dirs: list[str] = [],
        sources: list[str] = [],
    ) -> None:

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

        if extra_objects is not None:
            _kw['extra_objects'] = glob(extra_objects)

        super().__init__(**_kw)

