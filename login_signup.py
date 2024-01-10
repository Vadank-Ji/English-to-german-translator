import mysql.connector
import maskpass
myDB=mysql.connector.connect(host="localhost",user="root",passwd="Vadu",database="csproject")

myCursor=myDB.cursor()
print("login or signup,")
c=int(input("Enter 1 for login and 2 for signup:"))

def NUM():
    myCursor.execute("select * from users;")
    records=myCursor.fetchall()
    n=[]
    for i in records:
        n.append(i[0])
    if n!=[]:
        return max(n)+1
    else:
        return 1
#print(NUM())
def main():
    global valid
    valid=False
    if c==1:
        N=input("Enter your customer ID:")
        userName=input("Enter your UserName:")
        pwd=maskpass.askpass(mask="*")
        myCursor.execute(f"select * from users where UNo={N}")
        records=myCursor.fetchall()
        print(records[0][1])
        if userName in records[0][3:5] and pwd in records[0][3:5]:
            valid=True
        print(valid)
    if c==2:
        FN=input("Enter your first name:")
        LN=input("Enter your last name:")
        UN=input("Enter your username:")
        PW=input("Enter your pasword:")
        NUM()
        #k="insert into UserDetails values(\""+NUM()+","+FN+","+LN+","+UN+","+PW+"\")"
        #k="insert into UserDetails values(4,\"fda\",\"fda\",\"da\",\"da\")"
        print("Ur Customer ID is",NUM())
        myCursor.execute(f"insert into users values({NUM()},\"{FN}\",\"{LN}\",\"{UN}\",\"{PW}\")")

    myDB.commit()
