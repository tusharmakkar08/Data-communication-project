import sys
from termcolor import colored,cprint
def add(m,n):
    i=len(m)-1;k=[]
    c=0
    while (i>=0):
        l=int(m[i])^int(n[i])^c
        k.append(str(l))
        c=(int(m[i])&int(n[i]))|(int(n[i])&c)|(int(m[i])&c)
        i=i-1
    koi="".join(k[::-1])
    if c==1:
        mint='1'.zfill(len(koi))
        add(mint,koi)
    return koi
def comp(k):
    toi=""
    for i in k:
        if i=='1':
            toi+="0"
        else:
            toi+="1"
    return toi
cprint("\t\tWelcome to TM Error Detection,Control and Time Division Multiplexing System!", 'red', attrs=['bold','underline'], file=sys.stderr)
while 1:
    print colored("Enter input:",'cyan')
    print colored("1. For Error Detection ",'red')
    print colored("2. For Error Correction ",'red')
    print colored("3. For Time Division multiplexing ",'red')
    print colored("4. For Block Coding ",'red')
    print colored("5. Exit ",'red')
    foo=input()
    if foo==1:
        cprint("\n\t\tWelcome to TM Error Detection Module!", 'red', attrs=['bold','underline'], file=sys.stderr)
        print colored("Enter input:",'cyan')
        print colored("1. For Parity Check ",'red')
        print colored("2. For 2-Dimensional Parity Check ",'red')
        print colored("3. Checksum ",'red')
        print colored("4. Exit ",'red')
        tus=input()
        if tus==1:
            cprint("\n\t\tWelcome to TM Parity Check Module!", 'red', attrs=['bold','underline'], file=sys.stderr)
            while 1:
                print colored("Enter input:",'cyan')
                print colored("1. In Decimal numbers ",'red')
                print colored("2. In Binary numbers ",'red')            
                koi=input()
                if koi==1:#for decimal numbers
                    loi=input("Enter the sent number\n")
                    k=bin(loi)[2:].zfill(8)
                    cprint(k,'yellow','on_blue',end=" ")
                    cprint("is the input number in binary form",'yellow','on_blue')
                    loi1=input("Enter the recieved number\n")
                    k1=bin(loi1)[2:].zfill(8)
                    cprint(k1,'yellow','on_blue',end=" ")
                    cprint("is the input number in binary form",'yellow','on_blue')
                    count00=0;count10=0
                    for i in k: #Checking number of 1's and 0's
                        if i=='1':
                            count10+=1
                        else:
                            count00+=1
                    count11=0;count01=0
                    for i in k1:
                        if i=='1':
                            count11+=1
                        else:
                            count01+=1
                    if count11==count10 and count00==count01: # Condition for parity check
                        cprint("Error Not found","green",attrs=['dark'],file=sys.stderr)
                        if k==k1:
                            cprint("Method was Successfull","yellow",attrs=['blink'],file=sys.stderr)
                        else:
                            cprint("Method was Unsuccessfull","red",attrs=['blink'],file=sys.stderr)
                    else:
                        cprint("Error found","green",attrs=['dark'],file=sys.stderr)
                        if k!=k1:
                            cprint("Method was Successfull","yellow",attrs=['blink'],file=sys.stderr)
                        else:
                            cprint("Method was Unsuccessfull","red",attrs=['blink'],file=sys.stderr)                        
                    break
                elif koi==2:# for binary numbers
                    k=raw_input("Enter the sent number\n")
                    cprint(k,'yellow','on_blue',end=" ")
                    cprint("is the input number in binary form",'yellow','on_blue')
                    k1=raw_input("Enter the recieved number\n")
                    cprint(k1,'yellow','on_blue',end=" ")
                    cprint("is the input number in binary form",'yellow','on_blue')
                    count00=0;count10=0
                    for i in k:
                        if i=='1':
                            count10+=1
                        else:
                            count00+=1
                    count11=0;count01=0
                    for i in k1:
                        if i=='1':
                            count11+=1
                        else:
                            count01+=1
                    if count11==count10 and count00==count01:
                        cprint("Error Not found","green",attrs=['dark'],file=sys.stderr)
                        if k==k1:
                            cprint("Method was Successfull","yellow",attrs=['blink'],file=sys.stderr)
                        else:
                            cprint("Method was Unsuccessfull","red",attrs=['blink'],file=sys.stderr)
                    else:
                        cprint("Error found","green",attrs=['dark'],file=sys.stderr)
                        if k!=k1:
                            cprint("Method was Successfull","yellow",attrs=['blink'],file=sys.stderr)
                        else:
                            cprint("Method was Unsuccessfull","red",attrs=['blink'],file=sys.stderr)                        
                    break
                else:
                    cprint("Invalid Option!", 'green', attrs=['bold','underline'], file=sys.stderr)
        elif tus==2:
            cprint("\n\t\tWelcome to TM 2D Parity Check Module!", 'red', attrs=['bold','underline'], file=sys.stderr)
            while 1:
                print colored("Enter no of inputs :",'cyan')      
                n=input()
                print colored("Enter sent inputs :",'cyan');l=[]
                for i in xrange(n):
                    l.append(raw_input(""))
                m=[]
                for i in l:
                    count1=0;count0=0
                    for j in i:
                        if j=='0':
                            count0+=1
                        else:
                            count1+=1
                    if count1%2==0:
                        kim='0'
                    else:
                        kim='1'
                    i+=" "
                    i+=kim
                    m.append(i)
                m.append("");lol=""
                for j in xrange(len(l[1])):
                    count1=0
                    for i in l:
                        if i[j]=='1':
                            count1+=1
                    if count1%2==0:
                        lol+="0"
                    else:
                        lol+="1"
                lol+=" ";cou=0
                for j in lol:
                    if j=='1':
                        cou+=1
                if cou%2==0:
                    lol+="0"
                else:
                    lol+="1"
                m.append(lol) #m is the new array for first
                cprint("New array", 'green', attrs=['bold','underline'], file=sys.stderr)
                for i in m:
                    cprint(i,"cyan",attrs=['bold'],file=sys.stderr)
                print colored("Enter recieved inputs :",'cyan');l=[]
                for i in xrange(n):
                    l.append(raw_input(""))
                m1=[]
                for i in l:
                    count1=0;count0=0
                    for j in i:
                        if j=='0':
                            count0+=1
                        else:
                            count1+=1
                    if count1%2==0:
                        kim='0'
                    else:
                        kim='1'
                    i+=" "
                    i+=kim
                    m1.append(i)    #m1 is the new array for 2nd lol is the last line for first and lol1 is the last line for second
                m1.append("");lol1=""
                for j in xrange(len(l[1])):
                    count1=0
                    for i in l:
                        if i[j]=='1':
                            count1+=1
                    if count1%2==0:
                        lol1+="0"
                    else:
                        lol1+="1"
                lol1+=" ";cou=0
                for j in lol1:
                    if j=='1':
                        cou+=1
                if cou%2==0:
                    lol1+="0"
                else:
                    lol1+="1"
                m1.append(lol1)
                cprint("New array", 'green', attrs=['bold','underline'], file=sys.stderr)
                for i in m1:
                    cprint(i,"cyan",attrs=['bold'],file=sys.stderr)
                kit=len(m1[0])-1;flag=0
                if lol==lol1:   #condition checking for 2 d parity checking
                    for i in xrange(len(m1)):
                        if len(m1[i])<=kit:
                            continue
                        else:
                            if m1[i][kit]!=m[i][kit]:
                                cprint("Error found","green",attrs=['dark'],file=sys.stderr)
                                cprint("Method was Successfull","yellow",attrs=['blink'],file=sys.stderr)
                                flag=1
                                break
                    flag1=0
                    if flag==0:
                        cprint("Error Not found","green",attrs=['dark'],file=sys.stderr)
                        for i in xrange(len(m)):
                            if m[i]!=m1[i]:
                                cprint("Method was Unsuccessfull","red",attrs=['blink'],file=sys.stderr);flag1=1
                                break
                        if flag1==0:
                            cprint("Method was Successfull","yellow",attrs=['blink'],file=sys.stderr)
                else:
                    cprint("Error found","green",attrs=['dark'],file=sys.stderr)
                    cprint("Method was Successfull","yellow",attrs=['blink'],file=sys.stderr)
                break
        elif tus==3:
            cprint("\n\t\tWelcome to TM Checksum Error Detection Module!", 'red', attrs=['bold','underline'], file=sys.stderr)
            while 1:
                print colored("Enter no of inputs :",'cyan')      
                n=input()
                print colored("Enter sent inputs :",'cyan');l=[]
                for i in xrange(n):
                    l.append(raw_input(""))
                k="".zfill(len(l[0]))
                for i in l: # Finding addition
                    s=add(k,i)
                    k=s
                moi=comp(k) # finding compliment
                cprint ("Checksum for sent signals is",'red','on_blue',attrs=['bold'])
                cprint(moi,"cyan",attrs=['bold'],file=sys.stderr)
                print colored("Enter recieved inputs :",'cyan');lo=[]
                for i in xrange(n):
                    lo.append(raw_input(""))
                k="".zfill(len(l[0]))
                for i in lo: # Finding addition
                    s=add(k,i)
                    k=s
                moi1=comp(k) # finding compliment
                cprint ("Checksum for recieved signals is",'red','on_blue',attrs=['bold'])
                cprint(moi1,"cyan",attrs=['bold'],file=sys.stderr)
                if moi==moi1:   # Checksum method evaluation
                    cprint("Error Not found","green",attrs=['dark','bold'],file=sys.stderr);flag1=0
                    for i in xrange(len(l)):
                        if l[i]!=lo[i]:
                            cprint("Method was Unsuccessfull","red",'on_grey',attrs=['dark'],file=sys.stderr);flag1=1
                            break
                    if flag1==0:
                        cprint("Method was Successfull","red",attrs=['bold','underline'],file=sys.stderr)
                else:
                    cprint("Error found","green",'on_red',attrs=['dark'],file=sys.stderr)
                    cprint("Method was Successfull","red",attrs=['bold','underline'],file=sys.stderr)
                break
        elif tus==4:
            cprint("Thank You for using TM Error Detection and Control System!", 'yellow', attrs=['bold','underline'], file=sys.stderr)
            break
        else:
            cprint("Invalid Option--- Taking back to home page", 'green', attrs=['bold','underline'], file=sys.stderr)
    elif foo==2:
        cprint("\n\t\tWelcome to TM Hamming code Module!", 'red', attrs=['bold','underline'], file=sys.stderr)
        print colored("Enter input of 8 bit :",'cyan')
        k=raw_input("")
        print colored("The input taken is :",'red');t="";count=0;moi="";p="0";q="0";r="0";s="0"
        for i in k:
            count+=1
            if count==1:
                t+="p"
                count+=1
                flag=1
            if count==2:
                t+="q"
                count+=1
                flag=1
            if count==4:
                t+="r"
                count+=1
                flag=1
            if count==8:
                t+="s"
                count+=1
                flag=1
            t+=i
        cprint(t,"cyan",attrs=['bold'],file=sys.stderr);cp=0;cq=0;cr=0;cs=0
        if t[2]=="1" :
            cp+=1
            cq+=1
        if t[4]=="1":
            cp+=1
            cr+=1
        if t[6]=="1":
            cp+=1
            cq+=1
            cr+=1
        if t[8]=="1":
            cp+=1
            cs+=1
        if t[10]=="1":
            cp+=1
            cq+=1
            cs+=1
        if t[5]=="1":
            cq+=1
            cr+=1
        if t[9]=="1":
            cq+=1
            cs+=1
        if t[11]=="1":
            cr+=1
            cs+=1
        count=0
        for i in k:
            if cp%2==1 and count==0:
                moi+="1"
            elif cp%2==0 and count==0:
                moi+="0"
            if cq%2==1 and count==0:
                moi+="1"
            elif cq%2==0 and count==0:
                moi+="0"
            if cr%2==1 and count==2:
                moi+="1"
            if cr%2==0 and count==2:
                moi+="0"
            if cs%2==1 and count==6:
                moi+="1"
            if cs%2==0 and count==6:
                moi+="0"
            count+=1
            moi+=i
        cprint("New input with redundancy bits","green",'on_red',attrs=['dark'],file=sys.stderr)
        cprint(moi,"cyan",attrs=['bold'],file=sys.stderr);t=""
        t=raw_input("Enter the recieved signal\n")
        cp=0;cq=0;cr=0;cs=0
        if t[0]=="1":
            cp+=1
        if t[1]=="1":
            cq+=1
        if t[3]=="1":
            cr+=1
        if t[7]=="1":
            cs+=1
        if t[2]=="1" :
            cp+=1
            cq+=1
        if t[4]=="1":
            cp+=1
            cr+=1
        if t[6]=="1":
            cp+=1
            cq+=1
            cr+=1
        if t[8]=="1":
            cp+=1
            cs+=1
        if t[10]=="1":
            cp+=1
            cq+=1
            cs+=1
        if t[5]=="1":
            cq+=1
            cr+=1
        if t[9]=="1":
            cq+=1
            cs+=1
        if t[11]=="1":
            cr+=1
            cs+=1
        soi=""
        if cp%2==1:
            flag=3
            soi+="1"
        else:
            soi+="0"
        if cq%2==1:
            flag=3
            soi+="1"
        else:
            soi+="0"
        if cr%2==1:
            flag=3
            soi+="1"
        else:
            soi+="0"
        if cs%2==1:
            flag=3
            soi+="1"
        else:
            soi+="0"
        if flag==3:
            cprint("Error found at","green",'on_red',attrs=['dark'],file=sys.stderr);cprint(int(soi[::-1],2),"cyan",attrs=['bold'],file=sys.stderr)
        else:
            cprint("No Error found","green",'on_yellow',attrs=['dark'],file=sys.stderr)
    elif foo==3:
        cprint("\n\t\tWelcome to TM Time Division Multiplexing Module!", 'red', attrs=['bold','underline'], file=sys.stderr)
        print colored("Enter number of data streams :",'cyan')
        k0i=input();l=[]
        while k0i:
            k0i-=1
            print colored("Enter input bitrate :",'yellow')
            l.append(input())
        cprint ("Bitrate of output signals is",'red','on_blue',attrs=['bold'])
        cprint(sum(l),"cyan",attrs=['bold'],file=sys.stderr)
    elif foo==4:
        cprint("\n\t\tWelcome to TM Block Coding Module!", 'red', attrs=['bold','underline'], file=sys.stderr)
        print colored("Enter number of bytes you want to transfer :",'cyan')
        koli=input()
        tosi=raw_input("");count=0;k="";soma=[];king=[]
        for i in tosi:
            count+=1
            k+=str(i)
            if count%4==0:
                soma.append(k)
                k=""
        dicta={"0000":"11110","0001":"01001","0010":"10100","0011":"10101","0100":"01010","0101":"01011","0110":"01110","0111":"01111","1000":"10010","1001":"10011","1010":"10110","1011":"10111","1100":"11011","1110":"11100","1111":"11101"}
        for i in soma:
            s=dicta[i]
            king.append(s)
        sim=""
        for i in king:
            sim+=i
        cprint ("Encoded table is",'red','on_blue',attrs=['bold'])
        cprint(dicta,"cyan",attrs=['bold'],file=sys.stderr)
        cprint ("Encoded signal is",'red','on_blue',attrs=['bold'])
        cprint(sim,"cyan",attrs=['bold'],file=sys.stderr)
    elif foo==5:
        cprint("Thank You for using  TM Error Detection,Control and Time Division Multiplexing System!", 'yellow', attrs=['bold','underline'], file=sys.stderr)
        break
    else:
        cprint("Invalid Options", 'green', attrs=['bold','underline'], file=sys.stderr)
