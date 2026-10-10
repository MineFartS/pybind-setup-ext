
from .git import update_submodule
from .build_ext import build_ext
from .cpp_ext import cpp_ext
import setuptools as st

from .cpp_ext import (
    _extra_compile_args as extra_compile_args,
    _extra_objects as extra_objects,
    _include_dirs as include_dirs,
)

__all__ = [
    "cpp_ext", "setup", "update_submodule", 
    "extra_compile_args", "extra_objects", "include_dirs",
]

def setup(*ext_modules:cpp_ext) -> None:
    st.setup(
        cmdclass = {'build_ext': build_ext},
        ext_modules = list(filter(None, ext_modules)),
    )

