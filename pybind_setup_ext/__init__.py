
from .git import update_submodule
from .build_ext import build_ext
from .cpp_ext import cpp_ext
import setuptools as st

__all__ = ["cpp_ext", "setup", "update_submodule"]

def setup(*ext_modules:cpp_ext) -> None:
    st.setup(
        cmdclass = {'build_ext': build_ext},
        ext_modules = list(filter(None, ext_modules)),
    )

