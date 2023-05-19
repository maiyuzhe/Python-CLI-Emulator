import time 
import random
import subprocess

class Colors: 
    green = '\033[32m'
    white = '\033[37m'

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
    print("=========================================================================")
    time.sleep(1)
    print("Done: Reality Suspended.")
    print("=========================================================================")
    time.sleep(1)
    print("Reconfiguring...")
    print("=========================================================================")
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
    time.sleep(1)
    try:
        thanos_input = subprocess.run(["viu", "Assets/thanos.gif"], timeout=2)
        print("Simulation Loaded")
        print("=========================================================================")
        print("Bury your poor little head in the sand now, my sweet prince.")
        print("=========================================================================")
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
    print("=========================================================================")
    time.sleep(1)
    print("Done: Simulated Reality Suspended.")
    print("=========================================================================")
    time.sleep(1)
    print("Reconfiguring...")
    print("=========================================================================")
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