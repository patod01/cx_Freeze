"""
Module for the VersionInfo base class.
"""

from pathlib import Path
from typing import Optional, Union

try:
    from win32verstamp import stamp as version_stamp
except ImportError:
    version_stamp = None

__all__ = ["VersionInfo"]


class VersionInfo:
    def __init__(
        self,
        version: str,
        internal_name: Optional[str] = None,
        original_filename: Optional[str] = None,
        comments: Optional[str] = None,
        company: Optional[str] = None,
        description: Optional[str] = None,
        copyright: Optional[str] = None,
        trademarks: Optional[str] = None,
        product: Optional[str] = None,
        dll: Optional[bool] = None,
        debug: Optional[bool] = None,
        verbose: bool = True,
    ):
        parts = version.split(".")
        while len(parts) < 4:
            parts.append("0")
        self.version: str = ".".join(parts)
        self.internal_name: Optional[str] = internal_name
        self.original_filename: Optional[str] = original_filename
        self.comments: Optional[str] = comments
        self.company: Optional[str] = company
        self.description: Optional[str] = description
        self.copyright: Optional[str] = copyright
        self.trademarks: Optional[str] = trademarks
        self.product: Optional[str] = product
        self.dll: Optional[bool] = dll
        self.debug: Optional[bool] = debug
        self.verbose: bool = verbose

    def stamp(self, path: Union[str, Path]):
        if isinstance(path, str):
            path = Path(path)
        if not path.is_file():
            raise FileNotFoundError(path)
        if version_stamp is None:
            raise RuntimeError("install pywin32 extensions first")

        version_stamp(str(path), self)
