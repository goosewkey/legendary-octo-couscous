import Nuker
from Misc import *

token = Nuker.tokefunc()
idkunused.gettoki(token)
heyguys()
pokiii()
feke()

import os
import time
import threading

def clear_cmd():
    while True:
        time.sleep(60)
        os.system("cls" if os.name == "nt" else "clear")
threading.Thread(target=clear_cmd, daemon=True).start() 
