#Language translator
#TBT=To Be Traslated



pronouns={'I':'Ich','you':'du','he':'er','she':'sie','it':'es','we':'wir','this':'dieser',
'these':'diese', 'that':'dieses','more':'mehr','nothing':'nichts','none':'nichts'}

def pro():
    p=TBT1[i]
    if TBT1[i].islower():
        TBT1[i]=pronouns[p]

    elif TBT1[i][0].isupper() and TBT1[i] !='I':
        TBT1[i]
        TBT1[i]=pronouns[p.lower()].capitalize()
    else:
        TBT1[i]=pronouns['I']

objects={'dog':'das hund','time':'die Ziet','example':'das Biespiel','year':'das Jahr','morning':'der Morgen', 'one':'man','hello':'hallo'}

def obj():
    o=TBT1[i]
    if TBT1[i].islower():
        TBT1[i]=objects[o]

    elif TBT1[i][0].isupper():

        TBT1[i]=objects[o.lower()].capitalize()


    elif TBT1[i]=='morning':
        TBT1[i]=objects[o]

    elif TBT1[i]=='Morning':
        TBT1[i]=objects['morning'].capitalize()


adjectives={'long':'lang','new':'neu','old':'alt','many':'viel','a lot':'viel','many':'viel',
'small':'klein','whole':'ganz','complete':'ganz','entire':'ganz','big':'groß'}

def adj():
    a=TBT1[i]
    if TBT1[i].islower():
        TBT1[i]=adjectives[a]

    if TBT1[i][0].isupper():
        TBT1[i]=adjectives[a.lower()].capitalize()
    print("hello3")
qWords={'how':'wie','where':'wo','what':'what'}

def qW():
    q=TBT1[i]
    if TBT1[i].islower():
        TBT1[i]=objects[q]

    elif TBT1[i][0].isupper():
        TBT1[i]=objects[q.lower()].capitalize()

verbs={'to give':'gaben','say':'sagen','come':'kommen','want':'wollen','allow':'lassen','let':'lassen','know':'wissen',
'go':'gehen','have':'haben','see':'sehen','make':'machen','be':'sein','become':'werden','am':'bin'}

def ver():
    v=TBT1[i]
    if TBT1[i].islower():
        TBT1[i]=verbs[v]

    elif TBT1[i][0].isupper():
        TBT1[i]=verbs[v.lower()].capitalize()

print("-------------------------------------------------------")  
print("_______________________________________________________")
print("**         **")
print(" **       **")
print("  **  ** ** ")
print("   **   **  ",end=' ')
print("elcome to the German to English Translator")
print("*********************************************************")

import login_signup
n=1
while n>0:
    login_signup.main()
    if login_signup.valid==True or login_signup.c==2:
        n=1
        choice=input("What do you want to do\n1.convert english to german or\n2.help make our small dictionary of translations better\n3.Exit>>>")

        if choice=="1":
            TBT=input("Write the text that is too be translated into german:")
            TBT1=TBT.split()


            for i in range(0,len(TBT1)):

                if TBT1[i]=='German':
                    TBT1[i]='Deutsch'
                    #print(1)

                elif TBT1[i]=='Germany':
                    TBT1[i]='Deutchland'
                    #print(2)

                elif TBT1[i] in pronouns or TBT1[i].lower() in pronouns:
                    pro()
                    #print(3)

                elif TBT1[i-1]=='good' or TBT1[i-1][0].isupper() and TBT1[i]=='morning':
                    TBT1[i-1]='guten'
                    TBT1[i]='morgen'
                    #print(4)

                elif TBT1[i] in objects or TBT1[i].lower() in objects:
                    obj()
                    #print(5)

                elif TBT1[i] in adjectives or TBT1[i].lower() in adjectives:
                    adj()
                    #print(6)

                elif TBT1[i] in verbs or TBT1[i].lower() in verbs:
                    ver()
                    #print(7)

            n=n-1
            k=""
            for i2 in TBT1:
                k=k+i2+' '
            print(k)

        elif choice=="2":
            print("At this moment we have these words (please do not repeat the same word from our dictionary:{pronouns,object,adjectives,verbs,qWords}")
            print("Kindly add words which will be directly filled in a document, and please mail it to the email:ABC@gmail.com")

            num=int(input("Number of English words and the translation to German which are to be added:"))

            k=open('words.txt','w')
            k.write("German Dictionary:\n")

            for i1 in range(0,num):
                ele=input(f"Pair of English word and translation {i1+1}:\n")
                k.write(f"{i1+1}.{ele}\n")
            n=n-1
        
        elif choice==3:
            break
        else:
            print("Please enter again")
            n=1
    else:
        print("Please Enter again:")