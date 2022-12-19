import subprocess
import sys

from stollpy import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "stollpy", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
