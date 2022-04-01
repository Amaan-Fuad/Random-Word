from tkinter import*
import random

amaan=Tk()
amaan.title("Random Word Generator")
amaan.geometry("600x400")
amaan.configure(background="yellow")

label1=Label(amaan)
label1.place(relx=0.5,rely=0.4,anchor=CENTER)
def random_word():
    list1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","0","P","Q","R","S","T","U","W","X","Y","Z"]
    random1=random.randint(0,25)
    random2=random.randint(0,25)
    random3=random.randint(0,25)
    random4=random.randint(0,25)
    random5=random.randint(0,25)
    
    randomalpha1=list1[random1]
    randomalpha2=list1[random2]
    randomalpha3=list1[random3]
    randomalpha4=list1[random4]
    randomalpha5=list1[random5]
    

    randomword=randomalpha1+randomalpha2+randomalpha3+randomalpha4+randomalpha5
    label1["text"]=str(randomword)
button1=Button(amaan,text="Random Word",command=random_word)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)
amaan.mainloop()