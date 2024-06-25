import sys
import os
import subprocess


def assemble (name):
    command = ('as -o %s.o %s.s' % (name, name))
    os.system(command)

def link (name):
    command = ('clang -o %s %s.o -Wl,-e,_start -lc' % (name, name)  )  
    os.system(command)


def main ():
        argu=0
        try:
            argu = sys.argv[1]
        except Exception as e:
            print("there is no file to be compiled.")
            return 0
        file = argu.split('.')
        assemble(file[0])
        link(file[0])

main()
