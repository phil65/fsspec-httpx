__version__ = "0.1.3"

from fsspec_httpx.filesystem import HTTPFileSystem, HttpPath


def register():
    from fsspec import register_implementation

    register_implementation("http", HTTPFileSystem)

    from upath import registry

    registry.register_implementation("http", HttpPath)


__all__ = ["HTTPFileSystem", "HttpPath", "register"]
