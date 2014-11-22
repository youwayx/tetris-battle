from pygame import*
screen = display.set_mode((800,600))

def menu (page):
    running = True
    myClock = time.Clock()
    buttons = [Rect(325,y*40+275,135,30) for y in range(3)]
    vals = ["setmap","help","quit"]
    intro = image.load("intro screen.png")
    screen.blit (intro,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "exit"
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        
        for b,v in zip(buttons,vals):
            draw.rect(screen,(0,0,0),r)
            if r.collidepoint(mpos):
                draw.rect(screen,(0,255,0),r,2)
                if mb[0]==1:
                    return v
            else:
                draw.rect(screen,(255,255,0),r,2)
                
        display.flip()
    
        
page = "menu"
while page != "exit":
    if page == "menu":
        page = menu(page)
    if page == "simple3D":
        page = simple3D(page)    
    if page == "instructions":
        page = instructions(page)    
    if page == "story":
        page = story(page)    
    if page == "credits":
        page = credit(page)
quit()
