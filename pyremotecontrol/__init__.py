# Version 1.0
# Status: Stable

__VERSION__ = "1.0"

from platform import system

if system().lower() == "windows":
    from pyremotecontrol.remotecontrol import start_server
