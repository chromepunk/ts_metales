from datetime import datetime

d=datetime.today()
td=str(d).split()[0]

def countWords(text):
    n=len(text.split())
    return n

def saveFile(words, today):
    try:
        different=True
        
        l=open("palabrasIntro.txt")
        for line in l:
            #print(line.rstrip())
            if line == str(today):
                different=False
                print("ya puesto")
        l.close()
        
        f=open("palabrasIntro.txt","a")
        if different:
            f.write(str(words) +" "+ str(today)+ " \n" )
        else:
            pass
        f.close()

    except:
        print("error")


try:
    f=open("1introduccion.txt")
    s=f.read()
    f.close()

except:
    print("se ha cometido un error")

w=countWords(s)

saveFile(w,td)

