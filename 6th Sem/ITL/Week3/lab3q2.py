#!/usr/bin/python -tt
import sys
a = 123
def fileRev(filename):
     print (filename, '=======')
     f1 = open(filename, 'r')
     data = f1.read()
     f2 = open("saveFile.txt",'w')
     data = data[::-1]
     f2.write(data)
     f1.close()
     f2.close()

def main():
    args = sys.argv[1:]

    for filename in args:
        fileRev(filename)
        print ('all done')

if __name__ == '__main__':
 main()