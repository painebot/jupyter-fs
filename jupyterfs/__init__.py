# *****************************************************************************
#
# Copyright (c) 2019, the jupyter-fs authors.
#
# This file is part of the jupyter-fs library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import json
from contextlib import contextmanager
from pathlib import Path

from .extension import _jupyter_server_extension_points

__version__ = "1.0.1"

HERE = Path(__file__).parent.resolve()
with (HERE / "labextension" / "package.json").open() as fid:
    data = json.load(fid)


def open_fs(fs_url, type="pyfs", **kwargs):
    """Wrapper around fs.open_fs with {{variable}} substitution"""
    from .auth import stdin_prompt

    # substitute credential variables via `getpass` queries
    fs_url = stdin_prompt(fs_url)

    if type == "fsspec":
        import fsspec

        @contextmanager
        def _open_fs(fs_url, **kwargs):
            yield fsspec.core.url_to_fs(fs_url, **kwargs)[0]

        return _open_fs(fs_url, **kwargs)
    else:
        import fs

        # substitute credential variables via `getpass` queries
        return fs.open_fs(fs_url, **kwargs)


def _jupyter_labextension_paths():
    return [
        {
            "src": "labextension",
            "dest": data["name"],
        }
    ]
