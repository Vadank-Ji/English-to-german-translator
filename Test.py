
n=1
import login_signup
while n>0:
    if login_signup.valid==True or c==1:

        n=1
        choice=input("What do you want to do\n1.convert english to german or\n2.help make our small dictionary of translations better\n>>>" )

        if choice=="1":
            TBT=input("Write the text that is too be translated into german:")
            TBT1=TBT.split()
