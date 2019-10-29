
from time import sleep, time
from threading import *

print('Start Time: ', time())


def fun1(name=None):
    for i in range(10):
        print('Name = ', name)
        sleep(1)


def main():
    fun1('lokesh')
    print('**********')
    fun1('Sndhu')


main()
print("stop TIme: ", time())

