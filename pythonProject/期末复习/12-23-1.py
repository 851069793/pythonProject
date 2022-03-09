import random
from time import sleep

while 1:
    print({random.randint(0,8) for x in range(10)})
    sleep(5)