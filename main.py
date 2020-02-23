'''
Created on 04.10.2019

@author: w4r10ck
'''
from argparse import ArgumentParser
from scanner import Scanner
from pygments.unistring import Sc


banner = '''
#     # #######  #####  #######  #####   #####  #       #     # #     # ####### ######  
#     # #     # #     #    #    #     # #     # #    #  ##    # ##    # #       #     # 
#     # #     # #          #    #       #       #    #  # #   # # #   # #       #     # 
####### #     #  #####     #     #####  #       #    #  #  #  # #  #  # #####   ######  
#     # #     #       #    #          # #       ####### #   # # #   # # #       #   #   
#     # #     # #     #    #    #     # #     #      #  #    ## #    ## #       #    #  
#     # #######  #####     #     #####   #####       #  #     # #     # ####### #     # 
'''

args = ArgumentParser(description='This network scanner scans for living host in your current network')
args.add_argument('-r', '--range', help='specify the range of addresses to scan DEFAULT: 100', action="store_true")
args.add_argument('-f', '--format', help="define the ip format which should be used", action="store_true")
args.add_argument('-s', '--start', help='define the start number of the ip address DEFAULT: 0', action='store_true')
print(banner)
print()
args.parse_args()
scanner = Scanner()
scanner.scan()
scanner.printRES()