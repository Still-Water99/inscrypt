from tkinter import *
from Source import *
import mysql.connector as ms

Running=True
qu=0
def g():
    global Running,b6,r,qu
    b=a=c=t=qu=mn=0
    ps=-5
    k=180
    point=11
    user=''

    def tutorial():
        file=open('tutorial.txt')
        s=file.read()
        n=Tk(className='Tutorial')
        Label(n,text=s,justify='left',bg='#998675',font=('Epithet',13)).pack(anchor='w')
        n.mainloop()
        file.close()
    def highscores():
        ma=ms.connect(host='localhost',user='root',passwd='areen',database='epitaph')
        mc=ma.cursor()
        mc.execute("Select * from highscore order by score")
        mfm=mc.fetchmany(10)
        d='\n'
        for i in mfm:
            for j in i:
                d+=str(j)+'\t'
            d+='\n'
        mc.execute('Select * from lowscore order by Score')
        mfm=mc.fetchmany(10)
        v='\n'
        for i in mfm:
            for j in i:
                v+=str(j)+'\t'
            v+='\n'
        n=Tk(className='HIGHSCORE')
        n.eval('tk::PlaceWindow . center')
        #Canvas(n,width=100,height=100).pack()
        Label(n,text='High score:'+d+'Top Ten Losers:'+v,justify='left',bg='#998675',font=('Epithet',13)).pack(anchor='w')
        n.mainloop()
    def call(m,p):
        nonlocal user
        user=m.get()
        print(user)
        p.destroy()
    def death():
        global Running
        Running=False
        master.destroy()
    def restart():
        global Running,qu
        Running=True
        qu=1
        master.destroy()
    def startgame():
        mc.configure(text=player_mana)
        cl=gamestart()
        for i in range(0,len(cl),2):
            img=PhotoImage(file=cl[i+1]['img'],width=125,height=192) 
            if cl[i]==1:
                lc1.configure(text=cl[i+1]['health'])
                c1.configure(image=img)
                c1.image=img
            elif cl[i]==2:
                lc2.configure(text=cl[i+1]['health'])
                c2.configure(image=img)
                c2.image=img
            elif cl[i]==3:
                lc3.configure(text=cl[i+1]['health'])
                c3.configure(image=img)
                c3.image=img
            elif cl[i]==4:
                lc4.configure(text=cl[i+1]['health'])
                c4.configure(image=img)
                c4.image=img
        start.destroy()
        l.destroy()
        tut.destroy()
        hs.destroy()

    def point_calc(points):
        nonlocal point
        t=points+150
        point=21-(((t*20)//300))
        p.configure(height=point)
        game_over()

    def game_over():
        nonlocal point,user,ps
        global b6,r,qu 

        if point>=21:
            l=Label(master,height=500,width=500)
            l.place(x=0,y=0)
            l=Label(master,text='YOU LOSE!!',font=('Epithet',35))
            l.place(x=590,y=300)
            b6=Button(master,text='EXIT',height=3,width=20,font=('Epithet',15),command=death)
            b6.place(x=600,y=370)
            r=Button(master,text='RESTART',height=3,width=20,font=('Epithet',15),command=restart)
            r.place(x=600,y=450)
            if user !='':
                ma=ms.connect(host='localhost',user='root',passwd='areen',database='epitaph')
                mc=ma.cursor()
                qur="insert into lowscore(Name,Score) values('"+str(user)+"',"+str(ps+5)+");"
                mc.execute(qur)
                ma.commit()
                ma.close()
                user=''
            
        elif point<=0:
            l=Label(master,height=500,width=500)
            l.place(x=0,y=0)
            l=Label(master,text='YOU WIN!!',font=('Epithet',35))
            l.place(x=590,y=300)
            b6=Button(master,text='EXIT',height=3,width=20,font=('Epithet',15),command=death)
            b6.place(x=600,y=370)
            r=Button(master,text='RESTART',height=3,width=20,font=('Epithet',15),command=restart)
            r.place(x=600,y=450)
            l=Label(master,text='Your Score is: '+str(ps),height=3,width=20,font=('Epitaph',15))
            l.place(x=590,y=530)
            if user !='':
                ma=ms.connect(host='localhost',user='root',passwd='areen',database='epitaph')
                mc=ma.cursor()
                quer="insert into highscore(Name,Score) values('"+str(user)+"',"+str(ps)+");"
                mc.execute(quer)
                ma.commit()
                ma.close()
                user=''


        
    def pass_():
        nonlocal c,t,ps
        t=0
        c+=1
        l=game(c)
        if c<2:
            opponent_turn()
            pass
        else:
            
            for i in range(0,len(l),2):
                if i!=len(l)-1:
                    ps+=1
                    if c%2==0 and l[i+1]==0:
                        
                        if l[i]==1:
                            od1.configure(image=blank_img)
                            lod1.configure(text='')
                            od1.image=blank_img
                        elif l[i]==2:
                            od2.configure(image=blank_img)
                            lod2.configure(text='')
                            od2.image=blank_img
                        elif l[i]==3:
                            od3.configure(image=blank_img)
                            lod3.configure(text='')
                            od3.image=blank_img
                        elif l[i]==4:
                            od4.configure(image=blank_img)
                            lod4.configure(text='')
                            od4.image=blank_img
                    elif c%2!=0 and l[i+1]==0:
                        if l[i]==1:
                            d1.configure(image=blank_img)
                            ld1.configure(text='')
                            d1.image=blank_img
                        elif l[i]==2:
                            d2.configure(image=blank_img)
                            ld2.configure(text='')
                            d2.image=blank_img
                        elif l[i]==3:
                            d3.configure(image=blank_img)
                            ld3.configure(text='')
                            d3.image=blank_img
                        elif l[i]==4:
                            d4.configure(image=blank_img)
                            ld4.configure(text='')
                            d4.image=blank_img
                    elif c%2==0 and l[i+1]!=0:
                        if l[i]==1:
                            lod1.configure(text=l[i+1])
                        elif l[i]==2:
                            lod2.configure(text=l[i+1])
                        elif l[i]==3:
                            lod3.configure(text=l[i+1])
                        elif l[i]==4:
                            lod4.configure(text=l[i+1])
                    elif c%2!=0 and l[i+1]!=0:
                        if l[i]==1:
                            ld1.configure(text=l[i+1])
                        elif l[i]==2:
                            ld2.configure(text=l[i+1])
                        elif l[i]==3:
                            ld3.configure(text=l[i+1])
                        elif l[i]==4:
                            ld4.configure(text=l[i+1])
            else:
                point_calc(l[len(l)-1])
                if c%2!=0:
                    opponent_turn()
                    
    def opponent_turn():
        l=o_turn()
        for i in range(0,len(l),2):
            img=PhotoImage(file=l[i+1]['img'])
            if l[i]==1:
                od1.configure(image=img)
                od1.image=img
                lod1.configure(text=l[i+1]['health'])
            elif l[i]==2:
                od2.configure(image=img)
                od2.image=img
                lod2.configure(text=l[i+1]['health'])
            elif l[i]==3:
                od3.configure(image=img)
                od3.image=img
                lod3.configure(text=l[i+1]['health'])
            elif l[i]==4:
                od4.configure(image=img)
                od4.image=img
                lod4.configure(text=l[i+1]['health'])
        pass_()

    def turn(f):
        nonlocal a,b
        mc.configure(text=(k-20)//3)
        img=PhotoImage(file=f['img'])
        if a==1:
            c1.configure(image=blank_img)
            lc1.configure(text='')
            if b==1:
                d1.configure(image=img)
                ld1.configure(text=f['health'])
                d1.image=img
            elif b==2:
                d2.configure(image=img)
                ld2.configure(text=f['health'])
                d2.image=img
            elif b==3:
                d3.configure(image=img)
                ld3.configure(text=f['health'])
                d3.image=img
            elif b==4:
                d4.configure(image=img)
                ld4.configure(text=f['health'])
                d4.image=img
        elif a==2:
            c2.configure(image=blank_img)
            lc2.configure(text='')
            if b==1:
                d1.configure(image=img)
                ld1.configure(text=f['health'])
                d1.image=img
            elif b==2:
                d2.configure(image=img)
                ld2.configure(text=f['health'])
                d2.image=img
            elif b==3:
                d3.configure(image=img)
                ld3.configure(text=f['health'])
                d3.image=img
            elif b==4:
                d4.configure(image=img)
                ld4.configure(text=f['health'])
                d4.image=img
        elif a==3:
            c3.configure(image=blank_img)
            lc3.configure(text='')
            if b==1:
                d1.configure(image=img)
                ld1.configure(text=f['health'])
                d1.image=img
            elif b==2:
                d2.configure(image=img)
                ld2.configure(text=f['health'])
                d2.image=img
            elif b==3:
                d3.configure(image=img)
                ld3.configure(text=f['health'])
                d3.image=img
            elif b==4:
                d4.configure(image=img)
                ld4.configure(text=f['health'])
                d4.image=img
        elif a==4:
            c4.configure(image=blank_img)
            lc4.configure(text='')
            if b==1:
                d1.configure(image=img)
                ld1.configure(text=f['health'])
                d1.image=img
            elif b==2:
                d2.configure(image=img)
                ld2.configure(text=f['health'])
                d2.image=img
            elif b==3:
                d3.configure(image=img)
                ld3.configure(text=f['health'])
                d3.image=img
            elif b==4:
                d4.configure(image=img)
                ld4.configure(text=f['health'])
                d4.image=img
        elif a==5:
            c5.configure(image=blank_img)
            lc5.configure(text='')
            if b==1:
                d1.configure(image=img)
                ld1.configure(text=f['health'])
                d1.image=img
            elif b==2:
                d2.configure(image=img)
                ld2.configure(text=f['health'])
                d2.image=img
            elif b==3:
                d3.configure(image=img)
                ld3.configure(text=f['health'])
                d3.image=img
            elif b==4:
                d4.configure(image=img)
                ld4.configure(text=f['health'])
                d4.image=img
        
        a=b=0


    def mana():
        nonlocal k,t
        if t==0:
            if k<300:
                if k+75>320:
                    k=320
                else:
                    k=k+75
                man(k)
            bar.configure(height=k)
            mc.configure(text=(k-20)//3)
            t=1
        
            
            
    def draw():
        nonlocal t
        if t==0:
            i,im=s_draw()
            t=1
            img=PhotoImage(file=im['img'])
            if i==1:
                c1.configure(image=img)
                c1.image=img
                lc1.configure(text=im['health'])
            elif i==2:
                c2.configure(image=img)
                c2.image=img
                lc2.configure(text=im['health'])
            elif i==3:
                c3.configure(image=img)
                c3.image=img
                lc3.configure(text=im['health'])
            elif i==4:
                c4.configure(image=img)
                c4.image=img
                lc4.configure(text=im['health'])
            elif i==5:
                c5.configure(image=img)
                c5.image=img
                lc5.configure(text=im['health'])
            
        
    def card1():
        nonlocal a,b,k
        if check1(1):
            a=1
        if a!=0 and b!=0:
            l=cards(a,b)
            if l[0]:
                k=player_mana
                bar.configure(height=k)
                turn(l[1])
            
    def card2():
        nonlocal a,b,k
        if check1(2):
            a=2
        if a!=0 and b!=0:
            l=cards(a,b)
            if l[0]:
                k=player_mana
                bar.configure(height=k)
                turn(l[1])
            
    def card3():
        nonlocal a,b,k
        if check1(3):
            a=3
        if a!=0 and b!=0:
            l=cards(a,b)
            if l[0]:
                k=player_mana
                bar.configure(height=k)
                turn(l[1])
            
    def card4():
        nonlocal a,b,k
        if check1(4):
            a=4
        if a!=0 and b!=0:
            l=cards(a,b)
            if l[0]:
                k=player_mana
                bar.configure(height=k)
                turn(l[1])
            
    def card5():
        nonlocal a,b,k
        if check1(5):
            a=5
        if a!=0 and b!=0:
            l=cards(a,b)
            if l[0]:
                k=player_mana
                bar.configure(height=k)
                turn(l[1])
            
    def deck1():
        nonlocal a,b,k
        if check2(1):
            b=1
        if a!=0 and b!=0:
            l=cards(a,b)
            if l[0]:
                k=player_mana
                bar.configure(height=k)
                turn(l[1])
            
    def deck2():
        nonlocal a,b,k
        if check2(2):
            b=2
        if a!=0 and b!=0:
            l=cards(a,b)
            if l[0]:
                k=player_mana
                bar.configure(height=k)
                turn(l[1])
            
    def deck3():
        nonlocal a,b,k
        if check2(3):
            b=3
        if a!=0 and b!=0:
            l=cards(a,b)
            if l[0]:
                k=player_mana
                bar.configure(height=k)
                turn(l[1])
            
    def deck4():
        nonlocal a,b,k
        if check2(4):
            b=4
        if a!=0 and b!=0:
            l=cards(a,b)
            if l[0]:
                k=player_mana
                bar.configure(height=k)
                turn(l[1])
    
            
    master=Tk()
    master.title('Epithet')
    w = Canvas(master, width=1366, height=704)
    w.pack()
    blank_img=PhotoImage(file='blank.png',width=125,height=192)
    master.iconbitmap('logo.ico')
    drawcard = PhotoImage(file='drawcard.png')
    manadraw= PhotoImage(file='mana.png')
    b1 = Button(master,bg='BLUE',activebackground='LIGHTSKYBLUE1',font=('Epithet',11),image=manadraw,command=mana)
    b1.place(x=50,y=595)
    b2 = Button(master,bg='BROWN',activebackground='BROWN',font=('Epithet',11),image=drawcard,command=draw)
    b2.place(x=1250,y=595)
    b3=Button(master,bg='PINK',width=5,height=3,text='PASS',font=('Epithet',11),command=pass_)
    b3.place(x=1250,y=300)

    c1 = Button(master,image=blank_img,width=125,height=192,command=card1)
    c1.place(x=250,y=500)
    lc1=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    lc1.place(x=340,y=665)
    c2 = Button(master,image=blank_img,width=125,height=192,command=card2)
    c2.place(x=450,y=500)
    lc2=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    lc2.place(x=540,y=665)
    c3 = Button(master,image=blank_img,width=125,height=192,command=card3)
    c3.place(x=650,y=500)
    lc3=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    lc3.place(x=740,y=665)
    c4 = Button(master,image=blank_img,width=125,height=192,command=card4)
    c4.place(x=850,y=500)
    lc4=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    lc4.place(x=940,y=665)
    c5 = Button(master,image=blank_img,width=125,height=192,command=card5)
    c5.place(x=1050,y=500)
    lc5=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    lc5.place(x=1140,y=665)

    d1=Button(master,image=blank_img,width=125,height=192,command=deck1)
    d1.place(x=350,y=300)
    ld1=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    ld1.place(x=440,y=465)
    d2=Button(master,image=blank_img,width=125,height=192,command=deck2)
    d2.place(x=550,y=300)
    ld2=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    ld2.place(x=640,y=465)
    d3=Button(master,image=blank_img,width=125,height=192,command=deck3)
    d3.place(x=750,y=300)
    ld3=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    ld3.place(x=840,y=465)
    d4=Button(master,image=blank_img,width=125,height=192,command=deck4)
    d4.place(x=950,y=300)
    ld4=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    ld4.place(x=1040,y=465)

    od1=Label(master,image=blank_img,width=125,height=192)
    od1.place(x=350,y=50)
    lod1=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    lod1.place(x=440,y=215)
    od2=Label(master,image=blank_img,width=125,height=192)
    od2.place(x=550,y=50)
    lod2=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    lod2.place(x=640,y=215)
    od3=Label(master,image=blank_img,width=125,height=192)
    od3.place(x=750,y=50)
    lod3=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    lod3.place(x=840,y=215)
    od4=Label(master,image=blank_img,width=125,height=192)
    od4.place(x=950,y=50)
    lod4=Label(master,bg='#998675',width=3,foreground='#3E6A4E',font=('Epithet',11))
    lod4.place(x=1040,y=215)

    cap=Label(master,width=6,height=22,bg='BLACK')
    cap.place(x=47,y=40)
    cap=Label(master,width=5, height=21)
    cap.place(x=50,y=45)

    m=PhotoImage(file='bar.png')
    bar=Label(master,image=m,width=37,height=k)
    bar.place(x=50,y=45)
    cap=Label(master,width=5,height=0,bg='BLACK')
    cap.place(x=50,y=45)
    mc=Label(master,width=2,font=('Epithet',15),foreground='BLUE')
    mc.place(x=55,y=380)

    cap=Label(master,width=6,height=23,bg='BLACK')
    cap.place(x=1146,y=40)
    po=Label(master,bg="RED",width=5,height=21)
    po.place(x=1150,y=50)
    p=Label(master,bg='BLUE',width=5,height=point)
    p.place(x=1150,y=50)
    cap=Label(master,width=5,height=0,bg='BLACK')
    cap.place(x=1150,y=45)

    strt=PhotoImage(file='bg.png',height=1000,width=10000)
    l=Label(master,image=strt)
    l.place(x=-300,y=0)
    start=Button(master,height=3,width=20,text='START',font=('Epithet',15),command=startgame)
    start.place(x=600,y=300)
    
    tut=Button(master,height=3,width=20,text='TUTORIAL',font=('Epithet',15),command=tutorial)
    tut.place(x=600,y=400)
    
    hs=Button(master,height=3,width=20,text='HIGH SCORES',font=('Epithet',15),command=highscores)
    hs.place(x=600,y=500)
    if mn==0:
        mn+=1
        n=Tk()
        n.eval('tk::PlaceWindow . center')
        Label(n,height=3,width=20,text='Enter Name:').place(x=0,y=30)
        e=Entry(n,width=10)
        e.place(x=120,y=45)
        mq=Button(n,height=3,text='Submit',font=('Epithet',8),command=lambda: call(e,n))
        mq.place(x=40,y=90)
        n.mainloop()
    master.mainloop()
    
while Running:
    g()
    re()
    if qu == 0:
        Running = False
    else:
        Running = True
