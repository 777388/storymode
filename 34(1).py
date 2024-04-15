import hermes
import dataclasses
import inflect
import os
try:
    inflect.Field.__init__(dataclasses.astuple(hermes))
except:
    os.popen("python3 brickhouse.py").read()
    os.popen("python3 wac.py").read()