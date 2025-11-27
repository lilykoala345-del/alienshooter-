import random, pyautogui, pgzrun
WIDTH,HEIGHT= pyautogui.size()
print (pyautogui.size())
TITLE="cosmic rouge"
player=Actor("spaceship01")
player.pos=WIDTH//2,HEIGHT-150
by=-HEIGHT
foes=[]
ammo=[]
game=False
def draw():
    screen.blit("spacebg02",(0,by))
    player.draw()
    for i in foes:
        i .draw()
    for i in ammo:
        i.draw()
    if game:
        screen.draw.text("Game over!",center=(WIDTH/2,HEIGHT/2),fontsize=80)
def update():
    global by, game
    if not game:

        by+=1
        if by >0:
            by=-HEIGHT
        if keyboard.left:
            player.x-=10
        elif keyboard.right:
            player.x+=10
        
        if player.x<0:
            player.x=WIDTH
        if player.x>WIDTH:
            player.x=0
        for i in foes:
            i.y+=5
            if i.y>HEIGHT:
             foes.remove(i)
            for j in ammo:
                if i.colliderect(j):
                    ammo.remove(j)
                    foes.remove(i)
            if i.colliderect(player):
                game=True
                foes.remove(i)
        if keyboard.up:
            a=Actor("lazer")
            a.pos=player.x,player.y-50
            ammo.append(a)
        for i in ammo:
            i.y-=6
            if i.y<0:
                ammo.remove(i)   
      

def foe():
    foe=Actor("cyborgbug01")
    foe.pos=random.randint(50,WIDTH-50),0
    foes.append(foe)

clock.schedule_interval(foe,5.0)



pgzrun.go()