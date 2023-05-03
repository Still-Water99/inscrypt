from random import *

#cards
#common-66.67% fair-21.11% kinda rare-6.67% super rare-3.33% ultra omega rare-2.22%
blank={'health':0,'attack':0,'mana':0,'img':'blank.png'}
gilgamesh={'health':45,'attack':55,'mana':65,'img':'gilgamesh.png'} #-- fair 7
genghis={'health':40,'attack':50,'mana':45,'img':'genghis.png'} #-- common 10
gandhi={'health':1,'attack':99,'mana':70,'img':'gandhi.png'}# --super rare --Diff from Victoria 3
alexander={'health':50,'attack':60,'mana':55,'img':'alexander.png'}#-- common 10
victoria={'health':100,'attack':1,'mana':70,'img':'victoria.png'} # --fair  --Diff from Gandhi 5
caesar={'health':80,'attack':30,'mana':55,'img':'caesar.png'}#-- common 10
me={'health':69,'attack':69,'mana':69,'img':'me.png'}#-- kinda rare 6
napoleon={'health':45,'attack':45,'mana':45,'img':'napoleon.png'} #-- common 10
you={'health':420,'attack':420,'mana':420,'img':'you.png'} #-- Ultra omega rare 2
hitler={'health':10,'attack':70,'mana':65,'img':'hitler.png'} #-- fair 7
cleopatra={'health':70,'attack':20,'mana':45,'img':'cleopatra.png'} #-- common 10
lenin={'health':60,'attack':50,'mana':65,'img':'lenin.png'}#-- common 10
card=[blank,gilgamesh,genghis,gandhi,alexander,victoria,caesar,me,napoleon,you,hitler,cleopatra,lenin]

points=0

player_hand=[dict(blank),dict(blank),dict(blank),dict(blank),dict(blank)]
player_play=[dict(blank),dict(blank),dict(blank),dict(blank)]
player_mana=60

opponent_play=[dict(blank),dict(blank),dict(blank),dict(blank)]
opponent_hand=[dict(blank),dict(blank),dict(blank),dict(blank),dict(blank)]
opponent_mana=60

def card_calc():
    c=randint(1,90)
    if c<=7:
        c=1
    elif c<=17:
        c=2
    elif c<=20:
        c=3
    elif c<=30:
        c=4
    elif c<=35:
        c=5
    elif c<=45:
        c=6
    elif c<=51:
        c=7
    elif c<=61:
        c=8
    elif c<=63:
        c=9
    elif c<=70:
        c=10
    elif c<=80:
        c=11
    elif c<=90:
        c=12
    return c

def gamestart():
    global player_hand,card,opponent_hand
    i=0
    l=[]
    cl=[]
    while i<=3:
        c=card_calc()
        if c not in l:
            l.append(c)
            player_hand[i]=dict(card[c])
            cl.append(i+1)
            cl.append(card[c])
            i+=1
    i=0
    l=[]
    while i<=3:
        c=card_calc()
        if c not in l:
            l.append(c)
            opponent_hand[i]=dict(card[c])
            i+=1
    return cl
    
            
def man(k):
    global player_mana
    player_mana=(k-20)//3

def cards(a,b):
    global player_play,player_mana,player_hand
    l=[]
    if player_mana>=player_hand[a-1]['mana']:
        player_play[b-1]=dict(player_hand[a-1])
        player_mana=player_mana-player_hand[a-1]['mana']
        player_hand[a-1]=dict(blank)
        l.append(True)
        l.append(player_play[b-1])
    else:
        l.append(False)
    return l
    
def s_draw():
    global player_hand
    c=card_calc()
    for i in range(0,5):
        if player_hand[i]==dict(blank):
            player_hand[i]=dict(card[c])
            return i+1,card[c]
            break

def check1(a):
    global player_hand
    if player_hand[a-1]!=dict(blank):
        return True
    else:
        return False
    
def check2(b):
    global player_play
    if player_play[b-1]==dict(blank):
        return True
    else:
        return False

def game(c):
    global player_play,card,opponent_play,points
    l=[]
    if c<2:
        pass
    elif c%2==0:
        for b in range(1,5):
            if player_play[b-1]!=dict(blank):    
                l.append(b)
                if opponent_play[b-1]['health']-player_play[b-1]['attack']<=0:
                    points=points-(opponent_play[b-1]['health']-player_play[b-1]['attack'])
                    opponent_play[b-1]=dict(blank)
                else:
                    opponent_play[b-1]['health']=opponent_play[b-1]['health']-player_play[b-1]['attack']
                l.append(opponent_play[b-1]['health'])
    else:
        for b in range(1,5):
            if opponent_play[b-1]!=dict(blank):
                l.append(b)
                if player_play[b-1]['health']-opponent_play[b-1]['attack']<=0:
                    points=points+(player_play[b-1]['health']-opponent_play[b-1]['attack'])
                    player_play[b-1]=dict(blank)
                else:
                    player_play[b-1]['health']=player_play[b-1]['health']-opponent_play[b-1]['attack']
                l.append(player_play[b-1]['health'])
    l.append(points)
    return l

def o_turn():
    global opponent_hand,opponent_play,card,opponent_mana
    l=[]
    t=-1
    c=d=0
    for i in opponent_hand:
        if i!=dict(blank):
            d+=1
    if d<=3:
        c=1
        for i in range(0,len(opponent_hand)):
            if opponent_hand[i]==dict(blank):
                opponent_hand[i]=dict(card[card_calc()])
                break
    
    for i in range(0,len(opponent_hand)):
        if opponent_hand[i]['mana']<=opponent_mana and opponent_hand[i]!=dict(blank):
            opponent_mana=opponent_mana-opponent_hand[i]['mana']
            for j in range(0,4):
                if opponent_play[j]==dict(blank) and t==-1:
                    t=j
                elif player_play[j]!=dict(blank) and opponent_play[j]==dict(blank):
                    opponent_play[j]=dict(opponent_hand[i])
                    opponent_hand[i]=dict(blank)
                    l.append(j+1)
                    l.append(opponent_play[j])
                    break
            else:
                opponent_play[t]=opponent_hand[i]
                opponent_hand[i]=dict(blank)
                l.append(t+1)
                l.append(opponent_play[t])
    else:
        if c!=1 and opponent_mana+20<100 :
            opponent_mana+=25
            c=1
        elif c!=1:
            opponent_mana=100          
    return l

