'''
Created on 17 cze 2018

@author: Mariusz Wincior
'''
from lcdbridge import LCDBridge

dut = LCDBridge()

dut.send2LCD(3, 1, "Dupa")