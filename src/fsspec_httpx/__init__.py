__version__ = "0.1.3"

from fsspec_httpx.filesystem import HTTPFileSystem, HttpPath


def register(override: bool = True):
    from fsspec import register_implementation

    register_implementation("http", HTTPFileSystem, clobber=override)

    from upath import registry

    registry.register_implementation("http", HttpPath, clobber=override)


__all__ = ["HTTPFileSystem", "HttpPath", "register"]
