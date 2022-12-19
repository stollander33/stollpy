from importlib.metadata import version

__version__ = version("stollpy")
del version

__all__ = ["__version__"]
