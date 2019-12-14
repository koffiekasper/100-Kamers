kasperPlay = False
kasperMainMenu = True
kasperExit = False
kasperOptions = False

kasperTyping = False



kasperPlayer1Name = False
kasperPlayer2Name = False
kasperPlayer3Name = False
kasperPlayer4Name = False


player1Name = ""
player2Name = ""
player3Name = ""
player4Name = ""

playersPlaying = 1

def setup():
    global SimSun90, SimSun12
    size(1600,900)
    SimSun90 = createFont("SimSun", 90)
    SimSun12 = createFont("SimSun", 42)
    SimSun40 = createFont("SimSun", 90)
    
def keyTyped():
    global player1Name, player2Name, player3Name, player4Name
    if kasperPlayer1Name == True:
        if key == BACKSPACE and len(player1Name) >0:
            player1Name = player1Name[:-1]
        elif key != BACKSPACE:
            player1Name += key
    if kasperPlayer2Name == True:
        if key == BACKSPACE and len(player2Name) >0:
            player2Name = player2Name[:-1]
        elif key != BACKSPACE:
            player2Name += key
    if kasperPlayer3Name == True:
        if key == BACKSPACE and len(player3Name) >0:
            player3Name = player3Name[:-1]
        elif key != BACKSPACE:
            player3Name += key
    if kasperPlayer4Name == True:
        if key == BACKSPACE and len(player3Name) >0:
            player4Name = player4Name[:-1]
        elif key != BACKSPACE:
            player4Name += key

def draw():
    if kasperMainMenu == True:
        mainMenu()
    elif kasperOptions == True:
        options()
    elif kasperExit == True:
        exitMainMenu()
    elif kasperPlay == True:
        playgame()

    #DEBUG
    fill(255)
    # text(str(mouseX), 100, 100)
    # text(str(mouseY), 100, 200)
    # text(str(player1Name), 100, 300)


def playgame():
    global kasperMainMenu, kasperPlay, playersPlaying, kasperPlayer1Name, kasperPlayer2Name, kasperPlayer3Name, kasperPlayer4Name, player1Name, player2Name, player3Name, player4Name
    background(0)
    fill(255)
    textAlign(LEFT)
    text("Number of players", 190, 100)   
    #EXIT BUTTON
    if 1140<mouseX<1340 and 720<mouseY< 770:
        fill(255)
        rect(1137, 717, 206, 56)
        if mousePressed == True:
            player1Name = ""
            player2Name = ""
            player3Name = ""
            player4Name = ""
            playersPlaying = 1
            kasperMainMenu = True
            kasperPlay = False
    #PLAY BUTTON
    if 200 < mouseX < 550 and 570 < mouseY < 770:
        if frameCount % 60 <= 20:
            fill(255, 0, 0)
        elif frameCount % 60 <= 40:
            fill(0, 255, 0)
        else:
            fill(0,0,255)
        
        rect(190, 560, 370, 220)
        fill(255)
               
    if mouseX > 200 and mouseX < 300 and mouseY > 150 and mouseY < 470:
        fill(255)
        rect(197, 147, 106, 56)
        fill(80)
        rect(200, 150, 100, 320)
        fill(255)
        if 225 < mouseX < 275 and 205 < mouseY < 245:
            rect(223, 203, 54, 44)
        if 225 < mouseX < 275 and 275 < mouseY < 315:
            rect(223, 273, 54, 44)
        if 225 < mouseX < 275 and 345 < mouseY < 385:
            rect(223, 343, 54, 44)
        if 225 < mouseX < 275 and 415 < mouseY < 455:
            rect(223, 413, 54, 44)
        fill(90)
        rect(225, 205, 50, 40)
        rect(225, 275, 50, 40)
        rect(225, 345, 50, 40)
        rect(225, 415, 50, 40)
        fill(255)
        textAlign(CENTER)
        text("1", 250, 240)
        text("2", 250, 310)
        text("3", 250, 380)
        text("4", 250, 450)

        if mousePressed == True:
            if 225 < mouseX < 275 and 205 < mouseY < 245:
                playersPlaying = 1
            if 225 < mouseX < 275 and 275 < mouseY < 315:
                playersPlaying = 2
            if 225 < mouseX < 275 and 345 < mouseY < 385:
                playersPlaying = 3
            if 225 < mouseX < 275 and 415 < mouseY < 455:
                playersPlaying = 4
                
    if playersPlaying >= 1:
        if 340 < mouseX < 1240 and 150 < mouseY < 200:
            kasperPlayer1Name = True
            fill(255)
            rect(335, 145, 910, 60)
        else:
            kasperPlayer1Name = False
        if 1290 < mouseX < 1340 and 150 < mouseY < 200:
            fill(255)
            rect(1287, 147, 56, 56)
            if mousePressed == True:
                player1Name = ""
        fill(80)    
        rect(340, 150, 900, 50)

        rect(1290, 150, 50, 50)

        fill(255)
        textAlign(LEFT)
        text(player1Name, 400, 184)
        
    if playersPlaying >= 2:
        if 340 < mouseX < 1240 and 250 < mouseY < 300:
            kasperPlayer2Name = True
            fill(255)
            rect(335, 245, 910, 60)
        else: 
            kasperPlayer2Name = False
        if 1290 < mouseX < 1340 and 250 < mouseY < 300:
            fill(255)
            rect(1287, 247, 56, 56)
            if mousePressed == True:
                player2Name = ""
        fill(80)
        rect(340, 250, 900, 50)
        rect(1290, 250, 50, 50)
        fill(255)
        textAlign(LEFT)
        text(player2Name, 400, 284)        
        
    if playersPlaying >= 3:
        if 340 < mouseX < 1240 and 350 < mouseY < 400:
            kasperPlayer3Name = True
            fill(255)
            rect(335, 345, 910, 60)
        else:
            kasperPlayer3Name = False

        if 1290 < mouseX < 1340 and 350 < mouseY < 400:
            fill(255)
            rect(1287, 347, 56, 56)
            if mousePressed == True:
                player3Name = ""
            
        fill(80)
        rect(340, 350, 900, 50)
        rect(1290, 350, 50, 50)
        fill(255)
        textAlign(LEFT)
        text(player3Name, 400, 384)      
          
    if playersPlaying >= 4:
        if 340 < mouseX < 1240 and 450 < mouseY < 500:
            kasperPlayer4Name = True
            fill(255)
            rect(335, 445, 910, 60)
        else:
            kasperPlayer4Name = False
        if 1290 < mouseX < 1340 and 450 < mouseY < 500:
            fill(255)
            rect(1287, 447, 56, 56)
            if mousePressed == True:
                player4Name = ""
        fill(80)
        rect(340, 450, 900, 50)
        rect(1290, 450, 50, 50)
        fill(255)
        textAlign(LEFT)
        text(player4Name, 400, 484)
        
    textAlign(CENTER)            
    fill(100)
    rect(200, 150, 100, 50)
    rect(1140, 720 , 200, 50)
    rect(200, 570, 350, 200)
    fill(255)
    text("RETURN", 1230, 760)
    textFont(SimSun90)
    text("PLAY!", 375, 700)
    textFont(SimSun12)
    fill(50)
    triangle(235, 165, 265, 165, 250, 185)
    
    




def options():
    global kasperOptions, kasperMainMenu
    background(0)

    if mouseX > 1300 and mouseX < 1500 and mouseY > 700 and mouseY < 800:
        fill(255)
        rect(1290, 690, 220, 120)
        if mousePressed == True:
            kasperMainMenu = True
            kasperOptions = False

    fill(100)
    rect(1300, 700, 200, 100)

    fill(255)
    SimSun12 = createFont("SimSun", 42)
    textFont(SimSun12)
    textAlign(CENTER)
    text("RETURN", 1400, 770)    




def exitMainMenu():
    global kasperMainMenu, kasperExit
    background(0)

    fill(150)
    rect(400, 300, 800, 400)
    
    fill(255)
    if mouseX > 450 and mouseX < 550 and mouseY > 600 and mouseY < 670:
        rect(440, 590, 120, 90)
        if mousePressed == True:
            exit()
    
    if mouseX > 1050 and mouseX < 1150 and mouseY > 600 and mouseY < 670:
        rect(1040, 590, 120, 90)
        if mousePressed == True:
            kasperMainMenu = True
            kasperExit = False    

    fill(100)
    rect(450, 600, 100, 70)
    rect(1050, 600, 100, 70)
    
    fill(255)
    SimSun12 = createFont("SimSun", 42)
    textFont(SimSun12)
    textAlign(CENTER, CENTER)
    text("YES", 500, 630)
    text("NO", 1100, 630)
    text("Are you sure you want to exit?", 800, 400)
    





def mainMenu():
    global kasperExit, kasperOptions, kasperPlay, kasperMainMenu
    background(0)
    fill(255)
    
    if mouseX > 600 and mouseX < 1000 and mouseY > 350 and mouseY < 450:
        rect(590, 340, 420, 120)
        if mousePressed == True:
            kasperPlay = True
            kasperMainMenu = False

    if mouseX > 600 and mouseX < 1000 and mouseY > 500 and mouseY < 600:
        rect(590, 490, 420, 120)
        if mousePressed == True:
            kasperOptions = True
            kasperMainMenu = False
            
    if mouseX > 600 and mouseX < 1000 and mouseY > 650 and mouseY < 750:
        rect(590, 640, 420, 120)
        if mousePressed == True:
            kasperExit = True
            kasperMainMenu = False


    fill(100)
    rect(600, 350, 400, 100)
    rect(600, 500, 400, 100)
    rect(600, 650, 400, 100)
    fill(255)
    # # if frameCount % 60 <= 10:
    # #     fill(255,0,0)
    # if frameCount % 60 <= 20:
    #     fill(255,153,51)
    # elif frameCount % 60 <= 30:
    #     fill (255,153,51)
    # # elif frameCount % 60 <= 40:
    # #     fill(255)
    # # elif frameCount % 60 <= 45:
    # #     fill(153,0,0)    
    # elif frameCount % 60 <= 50:
    #     fill(255,52,0)
    SimSun40 = createFont("SimSun", 90)
    textFont(SimSun40)
    text("100 KAMERS", 800, 200)
    fill(255)


    textFont(SimSun12)
    textAlign(CENTER)
    text("PLAY", 800, 420)
    text("EXIT", 800, 710)
    text("CREDITS", 800, 560)    
