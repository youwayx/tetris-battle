'''
Tetris Battle
Created by Yuwei Xu, Eman Igbokwe
this is a similar version to the ever popular tetris battle
game with not many changes"
'''

#basic modules needed for game to run
from pygame import* 
from random import*

screen = display.set_mode((800,600))#screen is 800*600 

myClock=time.Clock() #this will be used to set the FPS(frames/s) 
timer2p=time.Clock() #this will be used for counting down time in our game

#first function
#will be used for choosing what map you want to play on
def setmap():
    running = True
    #loading images
    back1 = image.load("menu pics/mainsetmap.png")
    outline = image.load("menu pics/outline.png")
    #defining rectangles for collision checking
    map1= Rect(155,75,200,200)
    map2= Rect(439,75,200,200)
    map3= Rect(155,309,200,200)
    map4= Rect(439,309,200,200)
    buttons = [map1,map2,map3,map4]#preparing a buttons and names list to be zipped together
    names = ["none","classic","comboking","lunchbox"]# 
    screen.blit(back1,(0,0))#back1 is the main background
    while running:
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False

        for b,n in zip(buttons,names): #zipping buttons and names together       
            if b.collidepoint(mpos):   #for very easy collision checking            
                if mb[0]==1:
                    return n#return the name of the map chosen

        #this chunk of code is just making pretty pictures       
        if map1.collidepoint(mpos):
            screen.blit(outline,(149,64))
        elif map2.collidepoint(mpos):
            screen.blit(outline,(431,64))
        elif map3.collidepoint(mpos):
            screen.blit(outline,(149,301))
        elif map4.collidepoint(mpos):
            screen.blit(outline,(431,301))
        else:
            screen.blit(back1,(0,0))#keeping it fresh
        
        display.flip() #necessities

#gridchoice=""
#main game function
def start(myClock,timer2p):#parameters are FP/s rate and timer countdown
################################################################################
    
    gridchoice=setmap()#calling the setmap function for a choice of grid

    #the code below is what happens when you set a map
    #different maps = differnet grids
    if gridchoice == "none":
        grid1=[[0]*20 for i in range (10)]
        grid2=[[0]*20 for i in range (10)]
    if gridchoice == "classic":
        grid1=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        grid2=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    if gridchoice == "comboking":
        grid1=[[0, 0, 0, 0, 0, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [0, 0, 0, 0, 0, 6, 6, 6, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6, 4, 5], [0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5], [0, 0, 0, 0, 0, 6, 6, 6, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6, 4, 5], [0, 0, 0, 0, 0, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
        grid2=[[0, 0, 0, 0, 0, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [0, 0, 0, 0, 0, 6, 6, 6, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6, 4, 5], [0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5], [0, 0, 0, 0, 0, 6, 6, 6, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6, 4, 5], [0, 0, 0, 0, 0, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]
    if gridchoice == "lunchbox":
        grid1=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 2, 2, 2, 2, 2, 2, 5, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 2, 4, 4, 4, 4, 2, 5, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 2, 4, 4, 4, 4, 2, 5, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 2, 2, 2, 2, 2, 2, 5, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 5, 5, 5, 5, 5, 5, 5, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]]
        grid2=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 2, 2, 2, 2, 2, 2, 5, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 2, 4, 4, 4, 4, 2, 5, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 2, 4, 4, 4, 4, 2, 5, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 2, 2, 2, 2, 2, 2, 5, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 5, 5, 5, 5, 5, 5, 5, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]]
           
    init() #for music
    battlemusic=mixer.Sound("tetris sounds/battlemusic.wav")#importing sound file
    #the code below imports many of the images that will be used
    gamescreen=image.load("gamescreen.png")#backscreen
    lgrey=image.load("lightgreysquare.png")#square for grid background
    dgrey=image.load("darkgreysquare.png")#smae as above
    ipiece=image.load("tetris blocks/lightblue block.png") 
    opiece=image.load("tetris blocks/yellow block.png")
    jpiece=image.load("tetris blocks/blue block.png")
    lpiece=image.load("tetris blocks/orange block.png")
    zpiece=image.load("tetris blocks/red block.png")
    spiece=image.load("tetris blocks/green block.png")
    tpiece=image.load("tetris blocks/purple block.png")
    lspiece=image.load("tetris blocks/linessent block.png")
    sentpiece=image.load("tetris blocks/linessent block.png")#dark block for garbage lines
    ghost=image.load("tetris blocks/ghost block.png") #ghost block 
    decimal=image.load("tetris numbers/decimal.png") #for timer
    ko=image.load("tetris icons/KO.png")#knockout image
    holdback=image.load("tetris icons/holdback.png")#background for pic blitting
    sentback=image.load("tetris icons/sentback.png")#same as above
    nextback2=image.load("tetris icons/holdback2.png")#same as above
    nextback3=image.load("tetris icons/holdback3.png")#same as above
    timeback=image.load("tetris icons/timeback.png")#same as above

    kos = [] #ko pictures
    for i in range(1,4):#putting kO pictures in the list 
        kos.append(image.load("tetris icons/ko"+str(i)+".png"))

    #piecepics list is the list different block pictures
    piecepics=[ipiece,opiece,jpiece,lpiece,zpiece,spiece,tpiece,lspiece]
    resizepics=[]#blocks will be resized for hold piece 
    for i in range (7):
        resizepics.append(transform.smoothscale(piecepics[i],(12,12))) #12 x12 blocks

    nextpics=[]#blocks will be resized for next pieces
    for i in range (7):
        nextpics.append(transform.smoothscale(piecepics[i],(8,8)))  #8 x8 blocks

    numbers=[]#imputing the numbers from 1 to 10 into list 
    for i in range (10): #to be used for timer and sent lines
        numbers.append(image.load("tetris numbers/"+str(i)+".png"))

    combos=[]#inputs the combo pictures
    for i in range (1,11):
        combos.append(image.load("combo/"+str(i)+"combo.png"))

    back=image.load("tetris icons/back.png")#the main background screen
    tetris=image.load("tetris icons/tetris.png")#tetris image

    #these lists below are the different pieces in the game
    #there are 4 different types of each list so that when you
    #rotate the image will change
    ipieces=[[[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]],
             [[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]],
             [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]],
             [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]]]
    opieces=[[[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]],
             [[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]],
             [[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]],
             [[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]]]
    jpieces=[[[0,3,3,0],[0,0,3,0],[0,0,3,0],[0,0,0,0]],
             [[0,0,0,0],[0,3,3,3],[0,3,0,0],[0,0,0,0]],
             [[0,0,3,0],[0,0,3,0],[0,0,3,3],[0,0,0,0]],
             [[0,0,0,3],[0,3,3,3],[0,0,0,0],[0,0,0,0]]]
    lpieces=[[[0,0,4,0],[0,0,4,0],[0,4,4,0],[0,0,0,0]],
             [[0,0,0,0],[0,4,4,4],[0,0,0,4],[0,0,0,0]],
             [[0,0,4,4],[0,0,4,0],[0,0,4,0],[0,0,0,0]],
             [[0,4,0,0],[0,4,4,4],[0,0,0,0],[0,0,0,0]]]
    zpieces=[[[0,5,0,0],[0,5,5,0],[0,0,5,0],[0,0,0,0]],
             [[0,0,0,0],[0,5,5,0],[5,5,0,0],[0,0,0,0]],
             [[0,5,0,0],[0,5,5,0],[0,0,5,0],[0,0,0,0]],
             [[0,0,5,5],[0,5,5,0],[0,0,0,0],[0,0,0,0]]]
    spieces=[[[0,0,6,0],[0,6,6,0],[0,6,0,0],[0,0,0,0]],
             [[0,0,0,0],[0,6,6,0],[0,0,6,6],[0,0,0,0]],
             [[0,0,6,0],[0,6,6,0],[0,6,0,0],[0,0,0,0]],
             [[6,6,0,0],[0,6,6,0],[0,0,0,0],[0,0,0,0]]]
    tpieces=[[[0,0,7,0],[0,7,7,0],[0,0,7,0],[0,0,0,0]],
             [[0,0,0,0],[0,7,7,7],[0,0,7,0],[0,0,0,0]],
             [[0,0,7,0],[0,0,7,7],[0,0,7,0],[0,0,0,0]],
             [[0,0,7,0],[0,7,7,7],[0,0,0,0],[0,0,0,0]]]
    lspieces=[8,8,8,8,8,8,8,8,8,8]#this is the lines sent piece aka garbage lines

    #list of all the pieces used later for choosing newpieces 
    allpieces=[ipieces,opieces,jpieces,lpieces,zpieces,spieces,tpieces]

    #screen=display.set_mode((800,600))
    running=True#necessity
    screen.blit(gamescreen,(0,0))#blitting the main background
    a=screen.copy()#used for image coverage

    px=4#starting x position of newblock for p1
    py=-2#starting y position of newblock for p1
    px2=4#starting x position of newblock for p2
    py2=-2#starting x position of newblock for p2
    oldko1=0 #these two used to keep track of ko's
    oldko2=0

    #these two used for countdown
    #of the timer
    time=130000
    delaytime=time
    
    #positions1=[]
    #positions2=[]

    #list of the held piece
    held1=[]
    held2=[]

    #amount of lines sent for p1 and p2
    sent1=0
    sent2=0
    tempsend1=0 #tempsending for p1 and p2
    tempsend2=0
    oldcombo1=combo1=-1 #used for checking comboas
    oldcombo2=combo2=-1

    #combo checker function
    #this function gets the amount of lines sent
    #and the combonumber and returns how many extra lines sent
    #depending on your number of combos
    def checkCombo(combo,sent):
        if combo>0:
            if combo<=8:
                sent+=(combo+1)/2
            else: sent+=4
        return sent
        
    #block moving function
    #takes in the grid the block and the x and y position of the falling block
    #if the block collides with the grid then
    #the block is added to the grid
    def blockmoving(grid, block, px,py):
        if collideDown(grid, block,px,py)==True:
            for x in range(4):
                for y in range (4):
                    if block[x][y]>0:
                        num=block[x][y]
                        if -1<px+x<10 and -1<py+y<20:
                            grid[px+x][py+y]=num
            return False
        else:
            return True
    #the ghost block piece
    def drawGhost(sx,sy,x,y):
        screen.blit(ghost,(sx+x*18,sy+y*18))
        
    #draws the ghost piece at where harddrop will take place
    #ghost goes where block will be when you harddrop
    def drawGhostPiece(grid,block,sx,sy,px,py):
        y=hardDrop(grid,block,px,py)
        py+=y
        for x in range (4):
            for y in range (4):
                if block[x][y]>0:
                    if 10>px+x>-1 and 20>py+y>-1:
                        drawGhost(sx,sy,px+x,py+y)
                        
    #draws the number of lines sent
    def drawNumbers(grid,sent,sx,sy):
        tens=sent/10#integer division tens digit
        ones=sent%10#remainder ones digit
        screen.blit(sentback,(sx-12,sy))
        if tens>0:
            if tens==1:
                #blitting the numbers at the poisition in numbers list
                screen.blit(numbers[tens],(sx-14,sy))
                screen.blit(numbers[ones],(sx+7,sy))
            else:
                screen.blit(numbers[tens],(sx-14,sy))
                screen.blit(numbers[ones],(sx+14,sy))
        else:
            screen.blit(numbers[ones],(sx,sy))
            
    #the timer for the game
    def drawTime2p(time):
        minutes=time/60000#integer div for minutes
        seconds=(time/1000)%60#int and mod div for sec
        milliseconds=(time/10)%100#int and mod div for millisec
        
        x=292#position of the numbers 
        y=67
        screen.blit(timeback,(280,63))#background
        #minutes
        screen.blit(numbers[minutes/10],(x,y))
        screen.blit(numbers[minutes],(x+27,y))
        screen.blit(decimal,(292+56,67)) #graphics
        screen.blit(decimal,(292+56,81))#graphics
        screen.blit(decimal,(292+127,81))#graphics
        #seconds
        screen.blit(numbers[seconds/10],(x+73,y))
        screen.blit(numbers[seconds%10],(x+100,y))
        #milliseconds
        screen.blit(numbers[milliseconds/10],(x+144,y))
        screen.blit(numbers[milliseconds%10],(x+171,y))

    #drawing the held pieces
    #this function allows you to hold a piece
    #by hitting the respective hold button
    def drawHeld(grid,held,sx,sy):
        if held!=[]:
            num=allpieces.index(held)
            pos=[]
            for x in range (4):
                for y in range (4):
                    if held[0][x][y]>0:
                        pos.append((x,y))
            screen.blit(holdback,(sx-8,159))
            if num>1:
                for i in range(4):#if its an i piece different x and y position
                    screen.blit(resizepics[num],(sx+int(pos[i][0]*12),sy+int(pos[i][1]*12)))
            if num==0:
                for i in range(4):#if its an o piece different x and y position
                    screen.blit(resizepics[num],(sx-5+int(pos[i][0]*12),sy-6+int(pos[i][1]*12)))
            if num==1:
                for i in range(4):#any other piece id the same x and y position
                    screen.blit(resizepics[num],(sx-5+int(pos[i][0]*12),sy+int(pos[i][1]*12)))

    #drawing the next pieces 
    def drawNext(grid,nextpieces,sx,sy): 
        for i in range (5):#5 different pieces 
            pos=[]
            for x in range (4):
                for y in range (4): #same procedure as the drawhed function
                    if nextpieces[i][0][x][y]>0:
                        num=nextpieces[i][0][x][y]
                        pos.append((x,y))
            
            if i==0: #position 1
                screen.blit(holdback,(sx-1,159))            
                if num ==1:#i piece is different x and y pos
                    for i in range (4):
                        screen.blit(resizepics[num-1],(sx+1+int(pos[i][0]*12),156+int(pos[i][1]*12)))
                elif num==2: #o piece is different x and y pos
                    for i in range (4):
                        screen.blit(resizepics[num-1],(sx+1+int(pos[i][0]*12),158+int(pos[i][1]*12)))                
                else: #every other piece is the same x and y pos              
                    for i in range (4):
                        screen.blit(resizepics[num-1],(sx+7+int(pos[i][0]*12),159+int(pos[i][1]*12)))
            if i==1: #position2
                screen.blit(nextback2,(sx+2,230))
                if num==1:#i piece is differnet x and y pos
                    for i in range (4):
                        screen.blit(nextpics[num-1],(sx+9+int(pos[i][0]*8),235+int(pos[i][1]*8)))
                if num==2:#o piece is differnt x and y pos
                    for i in range (4):
                        screen.blit(nextpics[num-1],(sx+10+int(pos[i][0]*8),235+int(pos[i][1]*8)))
                if num>2:#every other piece same x and y pos
                    for i in range (4):
                        screen.blit(nextpics[num-1],(sx+13+int(pos[i][0]*8),235+int(pos[i][1]*8)))
            if i>=2:#position 3,4,5
                screen.blit(nextback3,(sx+4,288+52*(i-2)))
                if num==1: #same as above
                    for j in range (4):
                        screen.blit(nextpics[num-1],(sx+9+int(pos[j][0]*8),288+(i-2)*51+int(pos[j][1]*8)))
                if num==2: #same as above
                    for j in range (4):
                        screen.blit(nextpics[num-1],(sx+9+int(pos[j][0]*8),292+(i-2)*51+int(pos[j][1]*8)))
                if num>2: #same as above
                    for j in range (4):
                        screen.blit(nextpics[num-1],(sx+12+int(pos[j][0]*8),292+(i-2)*51+int(pos[j][1]*8)))
                
    #drawing the different blocks
    #different numbers(vals) draws differnt colour blocks on the screen
    def drawBlock(sx,sy,x,y,val):
        pics = [ipiece,opiece,jpiece,lpiece,zpiece,spiece,tpiece,lspiece]
        screen.blit(pics[val-1],(sx+(x)*18,sy+(y)*18))
        
    #drawing the piece on the screen
    #calls on the drawblock funct in order to draw
    #the piece on the screen
    def drawPiece(sx,sy,block,px,py):
        for x in range(4):
            for y in range (4):
                if block[x][y]>0:
                    if -1<px+x<10 and -1<py+y<20:
                        drawBlock(sx,sy,px+x,py+y,block[x][y])

    #drawing the blocks on the grid
    #calls the drawblock function so that different numbers draw different colours on the screen
    def drawBoard(grid,sx,sy):
        for x in range (10):
            for y in range (20):
                if grid[x][y]>0:
                    drawBlock(sx,sy,x,y,grid[x][y])
                    
    #drawing the actual game screen           
    def drawScreen():
        drawHeld(grid1,held1,46+8,161)#draws held piece for grid1
        drawHeld(grid2,held2,428+8,161)#draws held piece for grid2
        drawNext(grid1,nextlist1,318,161)#draws next piece for grid1
        drawNext(grid2,nextlist2,701,161)#draws next piece for grid2
        drawNumbers(grid1,sent1,56,377)#draws the linessent on the screen for grid1
        drawNumbers(grid2,sent2,56+383,377)#draws the linessent on the screen for grid2
                        
        #this code blits the background grid for grid1
        for x in range(10):
            for y in range (20):
                if grid1[x][y]==0 and (x,y) not in positions1:
                    if (x+y)%2==0:
                        screen.blit(dgrey,(112+x*18,138+y*18))
                    elif (x+y)%2==1:
                        screen.blit(lgrey,(112+x*18,138+y*18))
        #this code blits the background grid for grid2   
        for x in range(10):
            for y in range (20):
                if grid2[x][y]==0 and (x,y) not in positions2:
                    if (x+y)%2==0:
                        screen.blit(dgrey,(495+x*18,138+y*18))
                    elif (x+y)%2==1:
                        screen.blit(lgrey,(495+x*18,138+y*18))
        #drawing the ghost peices as long as there are no
        #pieces under the block ie collidedown==False
        if collideDown(grid1,block1,px,py)==False:
            drawGhostPiece(grid1,block1,112,138,px,py)
        if collideDown(grid2,block2,px2,py2)==False:
            drawGhostPiece(grid2,block2,495,138,px2,py2)
        #drawing the pieces
        drawPiece(112,138,block1,px,py)              
        drawPiece(495,138,block2,px2,py2)
        #drawing the grid
        drawBoard(grid1,112,138)
        drawBoard(grid2,495,138)

    #move right function
    #when respective right buttons are pressed
    #x pos of the block moves over 1unit right
    def moveRight(px,py,px2,py2):
        if keys[K_h]:
            if collideRight(grid1,block1,px,py)==False:    
                px+=1
        if keys[K_RIGHT]:
            if collideRight(grid2,block2,px2,py2)==False:
                px2+=1
        return [px,py,px2,py2]

    #move left function
    #when respective left buttons are pressed
    #x pos of the block moves over 1unit left
    def moveLeft(px,py,px2,py2):
        if keys[K_f]:
            if collideLeft(grid1,block1,px,py)==False:
                px-=1
        if keys[K_LEFT]:
            if collideLeft(grid2,block2,px2,py2)==False:
                px2-=1
        return [px,py,px2,py2]


    #move down function
    #when respective down buttons are pressed
    #y pos of the block moves down 1unit
    #as long as there is nothing underneath
    def moveDown(px,py,px2,py2):

        if keys[K_g]:
            if collideDown(grid1,block1,px,py)==False:
                py+=1
        if keys[K_DOWN]:
            if collideDown(grid2,block2,px2,py2)==False:
                py2+=1
        return [px,py,px2,py2]


    #collidedown function
    #for i in range 4(y position)
    #if px+y=20 then collidedown =true
    #used for move down and rotation collision
    def collideDown(grid,block,px,py):
        for x in range(4):
            for y in range(4):
                if block[x][y]>0:
                    if -1<px+x<10 and -1<py+y<20:
                        n=block[x][y]
                        if py+y+1==20:
                            return True
                        if grid[px+x][py+y+1]>0:
                            if y<3 and block[x][y+1]==0:
                                return True
                            if y==3:
                                return True

        return False


    #collideleft function
    #for i in range 4(x positions)
    #if blockx +x =0 then collide left = True
    #used for moving block and rotation collision
    def collideLeft(grid,block,px,py):
        for x in range (4):
            for y in range (4):
                if block[x][y]>0:
                    if px+x-1==-1:
                        return True
                    if grid[px+x-1][py+y]>0:
                        if x>0 and block[x-1][y]==0:
                            return True
                        if x==0:
                            return True
        return False


    #collideright function
    #for i in range 4(x positions)
    #if blockx +x +1>9 then collide left = True
    #plus 1 is there cuz pxis on left of the piece
    #used for moving block and rotation collision
    def collideRight(grid,block,px,py):
        for x in range (4):
            for y in range (4):
                if block[x][y]>0:
                    if px+x+1>9:
                        return True
                    if grid[px+x+1][py+y]>0:
                        if x<3 and block[x+1][y]==0:
                            return True
                        if x==3:
                            return True
        return False


    
    #send function
    #sending number of lines
    def send(grid,gridb,sent,tempsend):
        x=0
        #tempsend = send then send increases
        #lines sent is the difference between these two
        #lines p1 sends affects p2grid and vice versa
        garbage=sent-tempsend
        for y in range (1,garbage+1):
            if grid[0][-y]==8:
                x+=1
        for i in range (1,x+1):
            for x in range (10):
                del grid[x][-i]
                grid[x]=[0]+grid[x]
        for y in range (garbage-x):    
            for i in range(10):
                del(gridb[i][y])#deletes top of grid
                gridb[i]=gridb[i]+[8]#adds garbage lines at the bottom
        return grid,gridb

    #ko Function
    def KO(grid,block,px,py,time):
        ko=False
        #if your grid hits the top ko =true
        for x in range (4):
            for y in range (4):
                if block[x][y]>0:
                    if py+y<0:
                        ko=True
        #if ko = true then all the garbage lines
        #are deleted. If there are no garbage lines then you lose
        if ko==True:
            garbage=0
            for y in range (20):
                for x in range (10):
                    if grid[x][y]==8:
                        garbage+=1
                        grid[x].remove(grid[x][y])
                        grid[x]=[0]+grid[x]
            if garbage==0:
                time=0     
        return [grid,ko,time]

    #def win(grid,gridb,kO,sent):
        
    #clear lines function
    #when you send lines the grid clears the line
    def clear(grid,gridb,block,b,sent,tempsend,combo):
        global tempsend1
        global tempsend2
        cleared=0
        tempsend=sent
        add=3
        for y in range (20):
            row=0#starts checking from row zero
            for x in range (10):
                if grid[x][y]>0 and grid[x][y]<8:
                    row+=1
            if row==10:
                add-=1
                #print tspinCheck(grid,block,px,py,b)
                if tspinCheck(grid,block,px,py,b)==True:#for tspin sends more lines than actually cleared
                    sent+=add
                cleared+=1
                for i in range (10):
                    del(grid[i][y])#deletes cleared lines
                    grid[i]=[0]+grid[i]#adds a row of zeros to the grid
                        
        if cleared>=1:#for sending lines
            combo+=1
            if cleared==4:#a tetris
                #screen.blit(tetris,(330,465))
                sent+=4 
            for i in range (1,4):#single, double, triple
                if cleared==i:
                    sent+=(i-1)
        if cleared==0:#no lines cleared= no combo
            #screen.blit(back,(315,440))
            combo=-1
        sent=checkCombo(combo,sent)#linessent increases with amount of combos
        return (combo,sent,tempsend,cleared)


    #getPositon function
    #gets the position of the block falling
    #position is sorted and returned to be used
    #for the falling blocks
    def getPositions(block,px,py):  
        positions=[]
        for x in range(4):
            for y in range (4):
                if block[x][y]>0:
                    positions.append((px+x,py+y))
                    sorted(positions, key=lambda pos: pos[1])
        return positions

    #rotatecollision function
    #when respective rotate buttons are pressed
    #this function checks if collide(left right or down has occured)
    #if it hasnt then rotation occurs
    def rotateCollide(grid,block,px,py):
        for x in range (4):
            for y in range (4):
                if block[x][y]>0:
                    if -1<px+x<10 and -1<py+y<20:
                        if grid[px+x][py+y]>0: 
                            return ["both",0]
                    if px+x<0:
                        return ["left",x]
                    if px+x>9:
                        return ["right",x]
                    if py+y>19:
                        return ["down",0]
               
        return [False,0]

    #this function allows you to slide in a piece at the last minute
    #allows you to move over 1 unit to the left or right
    def moveOver(grid,block,px,py):
        for x in range (4):
            for y in range (4):
                if block[x][y]>0:
                    if px+x>9:
                        px=moveOver(grid,block,px-1,py)[0]
                        py=moveOver(grid,block,px-1,py)[1]
                    if px+x<0:
                        px=moveOver(grid,block,px+1,py)[0]
                        py=moveOver(grid,block,px+1,py)[1]
                        
        return (px,py)            

    #this function checks if a tspin has occured
    #checks all possible tspin positions
    #then spins the t piece into the spot
    def tspinCheck(grid,block,px,py,b):
        if collideDown(grid,block,px,py)==True:
            if b==tpieces:
                pos=getPositions(block,px,py)
                if px+2<10 and py+3<20:
                    if grid[px][py+1]>0 and grid[px][py+3]>0 and grid[px+2][py+3]>0:

                        return True
                    elif grid[px][py+3]>0 and grid[px+2][py+3]>0 and grid[px+2][py+1]>0:

                        return True
        return False
    #this function rotates the piece
    #when rotation button is hit the next grid in the piece list becomes the piece
    def rotate(grid,block,px,py,b,tspin):
        c=b.index(block)
        y=(c+1)%4
        block=b[y]
        collision=rotateCollide(grid,block,px,py)#checks for collisions
        x=collision[0]
        d=collision[1]
        if x=="both":
            if rotateCollide(grid,b[y],px,py+1)==False:
                py+=1
            else:
                a=1
                for i in range (2):                
                    if rotateCollide(grid,b[y],px,py-i)[0]=="both":
                        #print "yes"
                        py-=a
                        if i==1:
                            block=b[c]
                            py+=2
                    if rotateCollide(grid,b[y],px,py-i)[0]==False:
                        break
        if x=="left":
            px=moveOver(grid,block,px,py)[0]#px becomes moveover move left
        if x=="right":
            px=moveOver(grid,block,px,py)[0]#px becomes moveover move right
        if x=="down":
            py-=1
        if tspinCheck(grid,block,px,py,b)==True:
            tspin=1
        return [block,px,py,tspin]

    #this function drops the piece as far as it can go until
    #it collides with a piece below it
    def hardDrop(grid,block,px,py):
        y=0
        x=0
        if collideDown(grid,block,px,py)==False:
            x=1
        if x==1:
            while True:
                py+=1
                y+=1
                if collideDown(grid,block,px,py)==True:
                    break
            
        return y

    #this function enables you to hold a piece
    def hold(grid,b,held,nextlist,piecelist):
        #when piece is held the block at pos[0]
        #in the nextlist becomes the newpiece
        if held==[]:
            held=b
            b=nextlist[0]
            nextlist.remove(nextlist[0])
            if len(piecelist)==0:
                piecelist=[ipieces,opieces,jpieces,lpieces,zpieces,spieces,tpieces]
            nextlist.append(choice(piecelist))
            piecelist.remove(nextlist[-1])
        #the piece switches with the held piece     
        else:
            b,held=held,b
            
        return [b,held,nextlist,piecelist] 

    #thisfunction creates a newblock to be appended to the nextlist
    def newBlock(grid,block,b,nextlist,piecelist):
        if len(piecelist)>0:
            n=randint(0,len(piecelist)-1) #makes chooosing random
            nextlist.append(piecelist[n]) #appends at the nth piece to the nextlist
            piecelist.remove(piecelist[n])#takes that piece out so there are no repeats

        else:
            piecelist=[ipieces,opieces,jpieces,lpieces,zpieces,spieces,tpieces]#rests piecelist
            nextlist.append(choice(piecelist))#add to nextlist
            piecelist.remove(nextlist[-1])#removes the last item in the next list
        b=nextlist[0]#firt grid of four 
        nextlist.remove(nextlist[0])
        return [b,nextlist,piecelist]

    #this function draws the combo number
    def drawCombo(combo,sx,sy):
        if combo>0:
            a=screen.copy()
            counter=0
            screen.blit(combos[combo-1],(sx,sy)) #blits the combo number
            display.flip()
            while True:
                counter+=1
                if counter==100: #blits until counter is 100
                    screen.blit(a,(0,0))
                    break

    #counters for various reasons               
    #improve timing of the game
    counter=0
    movecounter=0
    downcounter=0
    stopcounter1=0
    stopcounter2=0
    #piecelist p1
    piecelist1=[ipieces,opieces,jpieces,lpieces,zpieces,spieces,tpieces]
    #piecelist p2
    piecelist2=[ipieces,opieces,jpieces,lpieces,zpieces,spieces,tpieces]
    #choices of the list
    b1=choice(piecelist1)
    b2=choice(piecelist2)
    #removes the choices
    piecelist1.remove(b1)
    piecelist2.remove(b2)
    nextlist1=[]#list of 5 pieces that are going to come next
    nextlist2=[]
    block1=b1[0]#first piece in list
    block2=b2[0]#first piece in list
    tspin1=0 #for t spin
    tspin2=0 #for t spin
    #for "KO"
    KO1=0 
    KO2=0
    #DEFINING VARIABLES
    cleared1=0
    cleared2=0
    kocounter1=0
    kocounter2=0
    for i in range (5):
        nextlist1.append(choice(piecelist1))#gets five random pieces from the piecelist
        nextlist2.append(choice(piecelist2))    
        piecelist1.remove(nextlist1[-1])    #removes from piecelist.
        piecelist2.remove(nextlist2[-1])

    #main loop
    while running:
        battlemusic.play()#plays music
        keys=key.get_pressed()#gets pressed keys
        counter+=1
        movecounter+=1
        downcounter+=1
        
        if counter==65:#timing
            if collideDown(grid1,block1,px,py)==False:
                py+=1
            # must check if the piece CAN move down, if not copy to grid
            if collideDown(grid2,block2,px2,py2)==False:
                py2+=1
            counter=0#reset counter

        for evt in event.get():
            if evt.type==QUIT:
                running=False
            if evt.type==KEYDOWN:
                if evt.key==K_s:#rotating
                    thing=rotate(grid1,block1,px,py,b1,tspin1)#stuff you need when rotating
                    #rotate returs 4 items 
                    block1=thing[0]
                    px=thing[1]
                    py=thing[2]
                    tspin1=thing[3]
                if evt.key==K_SLASH:#rotating p2
                    thing=rotate(grid2,block2,px2,py2,b2,tspin2)#parameters
                    #rotate returs 4 items 
                    block2=thing[0]
                    px2=thing[1]
                    py2=thing[2]
                    tspin2=thing[3]
                if evt.key==K_t:#harddrop
                    y=hardDrop(grid1,block1,px,py)#parameters
                    py+=y
                    stopcounter1=50
                if evt.key==K_UP:#harddrop
                    y=hardDrop(grid2,block2,px2,py2)#parameters
                    py2+=y
                    stopcounter2=50
                if evt.key==K_a:#holding 
                    x=hold(grid1,b1,held1,nextlist1,piecelist1)#parameters
                    px=4 #rests x and y coords
                    py=-2
                    #hold returns 4 items
                    #assignning variables to each item
                    b1=x[0]
                    block1=b1[0]
                    held1=x[1]
                    nextlist1=x[2]
                    piecelist1=x[3]
                if evt.key==K_RSHIFT:#holding
                    x=hold(grid2,b2,held2,nextlist2,piecelist2)#parameters
                    #hold return 4 items
                    #assignning variables to each item
                    px2=4
                    py2=-2
                    b2=x[0]
                    block2=b2[0]
                    held2=x[1]
                    nextlist2=x[2]
                    piecelist2=x[3]
       
        if collideDown(grid1,block1,px,py)==True:
            stopcounter1+=1#counter for collidedown 
        if collideDown(grid2,block2,px2,py2)==True:
            stopcounter2+=1#counter for collidedown
        if kocounter1>=1:
            kocounter1+=1
        if kocounter2>=1:
            kocounter2+=1
        if stopcounter1>=50:#adds adequate delay  
            if blockmoving(grid1,block1,px,py)==False:
                z=send(grid1,grid2,sent1,tempsend1)#parameters
                grid1=z[0]#1 item returned
                grid2=z[1]#2nd item returned
                tempsend1=sent1#needed for subtraction later
                newchie1=clear(grid1,grid2,block1,b1,sent1,tempsend1,combo1)#parameters for clear
                cleared1=newchie1[3]#4 item returned
                tempsend1=newchie1[2]#3rd
                sent1=newchie1[1]#2nd
                combo1=newchie1[0]#1st
                
                x=KO(grid1,block1,px,py,time)#parameters
                grid1=x[0]#1st item returned
                time=x[2]#3rd item returned
                if x[1]==True: #2nd item for KOing
                    delaytime=time
                    oldko2=KO2

                    screen.blit(kos[KO2],(426,235))#
                    KO2+=1
                    kocounter2+=1
                
                x=newBlock(grid1,block1,b1,nextlist1,piecelist1)#parameters
                b1=x[0]#item1
                block1=b1[0]#item1 in b1
                nextlist1=x[1]#item2
                piecelist1=x[2]#item3
                px=4#rests x and y
                py=-2
                stopcounter1=0#back to zero
        if stopcounter2>=50:#delay  
            if blockmoving(grid2,block2,px2,py2)==False:
                z=send(grid2,grid1,sent2,tempsend2)#parameters
                grid2=z[0]#1 item returned
                grid1=z[1]#2nd item returned
                tempsend2=sent2#needed for subtraction later              
                newchie2=clear(grid2,grid1,block2,b2,sent2,tempsend2,combo2)#parameters for clear
                cleared2=newchie2[3]#4th item returned
                tempsend2=newchie2[2]#3rd item returned
                sent2=newchie2[1]#2nd item returned
                combo2=newchie2[0]#1st item returned
                x=KO(grid2,block2,px2,py2,time)#parameters
                
                grid2=x[0]#1st item returned
                time=x[2]#3rd item returned 
                if x[1]==True:#2nd item, for kOing
                    delaytime=time 
                    oldko1=KO1

                    if x[1]==True:
                        delaytime=time

                        oldko1=KO1

                        screen.blit(kos[KO1],(44,235))
                        KO1+=1
                        kocounter1+=1


                x=newBlock(grid2,block2,b2,nextlist2,piecelist2)#parameters

                b2=x[0]#item1
                block2=b2[0]#item1 in b1
                nextlist2=x[1]#item2
                piecelist2=x[2]#item3
                px2=4#resets x and y
                py2=-2
                stopcounter2=0 #back to zero

        #parameters for getting position of
        #falling block
        positions1=getPositions(block1,px,py)
        positions2=getPositions(block2,px2,py2)     

        if movecounter==3:
             #done to eliminate the global aspect of px,py
             #yolo1 returns px,py,px2,py2
             yolo1 = moveLeft(px,py,px2,py2)
             px=yolo1[0]
             py=yolo1[1]
             px2=yolo1[2]
             py2=yolo1[3]
             #done to eliminate the global aspect of px,py
             #yolo1 returns px,py,px2,py2
             yolo2 = moveRight(px,py,px2,py2)
             px=yolo2[0]
             py=yolo2[1]
             px2=yolo2[2]
             py2=yolo2[3]
             movecounter=0
        if downcounter==2:
            #done to eliminate the global aspect of px,py
            #yolo1 returns px,py,px2,py2
            yolo3 = moveDown(px,py,px2,py2)
            px=yolo3[0]
            py=yolo3[1]
            px2=yolo3[2]
            py2=yolo3[3]
            downcounter=0
        
        
        if KO2-oldko2==1:
            b=screen.copy()
            screen.blit(ko,(140,233))
            display.flip()
            if kocounter2>=75:
                kocounter2=0
                oldko2=KO2
                time=delaytime
                screen.blit(b,(0,0))
                if KO2==3:
                    return [b,"endgame",2]
        #print KO1,oldko1

        if KO1-oldko1==1:
            
            a=screen.copy()
            screen.blit(ko,(527,233))
            
            display.flip()
            if kocounter1>=75:
                kocounter1=0
                oldko1=KO1
                time=delaytime
                screen.blit(a,(0,0))
                if KO1==3:
                    return [a,"endgame",1]
        else:
            drawScreen()
        display.flip()
        

        
        if time>=0:
            time-=timer2p.tick()
        else:
            a=screen.copy()
            if KO2>KO1: #Checks who is the winner of the game
                return [a,"endgame",2]#a is screebn.copy,endgame ends the game,2 is player 2 wins
            if KO1>KO2:
                return [a,"endgame",1]#a is screebn.copy,endgame ends the game,1 is player 1 wins
            if KO1==KO2:
                if sent2>sent1:
                    return [a,"endgame",2]#a is screebn.copy,endgame ends the game,2 is player 2 wins
                if sent1>sent2:
                    return [a,"endgame",1]#a is screebn.copy,endgame ends the game,1 is player 1 wins

        drawTime2p(time)
        if combo1-oldcombo1==1: #draws the combo picture
            drawCombo(combo1,164,190)
        if combo2-oldcombo2==1:
            drawCombo(combo2,535,190)
       
        

        #time goes until it hits zero
        #when it hits zero return endgame screen
        
        display.flip()
    quit()

#################################################################################


def viewmap():#viewmap function
    running = True
    #making it look nice
    back1 = image.load("menu pics/mainsetmap.png")
    outline = image.load("menu pics/outline.png")
#defining rectangles for collision checking
    map1= Rect(155,75,200,200)
    map2= Rect(439,75,200,200)
    map3= Rect(155,309,200,200)
    map4= Rect(439,309,200,200)
    buttons = [map1,map2,map3,map4]#preparing a buttons and names list to be zipped together
    names = ["none","classic","comboking","lunchbox"]# 
    screen.blit(back1,(0,0))#back1 is the main background
    while running:

        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        #print mpos

        #for b,n in zip(buttons,names): #zipping buttons and names together       
            #if b.collidepoint(mpos):   #for very easy collision checking            
                #if mb[0]==1:
                    

        #this chunk of code is just making pretty pictures       
        if map1.collidepoint(mpos):
            screen.blit(outline,(149,64))
        elif map2.collidepoint(mpos):
            screen.blit(outline,(431,64))
        elif map3.collidepoint(mpos):
            screen.blit(outline,(149,301))
        elif map4.collidepoint(mpos):
            screen.blit(outline,(431,301))
        else:
            screen.blit(back1,(0,0))#keeping it fresh
        display.flip() #necessities

    return "menu"


#instructions page
def instructions():
    back2 = image.load("menu pics/mainhelp.png")
    running =True
    screen.blit(back2,(0,0))
    #screen.blit(inst,(173,100))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        display.flip()
    return "menu"

#menu page
def menu (page):
    running = True
    myClock = time.Clock()
    button1 = Rect(320,204,146,50)#start rect
    buttons = [Rect(325,y*42+275,135,30) for y in range(3)]#other three rects 
    vals = ["viewmap","instructions","exit"]#values of other three rects
    intro = image.load("menu pics/intro screen.png")
    startbutton = image.load("menu pics/start.png")
    setmapbutton = image.load("menu pics/setmap.png")
    helpbutton = image.load("menu pics/help.png")
    quitbutton = image.load("menu pics/quit.png")
    
    screen.blit (intro,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "exit"
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        #print mpos

        #thank u for the code
        #zips button and vals and when
        #a collision and a click occurs
        #returns vals
        for r,v in zip(buttons,vals):
            if r.collidepoint(mpos):
                #print r,v
                if mb[0]==1:
                    return v#page to go to
       
        if button1.collidepoint(mpos):
            screen.blit(startbutton,(319,207))
            if mb[0]==1:
                return "start"#starting the game
            #making the game look pretty
        elif buttons[0].collidepoint(mpos):
            screen.blit(setmapbutton,(325,274))
        elif buttons[1].collidepoint(mpos):
            screen.blit(helpbutton,(325,317))
        elif buttons[2].collidepoint(mpos):
            screen.blit(quitbutton,(325,360))
            if mb[0]==1:
                return "exit"#quitting the game
        else:
            screen.blit(intro,(0,0))#reblit the background
        
        #draw.rect(screen,(0,0,0),button1,2)
        myClock.tick(50)            
        display.flip()

#endgame page
def endgame(a,winner):#parameters
    pics=[image.load("tetris icons/you win.png"),image.load("tetris icons/you lose.png")]
    transparent=image.load("tetris icons/transparent.png")#looking good
    counter=0
    #pretty stuff
    while True:
        counter+=1
        screen.blit(a,(0,0))
        screen.blit(transparent,(110,135))
        screen.blit(transparent,(494,135))
        screen.blit(pics[winner-1],(135,230))
        screen.blit(pics[(2-winner)],(500,230))
        display.flip()
        if counter==300:#time waiting
            return "menu"
#allowing for the menu to
#switch between pages 
page ="menu"
while page != "exit":
    if page == "menu":
        page = menu(page)
    if page == "start":
        x = start(myClock,timer2p)
        b=x[2]
        a=x[0]
        page=x[1]
    if page == "endgame":    
        page = endgame(a,b)
    if page == "viewmap":
        page = viewmap()    
    if page == "instructions":
        page = instructions()    
    if page == "quit":
        page = (page)    
    if page == "credits":
        page = credit(page)
quit()

