# Was
oõõøœ
by=100
bx=200
byt=100
ballx=100
bally=100
ballxspeed=-2
ballyspeed=2
def setup():
    global ballx,bally
    size(800,400)
    ballx=width/2
    bally=height/2
def draw():
    global ballx,bally,ballxspeed,ballyspeed,by,byt,bx
    rect(0,0,800,800)
    rect(100,100,600,200)
    rect(100,by,50,100)
    rect(650,byt,50,100)
    line(400,300,400,100)
    triangle(350,100,400,150,450,100)
    triangle(350,300,400,250,450,300)
    ellipse(ballx,bally,10,10)
    ballx+=ballxspeed
    bally+=ballyspeed
    if ballx<=105:
        ballxspeed=-ballxspeed
    if bally>=295:
        ballyspeed=-ballyspeed
    if bally<=105:
        ballyspeed=-ballyspeed
    if ballx>=705:
        ballxspeed=-ballxspeed
    if keyPressed:
        if key =='p':
            ballysoeed=2
            ballxspeed=-2
        if key == 'w' and by>=101:
            by-=2
        if key == 's' and by<=199:
            by+=2
        if key == 'r' and byt>=101:    
            byt-=2
        if key == 'f' and byt<=200:
            byt+=2
    if ballx<=150 and bally>=by and bally<=by+100:
        ballxspeed=-ballxspeed
    if ballx>=650 and bally>=byt and bally<=byt+100:
        ballxspeed=-ballxspeed
    if ballx<=110:
        ballxspeed=0
        ballyspeed=0
        ballx=width/2
        bally=height/2
    if ballx>=700:
        ballxspeed=0
        ballyspeed=0
        ballx=width/2
        bally=height/2
        
            
            
