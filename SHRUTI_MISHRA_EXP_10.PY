# import random and print the values between 1 to 10. and including 1 to 10

import random
# dont do head and tail and travel vlog
# do stone paper sissors

'''int_no=random.randint(1,10)
print(int_no)
'''
'''float_no=random.random()
print(float_no)'''

'''ht=random.randint(0,1)
if ht==0:
    print("Head")

else:
    print("Tails")

print(ht)'''

sps=random.randint(0,2)


stone="""         
                  -----
                ----------
                  ----- """

paper="""      
               ----------
               ----------
               ----------
                                    """

sissors="""
           --   
            -========
           --"""

user=int(input(""""
               0 ---> stone
               1 ---> paper
               2 ---> sissors
               Enter your input:
               """))

if user==0:
    print(stone)
elif user==1:
    print(paper)
elif user==2:
    print(sissors)
else:
    print("INVALID INPUT PLEASE SELECT THE CORRECT INPUT")



print("COMPUTER'S TURN")
if sps==0:
    print(stone)
elif sps==1:
    print(paper)
else:
    print(sissors)

if (user==0 and sps==0) or (user==1 and sps==1) or (user==2 and sps==2):
    result="TIE"
elif(user==0 and sps==1) or (user==1 and sps==2) or (user==2 and sps==0):
    result="COMPUTER WON , USER DEFEATED "
else:
    result="USER WON , COMPUTER DEFEATED "

print(result)
#print(sps)



