by=100
bx=200
byt=100
ballx=100
bally=100
ballxspeed=-2
ballyspeed=2
sk=20
ws=20
ms=20
t1=20
t2=20
t3=20
x1=3
x2=3
hw=800
menu=1
rz=900
op=1
def setup():
    global ballx,bally
    size(800,400)
    ballx=400
    bally=230
    f = createFont("Georgia", 50) 
    textFont(f)
def draw():
    global ballx,bally,ballxspeed,ballyspeed,by,byt,bx,sk,ws,ms,t1,t2,t3,x1,x2,hw,menu,rz
    fill(255,255,255)
    rect(0,0,800,800)
    fill(0,255,0)
    rect(100,100,600,260)
    fill(0,0,255)
    rect(137,by,10,75)
    fill(255,0,0)
    rect(20,20,sk,sk)
    rect(45,20,ws,ws)
    rect(70,20,ms,ms)
    rect(700,20,t1,t1)
    rect(725,20,t2,t2)
    rect(750,20,t3,t3)
    rect(650,byt,10,75)
    line(400,360,400,100)
    fill(78,33,45)
    triangle(350,100,400,150,450,100)
    triangle(350,360,400,310,450,360)
    fill(6,0,60)
    ellipse(ballx,bally,10,10)
    ballx+=ballxspeed
    bally+=ballyspeed
    if bally>=353:
        ballyspeed=-ballyspeed
    if bally<=105:
        ballyspeed=-ballyspeed
    if keyPressed:
        if key =='p' and ballxspeed == 0 and ballyspeed ==0:
            ballyspeed=2
            ballxspeed=-2
        if key == 'w' and by>=101 and ballxspeed<=0:
            by-=2
        if key == 's' and by<=282 and ballxspeed<=0:
            by+=2
        if key == 't' and byt>=101 and ballxspeed>=0: 
            byt-=2
        if key == 'o' and menu==1:
            op=0    
        if key == 'g' and byt<=282 and ballxspeed>=0:
            byt+=2
        if key == 't' and menu==1:
            menu=0
            x1=3
            x2=3
            ballx=400
            bally=230
            sk=20
            ws=20
            ms=20
            t1=20
            t2=20
            t3=20    
        if key == 'r' and hw == 800:
            x1=3
            x2=3
            ballx=400
            bally=230
            sk=20
            ws=20
            ms=20
            t1=20
            t2=20
            t3=20
    if ballx<=147 and bally>=by and bally<=by+75 and ballx>=137:
        ballxspeed=-ballxspeed
    if ballx>=650 and bally>=byt and bally<=byt+75 and ballx<=660:
        ballxspeed=-ballxspeed
    if ballx<=5:
        ballxspeed=0
        ballyspeed=0
        ballx=400
        bally=230
    if ballx>=795:
        ballxspeed=0
        ballyspeed=0
        ballx=400
        bally=230
    if ballx==70:
        x1=x1-1
    if ballx<=50 and x1==2:
        sk=0
    if ballx<=50 and x1==1:
        ws=0
    if ballx<=50 and x1==0:
        ms=0
    if ballx==730:
        x2=x2-1
    if ballx>=780 and x2==2:
        t1=0
    if ballx>=780 and x2==1:
        t2=0
    if ballx>=780 and x2==0:
        t3=0
    if x1==0 or x2==0:
        rect(0,0,hw,hw)
        fill(255,0,0)
        text("Game Over", 270,165)
        text("To restart press  R",220,220)
    if x1==0:
        text("Blue Wins",270,120)
    if x2==0:
        text("Red Wins",270,120)
    if menu==1:
        rect(0,0,rz,rz)
        fill(255,0,0)
        text("Two Players",270,170)
        text("One Player",270,240)
        text("Ping-Pong",270,110)
