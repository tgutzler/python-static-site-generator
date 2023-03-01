from pathlib import Path
from os import makedirs
from os import path as pth


class Site:
    def __init__(self, source, dest):
        self._source = Path(source)
        self._dest = Path(dest)

    def create_dir(self, path):
        directory = pth.join(self._dest, path.relative_to(self._source))
        makedirs(directory, exist_ok=True)

    def build(self):
        makedirs(self._dest, exist_ok=True)
        for path in self._source.rglob("*"):
            if Path(path).is_dir():
                self.create_dir(path)

