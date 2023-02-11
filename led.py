'''
Struttura esempio programma scritto in Python
E' un file di esempio
'''

import time
import random

def setup():
    time.sleep(1)
    print('Fase setup...')
    time.sleep(1)

def loop():
    while True:
        t = random.randint(1, 10)
        print(t, 'secondi di attesa...')
        time.sleep(t)
        print('Fase loop...')
        time.sleep(1)

def destroy():
    time.sleep(1)
    print('Fase destroy...')
    time.sleep(1)

if __name__ == '__main__':
    setup()
    print('Program is starting... \n')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()