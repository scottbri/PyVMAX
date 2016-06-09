import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import pyvmax

# this obviously won't work... just testing
vmax_api = pyvmax.connect('url', 'user', 'pass')

