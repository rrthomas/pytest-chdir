import importlib.metadata

from .plugin import define_chdir_fixture

try:
    __version__ = importlib.metadata.version("pytest-chdir")
except importlib.metadata.PackageNotFoundError:
    __version__ = "develop"
