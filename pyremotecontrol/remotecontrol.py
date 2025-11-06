import logging
import sys
import threading
import pyautogui
from flask import Flask, request

cli = sys.modules["flask.cli"]

app = Flask("app")

pyautogui.FAILSAFE = False
moving = False
drag = False
type_data = ""
old_data = ""
coords = (0, 0)
lastcords = (0, 0)
lstmcord = (0, 0)
lstlen = 0
coords = [(0, 0)]