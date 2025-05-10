print("welcome to a 1v1 TicTaeToe game!")
ch=str(input("Choose 'X' in order to have the first chance else choose 'O': "))
ox=ch.capitalize()
left = [1,2,3,4,5,6,7,8,9]
used=[]
if ox=='X':
    comp = 'O'
else:
    comp = 'X'

def table():
    print('''
_1_|_2_|_3_
_4_|_5_|_6_
 7 | 8 | 9
    ''')

def move(list=left,use=used):
    table()
    mov=int(input("Look at the table, and enter the number to move: "))
    if mov in list:
        list.remove(mov)
        use.append(mov)
        return mov
    else:
        print("invalid! choose again\n")
        return move()

dict={"s1":"_","s2":"_","s3":"_","s4":"_","s5":"_","s6":"_","s7":" ","s8":" ","s9":" "}

def exe():
    for i in range(1,10):
        mov=move()
        if (i%2)!=0:
            xo = ox
            if mov == 1:
                dict["s1"]=xo
            elif mov ==2:
                dict["s2"]=xo
            elif mov ==3:
                dict["s3"]=xo
            elif mov ==4:
                dict["s4"]=xo
            elif mov ==5:
                dict["s5"]=xo
            elif mov ==6:
                dict["s6"]=xo
            elif mov ==7:
                dict["s7"]=xo
            elif mov ==8:
                dict["s8"]=xo
            elif mov ==9:
                dict["s9"]=xo
            gt = (f'''
            _{dict["s1"]}_|_{dict["s2"]}_|_{dict["s3"]}_
            _{dict["s4"]}_|_{dict["s5"]}_|_{dict["s6"]}_
             {dict["s7"]} | {dict["s8"]} | {dict["s9"]}       
            ''')
            print (gt)
        else:
            if mov == 1:
                dict["s1"]=comp
            elif mov ==2:
                dict["s2"]=comp
            elif mov ==3:
                dict["s3"]=comp
            elif mov ==4:
                dict["s4"]=comp
            elif mov ==5:
                dict["s5"]=comp
            elif mov ==6:
                dict["s6"]=comp
            elif mov ==7:
                dict["s7"]=comp
            elif mov ==8:
                dict["s8"]=comp
            elif mov ==9:
                dict["s9"]=comp
            gt = (f'''
            _{dict["s1"]}_|_{dict["s2"]}_|_{dict["s3"]}_
            _{dict["s4"]}_|_{dict["s5"]}_|_{dict["s6"]}_
             {dict["s7"]} | {dict["s8"]} | {dict["s9"]}       
            ''')
            print (gt)

exe()