import time 
import random as rd
import msvcrt as ms

r=rd.randrange(2,8)
a="y"
while a=="y" or a=="Y":
    print("\nWhen you see 'GO!', press ENTER as fast as you can.")
    input("press ENTER to start")

    time.sleep(1)
    print("\nwait...")

    time.sleep(r)
    if ms.kbhit():
        print("\ntoo early, you are disqualified")
        
    else:
        print("\nGO!!!")

        t1=time.time()
        input()
        t2=time.time()

        result=t2-t1
        print(f"your reaction time: {result:.4f}")
        
    print("-"*30)
    a=input("would you like to play again ? (y/n) ")
     