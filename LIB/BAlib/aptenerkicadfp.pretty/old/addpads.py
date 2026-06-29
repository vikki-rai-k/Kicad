import os
import sys
from subprocess import call
fname = input("enter the file name (in double qoute) : ")
pad=input("enter the first pad no = ")
padn = input("enter the second pad no =")
padl = input("enter the last pad no =")
posx = input("enter the xposision of first pin = ")
posy = input("enter the y_possision of first pin = ")
sizex = input("enter the x_size  = ")
sizey = input("enter the y_size = ")
xdiiff = input("enter the x differnece between each pad = ")
ydiff = input("enter the x differnece between each pad = ")
diff = padn-pad
while padn <= padl:
        print("pad= " ,pad)
        print("padn= ",padn)
        posx = posx + xdiiff
        posy = posy + ydiff
        call(['sh' ,'addpads.sh',str(pad),str(padn),str(posx),str(posy),str(sizex),str(sizey),fname])
        #call(['sed' ,'-i', "/pad $1 smd/a pad $2 rect (at -1.2 -2.4) (size 0.75 0.35) (layers F.Cu F.Paste F.Mask))", 'MAX30101.kicad_mod'])
        pad = padn
        padn= pad + diff
