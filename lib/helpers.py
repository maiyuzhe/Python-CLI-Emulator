import time 
from time import sleep
import random
import subprocess
import sys

class Colors: 
    green = '\033[32m'
    white = '\033[37m'

def load_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    # print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='')
    # if iteration == total:
    #     print()
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')
    
items = list(range(0,50))
l = len(items)

for i, item in enumerate(items):
    sleep(0.1)
    load_bar(i + 1, l, prefix="Generating", suffix="Complete", length=l)

def blue_or_red():
    inp = input("Choose blue pill or red pill: ")
    if inp == "blue pill":
        blue_pill()
    elif inp == "red pill":
        red_pill()
    else:
        print("You must choose between the blue pill or the red pill")
    return blue_or_red

def blue_pill():
    print(Colors.green,"Reality is often disapointing. Now, reality can be whatever you want.")
    print("=========================================================================")
    time.sleep(1)
    print("Exiting Reality...")
    load_bar(0, l, prefix="Generating", suffix="Complete", length=l)
    for i, item in enumerate(items):
        sleep(0.1)
        load_bar(i + 1, l, prefix="Generating", suffix="Complete", length=l)
    time.sleep(1)
    print("Done: Reality Suspended.")
    time.sleep(1)
    print("Reconfiguring...")
    for i, item in enumerate(items):
        sleep(0.1)
        load_bar(i + 1, l, prefix="Generating", suffix="Complete", length=l)
    time.sleep(1.5)
    nums = [1,0]
    tm = 0
    while tm < 10:
        print(Colors.green, random.randrange(1,5)* "    ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),)
        tm = tm + 0.1
        time.sleep(0.01) 
    print("What did you lose?")
    time.sleep(.5)
    try:
        thanos_input = subprocess.run(["viu", "Assets/thanos.gif"], timeout=2)
        print("Simulation Loaded")
        print("=========================================================================")
        print("Bury your poor little head in the sand now, my sweet prince.")

    except: 
        while tm < 10:
            print(Colors.green, random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",                
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),random.randrange(1,5)* " ",
            random.choice(nums),)        
            nums = [1,0]
            tm = 0

def red_pill():
    print(Colors.green,"\nBold move, Cotton. Let's see if it pays off.")
    print("=========================================================================")
    time.sleep(1)
    print("Exiting Simulated Reality...")
    load_bar(0, l, prefix="Generating", suffix="Complete", length=l)
    for i, item in enumerate(items):
        sleep(0.1)
        load_bar(i + 1, l, prefix="Generating", suffix="Complete", length=l)
    time.sleep(1)
    print("Done: Simulated Reality Suspended.")
    print("=========================================================================")
    time.sleep(1)
    print("Reconfiguring...")
    load_bar(0, l, prefix="Generating", suffix="Complete", length=l)
    for i, item in enumerate(items):
        sleep(0.1)
        load_bar(i + 1, l, prefix="Generating", suffix="Complete", length=l)
    nums = [1,0]
    tm = 0
    time.sleep(1)
    while tm < 10:
        print(Colors.green, random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",                
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),)
        tm = tm + 0.1
        time.sleep(0.01)
    print("=========================================================================")
    print("Done: Base Reality Configured.")
    print("=========================================================================")
    print("Bye!")
    exit()

    