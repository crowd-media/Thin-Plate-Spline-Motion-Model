

import os
import sys

# print("run init in thin_plate")

## add current dir to sys path so that root dbpn py files can be imported from outside 
current_dir = os.path.dirname( __file__ )
sys.path.append( current_dir )




def print_version():
    print('THINPLATE VERSION 0.1.0')
