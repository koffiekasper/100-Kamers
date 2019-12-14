lootLevel = 2
rng = 0

def setup():
    global Harrington40, Harrington80, Harrington160, weaponArmorLoot, spellCardLoot, pickKindMenu, rngGenerated, Harrington180
    size(1600, 900)
    Harrington40 = createFont("Harrington", 40)
    Harrington80 = createFont("Harrington", 80)
    Harrington160 = createFont("Harrington", 160)
    Harrington180 = createFont("Harrington", 180)
    weaponArmorLoot = False
    spellCardLoot = False
    pickKindMenu = True
    rngGenerated = False

        
def mouseClicked():
    global rng, rngGenerated
    if 970<mouseX<1270 and 250<mouseY<750 and rngGenerated != True:
        rng = int(random(1, 14))
        rngGenerated = True
        
def draw():
    global pickKindMenu
    if weaponArmorLoot == True:
        weaponLoot()
    elif spellCardLoot == True:
        spellLoot()
    elif pickKindMenu == True:
        pickKind()
    textFont(Harrington40)
    text(mouseX, 100,100)
    text(mouseY,100,200)
    
    
    
def pickKind():
    global weaponArmorLoot, spellCardLoot
    background(0)
    
    fill(255)
    textFont(Harrington80)
    textAlign(CENTER)
    text("Pick your loot...", 800, 200)

    rgblight()
    if 970<mouseX<1270 and 250<mouseY<750:
        rect(965, 245, 310, 510)
        if mousePressed:
            spellCardLoot = True
            pickKindMenu = False
    if 330<mouseX<630 and 250<mouseY<750:
        rect(325, 245, 310, 510)    
        if mousePressed:
            weaponArmorLoot = True
            pickKindMenu = False
    
    fill(80)
    rect(330, 250, 300, 500)
    rect(970, 250, 300, 500)
    fill(255)
    text("lvl " + str(lootLevel), 430, 700)
    text("Spell",1070, 700)
    
    
def weaponLoot():
    global pickKindMenu, weaponArmorLoot
    background(0)
    
    rgblight()
    if 350<mouseX<750 and 100<mouseY<800:
        rect(345, 95, 410, 710)
    if 850<mouseX<1250 and 100<mouseY<800:
        rect(845,95,410,710)
    if 1300<mouseX<1550 and 650<mouseY<800:
        rect(1295,645,260,160)
        if mousePressed:
            weaponArmorLoot = False

    if 50<mouseX<330 and 500<mouseY<800:
        rect(45,495,280,310)
    
    fill(80)
    rect(350, 100, 400, 700)
    rect(850, 100, 400, 700)
    rect(1300, 650, 250, 150)
    rect(50, 500, 270, 300)
    
    fill(200)
    textFont(Harrington80)
    textAlign(CENTER)
    text("BACK", 1420, 750)
    textFont(Harrington160)
    text(lootLevel, 1420, 550)
    textFont(Harrington40)
    text("Loot level:", 1420, 400)
    text("View inventory", 185, 550)
    text("Weapon", 550, 260)
    text("Armor", 1050, 260)
    
    
    
def spellLoot():
    background(0)
        
    fill(80)
    rect(600, 100, 400, 700)
    
    rgblight()
    if 660<mouseX<940 and 625<mouseY<725:
        rect(655, 620, 290, 110)
        if mousePressed:
            pass
            
    fill(55,27,7)
    rect(660, 625 , 280, 100)
    
    fill(255)
    textFont(Harrington160)
    text(rng,800, 500)
    textFont(Harrington80)
    text("OKAY!", 800,700)

def rgbflame():
    if frameCount % 60 <= 30:
        fill(89,35,13)
    else:
        fill(89,72,13)
    
def rgblight():
    if frameCount % 60 <= 20:
        fill(255,255,0)
    elif frameCount % 60 <= 40:
        fill(255,128,0)
    else:
        fill(255,0,0)
