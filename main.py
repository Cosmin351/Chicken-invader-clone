import pygame
import Obiecte
import Colors
import random
import time
from Colors import Developer
from pygame import mixer

pygame.init()
mixer.init()

def drawBackground():
    global Ecran, BackgroundSpeed, Background, BackgroundText
    Ecran.blit(Background, (0,BackgroundSpeed))
    Ecran.blit(Background, (0,-Height + BackgroundSpeed))
    if Background == Background1:
        Ecran.blit(BackgroundText,(Width/2-250/2,Height//3))
    if Background == Background2:
        BackgroundSpeed += 1.25
    else:
        BackgroundSpeed += 0.25
    if BackgroundSpeed == Height:
        BackgroundSpeed = 0

def drawButtonsMain():
    global ButtonsMain, MMtext
    for Button in ButtonsMain:
        if (Button.CursorTrigx < pos[0] < Button.CursorTrigx + Button.sizex and
                Button.CursorTrigy < pos[1] < Button.CursorTrigy + Button.sizey):
            Button.draw(Ecran, True)
        else:
            Button.draw(Ecran, False)
    MMtext.draw(Ecran,'main menu')

def drawButtonsOptions():
    global ButtonsOption, Optiontext, Music, Effects, Imgbif
    for Button in ButtonsOption:
        if (Button.CursorTrigx < pos[0] < Button.CursorTrigx + Button.sizex and
                Button.CursorTrigy < pos[1] < Button.CursorTrigy + Button.sizey):
            Button.draw(Ecran, True)
        else:
            Button.draw(Ecran, False)
    if Music:
        Ecran.blit(Imgbif,(ButtonsOption[1].CursorTrigx,ButtonsOption[1].CursorTrigy))
    if Effects:
        Ecran.blit(Imgbif,(ButtonsOption[2].CursorTrigx,ButtonsOption[2].CursorTrigy))
    Optiontext.draw(Ecran,'options')

def drawButtonsStart():
    global ButtonsStart, Imgbif, Ecran, MyCareer
    if Choosed:
        ButtonsStart[2].Text.color = Colors.MidDarkGrey
        ButtonsStart[2].color = Colors.DarkPurple
        ButtonsStart[4].Text.color = Colors.MidDarkGrey
        ButtonsStart[4].color = Colors.DarkPurple
        ButtonsStart[5].Text.color = Colors.MidDarkGrey
        ButtonsStart[5].color = Colors.DarkPurple
        ButtonsStart[6].Text.color = Colors.MidDarkGrey
        ButtonsStart[6].color = Colors.DarkPurple

    for Button in ButtonsStart:
        if (Button.CursorTrigx < pos[0] < Button.CursorTrigx + Button.sizex and
                Button.CursorTrigy < pos[1] < Button.CursorTrigy + Button.sizey):
            Button.draw(Ecran, True)
        else:
            Button.draw(Ecran, False)

    if not Choosed:
        ButtonsStart[2].Text.color = Colors.White
        ButtonsStart[2].color = Colors.ButtonPurple
        ButtonsStart[4].Text.color = Colors.White
        ButtonsStart[4].color = Colors.ButtonPurple
        ButtonsStart[5].Text.color = Colors.White
        ButtonsStart[5].color = Colors.ButtonPurple
        ButtonsStart[6].Text.color = Colors.White
        ButtonsStart[6].color = Colors.ButtonPurple 
    if not MyCareer:
        ButtonsStart[3].Text.color = Colors.MidDarkGrey
        ButtonsStart[3].color = Colors.DarkPurple
        ButtonsStart[3].draw(Ecran, False)
    else:
        ButtonsStart[3].Text.color = Colors.White
        ButtonsStart[3].color = Colors.ButtonPurple
    if Rookie and not Choosed:
        Ecran.blit(Imgbif,(ButtonsStart[4].CursorTrigx,ButtonsStart[4].CursorTrigy))
    if Veteran and not Choosed:
        Ecran.blit(Imgbif,(ButtonsStart[5].CursorTrigx,ButtonsStart[5].CursorTrigy))
    if not Choosed:
        Ecran.blit(Imgbif,(ButtonsStart[2].CursorTrigx,ButtonsStart[2].CursorTrigy))
    else:
        Ecran.blit(Imgbif,(ButtonsStart[3].CursorTrigx,ButtonsStart[3].CursorTrigy))

def drawPause():
    pygame.draw.rect(Ecran, Colors.ButtonPurple, pygame.Rect(Width/2 - Width/10, Height/2 - 35/2*Height/100, 20*Width/100, 35*Height/100), 0, 15)
    pygame.draw.rect(Ecran, Colors.MidLightBlue, pygame.Rect(Width/2 - Width/10, Height/2 - 35/2*Height/100, 20*Width/100, 35*Height/100), 5, 15)
    for ButtonPause in ButtonsPause:
        if (ButtonPause.CursorTrigx < pos[0] < ButtonPause.CursorTrigx + ButtonPause.sizex and
                ButtonPause.CursorTrigy < pos[1] < ButtonPause.CursorTrigy + ButtonPause.sizey):
            ButtonPause.draw(Ecran, True)
        else:
            ButtonPause.draw(Ecran, False)

def drawControls():
    pygame.draw.rect(Ecran, Colors.ButtonPurple, pygame.Rect(Width/2 - Width/10, Height/2 - 35/2*Height/100, 20*Width/100, 35*Height/100), 0, 15)
    pygame.draw.rect(Ecran, Colors.MidLightBlue, pygame.Rect(Width/2 - Width/10, Height/2 - 35/2*Height/100, 20*Width/100, 35*Height/100), 5, 15)
    if (ButtonsControls[0].CursorTrigx < pos[0] < ButtonsControls[0].CursorTrigx + ButtonsControls[0].sizex and
        ButtonsControls[0].CursorTrigy < pos[1] < ButtonsControls[0].CursorTrigy + ButtonsControls[0].sizey):
        ButtonsControls[0].draw(Ecran, True)
    else:
        ButtonsControls[0].draw(Ecran, False)
    TextControls[0].draw(Ecran , 'Shoot -> Left Click')
    TextControls[1].draw(Ecran , 'Rocket -> Right Click')

def drawGUIGame():
    global Progress, Progress2
    pygame.draw.rect(Ecran, Colors.MidDarkBlue, pygame.Rect(-4, -4, 25*Width/100, 6*Height/100), 0, border_bottom_right_radius = 15)
    pygame.draw.rect(Ecran, Colors.MidLightBlue, pygame.Rect(-4, -4, 25*Width/100, 6*Height/100), 4, border_bottom_right_radius = 15)

    pygame.draw.rect(Ecran, Colors.MidDarkBlue, pygame.Rect(-4, Height - 5*Height/100 + 4 , 18*Width/100, 5*Height/100), 0, border_top_right_radius = 15)
    pygame.draw.rect(Ecran, Colors.MidLightBlue, pygame.Rect(-4, Height - 5*Height/100 + 4, 18*Width/100, 5*Height/100), 4, border_top_right_radius = 15)
    Ecran.blit(IconHeart,[1*Width/100,Height- 3*Height/100])
    Ecran.blit(IconRocket,[5*(1*Width/100),Height- 3*Height/100])
    Ecran.blit(IconThunder,[9*(1*Width/100),Height- 3*Height/100])
    Ecran.blit(IconLegChicken,[13*(1*Width/100),Height- 3*Height/100])
    i = 0
    PScore[7].draw(Ecran)
    if Progress:
        PGbar.txt = str(int(((Progress - Progress2)*100)/Progress))
        PGbar.draw(Ecran)
    for TextG in TextGUI:
        TextG.draw(Ecran,str(PScore[i]))
        i += 1

def drawWaveText():
    global Wave
    WaveText.draw(Ecran, 'Wave ' + str(Wave))

def drawCarrerSelect():
    pygame.draw.rect(Ecran, Colors.ButtonPurple, pygame.Rect(Width/2 - Width/10, Height/2 - 35/2*Height/100, 20*Width/100, 35*Height/100), 0, 15)
    pygame.draw.rect(Ecran, Colors.MidLightBlue, pygame.Rect(Width/2 - Width/10, Height/2 - 35/2*Height/100, 20*Width/100, 35*Height/100), 5, 15)
    for ButtonSaves in ButtonsSaves:
        if (ButtonSaves.CursorTrigx < pos[0] < ButtonSaves.CursorTrigx + ButtonSaves.sizex and
                ButtonSaves.CursorTrigy < pos[1] < ButtonSaves.CursorTrigy + ButtonSaves.sizey):
            ButtonSaves.draw(Ecran, True)
        else:
            ButtonSaves.draw(Ecran, False)
        if ButtonSaves == Obiectcopy and ButtonSaves != ButtonsSaves[0] and ButtonSaves != ButtonsSaves[1]:
            Ecran.blit(Imgbif,(ButtonSaves.CursorTrigx,ButtonSaves.CursorTrigy))

def addChickens(Nr, NumberChick, Direction, xpos, ypos, Row, Nr2, move):
    global Progress
    List = []
    xp = 10
    if NumberChick == 6:
        yp = 10
    else:
        yp = 5
    if NumberChick > 10:
        olimit = 0
        nrx = 1
    else:
        olimit = Width/100
        nrx = 3
    xlimit = Width
    for i in range(Nr):
        if Direction == 1:
            List.append(Obiecte.Chicken(0 - i*50, Height/12, 4, 4 , Width, Height, NumberChick, xp*xpos, yp*Height/100 + ypos, move, xlimit, olimit))
        elif Direction == 2:    
            List.append(Obiecte.Chicken(Width + i*75, Height/12, 4, 4 , Width, Height, NumberChick, xp*xpos, yp*Height/100 + ypos, move, xlimit, olimit))
        elif Direction == 3:
            List.append(Obiecte.Chicken(0 + i*50, -random.randint(Height/6, Height/4) , 4, 4 , Width, Height, NumberChick, xp*xpos, yp*Height/100 + ypos, move, xlimit, olimit))
        if len(List) == 1:
            List[0].xlimit = olimit + List[0].Lenx + nrx*Width/100
            xlimit = olimit + List[0].Lenx + nrx*Width/100
        olimit += List[0].Lenx + nrx*Width/100
        xlimit = olimit + nrx*Width/100 + List[0].Lenx
        if Row:
            if (i+1)%Nr2 == 0:
                xp += 10
                if NumberChick == 6:
                    yp = 10
                else:
                    yp = 5
            elif NumberChick == 6:
                yp += 15
            else:
                yp += 10
            if NumberChick == 1:
                Progress += 800
            elif NumberChick == 5:
                Progress += 400
            elif NumberChick == 6:
                Progress += 1400
            elif NumberChick == 4:
                Progress += 1200
            elif NumberChick == 3:
                Progress += 2000
            elif NumberChick == 11:
                Progress += 2000
            elif NumberChick == 7:
                Progress += 4000
            elif NumberChick == 12:
                Progress += 3500
    return List

def drawEggs():
    global SShipHITBOXx, Dead
    for Egg in Eggs:
        if SpaceShip.posx < Egg.posx < SpaceShip.posx + SpaceShip.Lenx or SpaceShip.posx< Egg.posx + Egg.EggLenx < SpaceShip.posx + SpaceShip.Lenx:
            if SpaceShip.posy < Egg.posy < SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy < Egg.posy + Egg.EggLeny < SpaceShip.posy + SpaceShip.Leny:
                PScore[0] -= 1
                Eggs.remove(Egg)
                Dead = True
        if Egg.posy > Height:
            Eggs.remove(Egg)
        else:
            Egg.draw(Ecran)              

def drawChickens():
    global Dead, seconds, SSpawn, SShipHITBOXx, SShipHITBOXy, Progress2, EffectSize, PScore, Gift
    for Chicken in Chickens:
            Progress2 += Chicken.Health
            if not Dead:
                if Chicken.posx <= SpaceShip.posx <= Chicken.posx + Chicken.Lenx or Chicken.posx <= SpaceShip.posx + SpaceShip.Lenx <= Chicken.posx + Chicken.Lenx:
                    if SpaceShip.posy <= Chicken.posy <= SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy <= Chicken.posy + Chicken.Leny <= SpaceShip.posy + SpaceShip.Leny:
                        PScore[0] -= 1
                        Dead = True
            if EffectSize:
                if Width/2 - EffectSize < Chicken.posx < Width/2 + EffectSize or Width/2 - EffectSize < Chicken.posx + Chicken.Lenx< Width/2 + EffectSize:
                    rand = random.randint(0,11)
                    if 10 > rand > 2:
                        ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, 2))
                    elif rand < 2:
                        ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, 3))
                    elif rand == 10:
                        ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, 4))                            
                        if Effects:
                            SoundUp.play()
                    elif rand == 11:
                        if random.randint(1,2) == 2 and not Gift:
                            Gift = True
                            while True:
                                z = random.randint(6, 8)
                                if Weapon1.number == 1 and z != 6:
                                    ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, z))
                                    break
                                elif Weapon1.number == 2 and z != 7:
                                    ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, z))
                                    break
                                elif Weapon1.number == 3 and z != 8:
                                    ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, z))
                                    break
                    PScore[4] += 500
                    Chickens.remove(Chicken)
                    if Effects:
                        SoundChicken.play()                
            Chicken.draw(Ecran)
    for Chicken in Chickens:
        for Chicken2 in Chickens:
            if Chicken == Chicken2:
                continue
            if Chicken.posx <= Chicken2.posx <= Chicken.posx + Chicken.Lenx or Chicken.posx <= Chicken2.posx + Chicken2.Lenx <= Chicken.posx + Chicken.Lenx:
                if Chicken2.posy <= Chicken.posy <= Chicken2.posy + Chicken2.Leny or Chicken2.posy <= Chicken.posy + Chicken.Leny <= Chicken2.posy + Chicken2.Leny:
                    if Chicken.xfloat == -1:
                        Chicken.xfloat = 1
                        break
                    else:
                        Chicken.xfloat = 1
                        break

def drawChickenBoss():
    global Dead, ChickenBoss, PScore, Progress2
    for ChickBoss in ChickenBoss:
        Progress2 += ChickBoss.Health
        if not Dead:
            if ChickBoss.posx <= SpaceShip.posx <= ChickBoss.posx + ChickBoss.Lenx or ChickBoss.posx <= SpaceShip.posx + SpaceShip.Lenx <= ChickBoss.posx + ChickBoss.Lenx:
                if SpaceShip.posy <= ChickBoss.posy <= SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy <= ChickBoss.posy + ChickBoss.Leny <= SpaceShip.posy + SpaceShip.Leny:
                            PScore[0] -= 1
                            Dead = True
        ChickBoss.draw(Ecran)

def drawWeaponBullets():
    global Dead, seconds, SSpawn, ChickenBoss, Up, Gift
    if Weapon1.Bullets:
        for Bullet in Weapon1.Bullets:
            for Chicken in Chickens:
                if Chicken.posx <= Bullet.posx <= Chicken.posx + Chicken.Lenx or Chicken.posx <= Bullet.posx + Bullet.Lenx <= Chicken.posx + Chicken.Lenx:
                    if Chicken.posy <= Bullet.posy <= Chicken.posy + Chicken.Leny:
                        try:
                            Weapon1.Bullets.remove(Bullet)
                        except:
                            pass
                        Chicken.Health -= Weapon1.damage
                        if Chicken.Health < 0:
                            if Chicken.number == 11 or Chicken.number == 12:
                                Chickens.remove(Chicken)
                                if Effects:
                                    SoundChicken.play()  
                                break
                            rand = random.randint(0,11)
                            if 10 > rand > 2:
                                ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, 2))
                            elif rand < 2:
                                ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, 3))
                            elif rand == 10 and not Up:
                                Up = True
                                if Effects:
                                    SoundUp.play()
                                ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, 4))
                            elif rand == 11:
                                if random.randint(1,2) == 2 and not Gift:
                                   Gift = True
                                   while True:
                                    z = random.randint(6, 8)
                                    if Weapon1.number == 1 and z != 6:
                                        ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, z))
                                        break
                                    elif Weapon1.number == 2 and z != 7:
                                        ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, z))
                                        break
                                    elif Weapon1.number == 3 and z != 8:
                                        ChickenDrop.append(Obiecte.ChickenDrop(Chicken.posx  - Width/100,Chicken.posy , Width, Height, z))
                                        break
                            Chickens.remove(Chicken)
                            if Effects:
                                SoundChicken.play()  
                            PScore[4] += 500
            for Asteroid in Asteroids:
                if Asteroid.posx <= Bullet.posx <= Asteroid.posx + Asteroid.x*Width/100 or Asteroid.posx <= Bullet.posx + Width/75 <= Asteroid.posx + Asteroid.x*Width/100:
                    if Asteroid.posy <= Bullet.posy <= Asteroid.posy + Asteroid.x*Height/100:
                        Asteroid.health -= Weapon1.damage
                        if Asteroid.health < 0:
                            Asteroids.remove(Asteroid)
                        try:
                            Weapon1.Bullets.remove(Bullet)
                        except:
                            pass
            for ChickBoss in ChickenBoss:
                    if ChickBoss.posx <= Bullet.posx <= ChickBoss.posx + ChickBoss.Lenx or ChickBoss.posx <= Bullet.posx + Width/75 <= ChickBoss.posx + ChickBoss.Lenx:
                        if ChickBoss.posy <= Bullet.posy <= ChickBoss.posy + ChickBoss.Leny:
                            ChickBoss.Health -= Weapon1.damage
                            if ChickBoss.Health <0:
                                for i in range(5):
                                    rand = random.randint(0,10)
                                    if 10 > rand > 2:
                                        ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, 2))
                                    elif rand < 2:
                                        ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, 3))
                                    elif rand == 10:
                                        ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, 4))
                                        if Effects:
                                            SoundUp.play()
                                ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, 5))
                                while True:
                                    z = random.randint(6, 8)
                                    if Weapon1.number == 1 and z != 6:
                                        ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, z))
                                        break
                                    elif Weapon1.number == 2 and z != 7:
                                        ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, z))
                                        break
                                    elif Weapon1.number == 3 and z != 8:
                                        ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, z))
                                        break
                                ChickenBoss.remove(ChickBoss)
                                if Effects:
                                    SoundChicken.play()  
                            try:
                                Weapon1.Bullets.remove(Bullet)
                            except:
                                pass    
    Weapon1.draw(Ecran)

def drawChickenDrops():
    global Gift
    for Drop in ChickenDrop:
        if Drop.number == 2:
            if SpaceShip.posx < Drop.posx < SpaceShip.posx + SpaceShip.Lenx or SpaceShip.posx < Drop.posx + Width/40 < SpaceShip.posx + SpaceShip.Lenx:
                if SpaceShip.posy < Drop.posy < SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy < Drop.posy + Height/20 < SpaceShip.posy + SpaceShip.Leny:
                    ChickenDrop.remove(Drop)
                    PScore[4] += 200
                    PScore[3] += 1
        elif Drop.number == 3:
            if SpaceShip.posx < Drop.posx < SpaceShip.posx + SpaceShip.Lenx or SpaceShip.posx < Drop.posx + Width/40 < SpaceShip.posx + SpaceShip.Lenx:
                if SpaceShip.posy < Drop.posy < SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy < Drop.posy + Height/20 < SpaceShip.posy + SpaceShip.Leny:
                    ChickenDrop.remove(Drop)
                    PScore[4] += 500
                    PScore[3] += 3
        elif Drop.number == 4:
            if SpaceShip.posx < Drop.posx < SpaceShip.posx + SpaceShip.Lenx or SpaceShip.posx < Drop.posx + Width/40 < SpaceShip.posx + SpaceShip.Lenx:
                if SpaceShip.posy < Drop.posy < SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy < Drop.posy + Height/20 < SpaceShip.posy + SpaceShip.Leny:
                    ChickenDrop.remove(Drop)
                    Up = True
                    PScore[2] += 1
        elif Drop.number == 5:
            if SpaceShip.posx < Drop.posx < SpaceShip.posx + SpaceShip.Lenx or SpaceShip.posx < Drop.posx + Width/40 < SpaceShip.posx + SpaceShip.Lenx:
                if SpaceShip.posy < Drop.posy < SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy < Drop.posy + Height/20 < SpaceShip.posy + SpaceShip.Leny:
                    ChickenDrop.remove(Drop)
                    PScore[4] += 2000
        elif Drop.number == 6:
            if SpaceShip.posx < Drop.posx < SpaceShip.posx + SpaceShip.Lenx or SpaceShip.posx < Drop.posx + Width/40 < SpaceShip.posx + SpaceShip.Lenx:
                if SpaceShip.posy < Drop.posy < SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy < Drop.posy + Height/20 < SpaceShip.posy + SpaceShip.Leny:
                    Weapon1.number = 1
                    ChickenDrop.remove(Drop)
                    Gift = True
        elif Drop.number == 7:
            if SpaceShip.posx < Drop.posx < SpaceShip.posx + SpaceShip.Lenx or SpaceShip.posx < Drop.posx + Width/40 < SpaceShip.posx + SpaceShip.Lenx:
                if SpaceShip.posy < Drop.posy < SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy < Drop.posy + Height/20 < SpaceShip.posy + SpaceShip.Leny:
                    Weapon1.number = 2
                    ChickenDrop.remove(Drop)
                    Gift = True
        elif Drop.number == 8:
            if SpaceShip.posx < Drop.posx < SpaceShip.posx + SpaceShip.Lenx or SpaceShip.posx < Drop.posx + Width/40 < SpaceShip.posx + SpaceShip.Lenx:
                if SpaceShip.posy < Drop.posy < SpaceShip.posy + SpaceShip.Leny or SpaceShip.posy < Drop.posy + Height/20 < SpaceShip.posy + SpaceShip.Leny:
                    Weapon1.number = 3
                    ChickenDrop.remove(Drop)
                    Gift = True            
        if Drop.number == 4 or Drop.number == 6 or Drop.number == 7 or Drop.number == 8:
            pass
        elif Drop.posy > Height - Height/11 and Drop.velo > 0 and Drop.y_speed > 0 and Drop.fall:
            Drop.y_speed -= 1
            Drop.y_speed *= -1
            Drop.fall = False
        elif not Drop.fall and Drop.y_speed < 0:
            Drop.y_speed += 0.05 * Drop.velo
        elif Drop.posy < Height - Height/11:
            Drop.fall = True
            Drop.y_speed += 0.025 * Drop.velo
        elif Drop.posy > Height - Height/11:
            Drop.y_speed = 0
        if PScore[3] > 50:
            PScore[1] +=1
            PScore[3] = 0
        Drop.draw(Ecran)

def drawRocketExp():
    global EffectSize, RocketEffect, xRocket, yRocket
    if EffectSize < 2*Height:
        EffectSize += 7
    else:
        EffectSize = 0
        RocketEffect = False
    pygame.draw.circle(Ecran, Colors.LightOrange, [xRocket ,yRocket], EffectSize, 10)

def AsteroidSpawn(number1 ,number):
    global Asteroids, LevelDraw, Aster
    for i in range(random.randrange(4)):
        Asteroids.append(Obiecte.Asteroids(Width, Height, number1, number))
    LevelDraw = True

def drawAsteroidWave():
    global Dead, seconds, SSpawn
    for Asteroid in Asteroids:
        if not Dead:
            if Asteroid.posx <= SpaceShip.posx <= Asteroid.posx + Asteroid.x*Width/100 or Asteroid.posx <=  SpaceShip.posx + SpaceShip.Lenx <= Asteroid.posx + Asteroid.x*Width/100:
                if Asteroid.posy <= SpaceShip.posy <= Asteroid.posy + Asteroid.x*Height/100 or Asteroid.posy <= SpaceShip.posy + SpaceShip.Leny <= Asteroid.posy + Asteroid.x*Height/100:
                    PScore[0] -= 1
                    Dead = True
        Asteroid.draw(Ecran)
        if Asteroid.posy > Height:
            Asteroids.remove(Asteroid)

def drawStart():
    global Dead, Endgame, Main, LevelDraw, Pause, StartPlay, Progress2, ChickenBoss, Startticks2, seconds2, Asteroids, AsteroidSpwn, Wave, WaveUp, LevelLoad, seconds, SSpawn, RocketCoolDown, SShipHITBOXy, SShipHITBOXx, Chickens, RocketEffect, xRocket, yRocket
    if Endgame:
        Background = Background1
        Main = True
        LevelDraw = False
        Pause = False
        StartPlay = False
        return 0
    if not Dead:
        SpaceShip.draw(Ecran, pos)
    elif SSpawn:
        SpaceShip.draw(Ecran, pos)
        SSpawn = False
    Weapon1.level = PScore[2]
    Weapon1.posx = SpaceShip.posx + SpaceShip.Lenx/2
    Weapon1.posy = SpaceShip.posy
    Progress2 = 0
    if PScore[0] <= 0:
        LevelLoad = False
        ChickenBoss = []
        Chickens = []
        Asteroids = []
        AsteroidSpwn = False
        Startticks2 = -1
        seconds2 = 0
        PScore[0] = 5
    if not WaveUp:
        if not LevelLoad:
            Levels()
        else:
            drawChickens()
    if Chickens == [] and not AsteroidSpwn and not ChickenBoss and not WaveUp:
        Wave +=1
        WaveUp = True
        LevelLoad = False
        Gift = False
        Up = False
    if ChickenBoss:
        drawChickenBoss()
    if AsteroidSpwn or Asteroids:
        drawAsteroidWave()
    if Eggs:
        drawEggs()
    if ChickenDrop:
        drawChickenDrops()
    drawWeaponBullets()
    if RocketsObject:
        for Rocket in RocketsObject:
            Rocket.draw(Ecran)
            if abs(Rocket.posx - Rocket.xpos) < 3:
                xRocket = Rocket.xpos
                yRocket = Rocket.ypos
                for ChickBoss in ChickenBoss:
                        ChickBoss.Health -= 3000
                        if ChickBoss.Health < 0:
                            for i in range(5):
                                rand = random.randint(0,10)
                                if 10 > rand > 2:
                                    ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx  + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, 2))
                                elif rand < 2:
                                    ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx  + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, 3))
                                elif rand == 10:
                                    ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx  + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, 4))
                            ChickenDrop.append(Obiecte.ChickenDrop(ChickBoss.posx  + random.randint(0 ,int(ChickBoss.Lenx/2)),ChickBoss.posy , Width, Height, 5))
                            ChickenBoss.remove(ChickBoss)
                RocketEffect = True
                RocketsObject.remove(Rocket)
    if RocketEffect:
        drawRocketExp()
    if WaveUp:
        drawWaveText()
    drawGUIGame()

def FileLoad():
    global Saves, Ysaves, ButtonsSaves, NamesSaves
    Ysaves = Height/2 - 4*Yx
    SaveFile.seek(0)
    SaveFileTemp.seek(0)
    Saves = 0
    ButtonsSaves = []
    ButtonsSaves.append(Obiecte.Button(Width/9, Height-(3.5*Height)/100, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'back'))
    ButtonsSaves.append(Obiecte.Button(Width - Width/9, Height-(3.5*Height)/100, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'next'))
    NamesSaves = []
    Line = SaveFile.readline()
    if not Empty:
        while Line != []:
            LineWords = Line.split()
            try:
                NamesSaves.append(LineWords[0])
            except:
                break
            ButtonsSaves.append(Obiecte.Button(Width/2, Ysaves, Width/10, Height/30, Colors.ButtonPurple, LineWords[0]))
            Saves += 1
            Ysaves += Yx
            Line = SaveFile.readline()

def FileSave():
    global PScore, Empty, SaveFile, SaveFileTemp, Last, Wave, MyCareer 
    PScore[5] = Wave
    PScore[6] = Weapon1.number
    j = 0
    Last = False
    Wrote = False
    if Pause:
        SaveFileTemp.close()
        SaveFileTemp = open(r'Icons/savetemp.txt', 'w+')
        SaveFileTemp.write(PlayerName + ' ' + RookStats)
        for i in range(7):
            SaveFileTemp.write(' ' + str(PScore[i]))
        SaveFileTemp.seek(0)
        TtempLine = SaveFileTemp.readline()
        SaveFileTemp.close()
        SaveFileTemp = open(r'Icons/savetemp.txt', 'w+')
        SaveFile.seek(0)
        for Line in SaveFile.readlines():
            j +=1
            LineWords = Line.split()
            if LineWords == []:
                break
            if LineWords[0] == PlayerName:
                if Saves == j:
                    Last = True
                Wrote = True
                continue
            SaveFileTemp.write(Line)
        SaveFile.close()
        SaveFile = open(r'Icons/save.txt', 'w+')
        SaveFile.close()
        SaveFile = open(r'Icons/save.txt', 'r+')
        SaveFileTemp.seek(0)
        Liness = SaveFileTemp.readlines()
        SaveFile.writelines(Liness)
        if Wrote:
            if not Last:
                SaveFile.write('\n')
            SaveFile.writelines(TtempLine)
        if not Wrote:
            if Saves >=9:
                TempLine = SaveFileTemp.readline()
                SaveFileTemp.close()
                SaveFileTemp = open(r'Icons/savetemp.txt', 'w+')
                SaveFile.seek(0)
                Lines= SaveFile.readlines()
                for i in range(Saves):
                    if i > 0:
                        SaveFileTemp.write(Lines[i])
                SaveFile.close()
                SaveFile = open(r'Icons/save.txt', 'w+')
                SaveFile.close()
                SaveFile = open(r'Icons/save.txt', 'r+')
                SaveFile.write(TempLine + '\n')
                SaveFileTemp.seek(0)
                for Line in SaveFileTemp.readlines():
                    SaveFile.write(Line)
            else:
                if not Empty:
                    SaveFile.write('\n' + TtempLine)
                else:
                    SaveFile.write(TtempLine)
                    Empty = False
                    MyCareer = True
    else:
        SaveFileTemp.seek(0)
        SaveFileTemp.write(PlayerName + ' ' + RookStats)
        for i in range(7):
            SaveFileTemp.write(' ' + str(PScore[i]))
        SaveFileTemp.close()
        SaveFileTemp = open(r'Icons/savetemp.txt', 'w+')

def Levels():
    global PlayerLevel, Endgame, LevelLoad, Chickens, AsteroidSpwn, ChickenBoss, Progress, Aster, BossEggs, Boss, secAster
    Progress = 0 
    if PlayerLevel == 1:
        if Wave == 1:
            ListChicken1 = addChickens(8, 5, 1, Width/100, Height/100, True, 1, 0)
            ListChicken2 = addChickens(8, 5, 2, Width/100, 10*Height/100, True, 1, 0)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            LevelLoad = True
        elif Wave == 2:
            ListChicken1 = addChickens(8, 5, 1, Width/100, Height/100, True, 1, 0)
            ListChicken2 = addChickens(8, 5, 1, Width/100, 10*Height/100, True, 1, 0)
            ListChicken3 = addChickens(8, 5, 2, Width/100, 30*Height/100, True, 1, 0)
            ListChicken4 = addChickens(8, 5, 2, Width/100, 40*Height/100, True, 1, 0)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            LevelLoad = True
        elif Wave == 3:
            ListChicken1 = addChickens(8, 5, 1, Width/100, Height/100, True, 1, 0)
            ListChicken2 = addChickens(8, 5, 2, Width/100, 10*Height/100, True, 1, 0)
            ListChicken3 = addChickens(8, 5, 2, Width/100, 20*Height/100, True, 1, 0)
            ListChicken4 = addChickens(8, 5, 1, Width/100, 30*Height/100, True, 1, 0)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            LevelLoad = True
        elif Wave == 4:
            ListChicken1 = addChickens(8, 1, 1, Width/100, Height/100, True, 1, 0)
            ListChicken2 = addChickens(8, 5, 2, 1.02*Width/100, 10*Height/100, True, 1, 0)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            LevelLoad = True
        elif Wave == 5:
            ListChicken1 = addChickens(8, 1, 1, Width/100, Height/100, True, 1, 0)
            ListChicken2 = addChickens(8, 1, 1, Width/100, 10*Height/100, True, 1, 0)
            ListChicken3 = addChickens(8, 5, 2, 1.02*Width/100, 20*Height/100, True, 1, 0)
            ListChicken4 = addChickens(8, 5, 2, 1.02*Width/100, 30*Height/100, True, 1, 0)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            LevelLoad = True
        elif Wave == 6:
            Aster = 1
            secAster = 35
            AsteroidSpwn = True
            LevelLoad = True
        elif Wave == 7:
            ListChicken1 = addChickens(16, 1, 1, Width/100, Height/100, True, 2, 0)
            ListChicken2 = addChickens(16, 1, 2, Width/100, 20*Height/100, True, 2, 0)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            LevelLoad = True
        elif Wave == 8:
            ListChicken1 = addChickens(16, 1, 1, Width/100, Height/100, True, 2, 0)
            ListChicken2 = addChickens(16, 1, 2, Width/100, 20*Height/100, True, 2, 0)
            ListChicken3 = addChickens(8, 1, 1, Width/100, 40*Height/100, True, 1, 0)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            LevelLoad = True
        elif Wave == 9:
            ListChicken1 = addChickens(16, 1, 1, Width/100, Height/100, True, 2, 0)
            ListChicken2 = addChickens(16, 1, 2, Width/100, 20*Height/100, True, 2, 0)
            ListChicken3 = addChickens(16, 1, 1, Width/100, 40*Height/100, True, 2, 0)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            LevelLoad = True
        elif Wave == 10:
            ChickenBoss.append(Obiecte.ChickenBoss(Width/2, -Height/3, Width, Height, 1, Width/2, 25*Height/100))
            Progress = ChickenBoss[0].Health 
            BossEggs = 2
            Boss = 1
            LevelLoad = True
        elif Wave == 11:
            ListChicken1 = addChickens(8, 5, 3, Width/100, Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 12:
            ListChicken1 = addChickens(8, 5, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 5, 3, Width/100, Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 13:
            ListChicken1 = addChickens(8, 5, 2, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 5, 2, Width/100, 10*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 5, 3, Width/100, 20*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 14:
            ListChicken1 = addChickens(8, 5, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 5, 1, Width/100, 10*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 5, 1, Width/100, 20*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 5, 3, Width/100, 30*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 15:
            Aster = 1
            secAster = 45
            AsteroidSpwn = True
            LevelLoad = True
        elif Wave == 16:
            ListChicken1 = addChickens(8, 1, 3, Width/100, Height/100, True, 1, -1)
            ListChicken2 = addChickens(8, 5, 2, Width/100, 20*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 5, 2, Width/100, 30*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 17:
            ListChicken1 = addChickens(8, 1, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 1, 3, Width/100, 10*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 1, 2, Width/100, 20*Height/100, True, 1, -1)
            ListChicken4 = addChickens(8, 1, 2, Width/100, 30*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 18:
            ListChicken1 = addChickens(8, 1, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 1, 1, Width/100, 20*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 1, 3, Width/100, 30*Height/100, True, 1, 0)
            ListChicken4 = addChickens(8, 1, 3, Width/100, 40*Height/100, True, 1, 0)
            ListChicken5 = addChickens(8, 1, 2, Width/100, 50*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            Chickens.extend(ListChicken5)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 19:
            ListChicken1 = addChickens(8, 1, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 1, 1, Width/100, 20*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 1, 2, Width/100, 30*Height/100, True, 1, -1)
            ListChicken4 = addChickens(8, 1, 2, Width/100, 40*Height/100, True, 1, -1)
            ListChicken5 = addChickens(8, 1, 1, Width/100, 50*Height/100, True, 1, 1)
            ListChicken6 = addChickens(8, 1, 1, Width/100, 60*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            Chickens.extend(ListChicken5)
            Chickens.extend(ListChicken6)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 20:
            ChickenBoss.append(Obiecte.ChickenBoss(Width/2, -Height/3, Width, Height, 2, Width/2, 25*Height/100))
            ChickenBoss.Health = 25000
            BossEggs = 4
            Boss = 2
            Progress = ChickenBoss.Health 
            LevelLoad = True
        elif Wave == 21:
            ListChicken1 = addChickens(8, 1, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 1, 1, Width/100, 20*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 22:
            ListChicken1 = addChickens(8, 4, 2, Width/100, Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 23:
            ListChicken1 = addChickens(8, 1, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 1, 3, Width/100, 20*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 4, 3, Width/100, 30*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 24:
            ListChicken1 = addChickens(8, 4, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 4, 1, Width/100, 20*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 1, 3, Width/100, 20*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 25:
            Aster = 2
            secAster = 35
            AsteroidSpwn = True
            LevelLoad = True
        elif Wave == 26:
            ListChicken1 = addChickens(8, 4, 1, Width/100, Height/100, True, 1, -1)
            ListChicken2 = addChickens(8, 4, 1, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 4, 2, Width/100, 20*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 4, 2, Width/100, 30*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 27:
            ListChicken1 = addChickens(8, 4, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 6, 2, Width/100, 20*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 28:
            ListChicken1 = addChickens(8, 1, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 1, 1, Width/100, 10*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 6, 2, Width/100, 20*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 29:
            ListChicken1 = addChickens(8, 1, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 1, 3, Width/100, 10*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 6, 2, Width/100, 20*Height/100, True, 1, -1)
            ListChicken4 = addChickens(8, 6, 2, Width/100, 30*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 30:
            ChickenBoss.append(Obiecte.ChickenBoss(Width/2, -Height/3, Width, Height, 3, Width/2, 25*Height/100))
            ChickenBoss.Health = 35000
            BossEggs = 3
            Boss = 2
            Progress = ChickenBoss.Health 
            LevelLoad = True
        elif Wave == 31:
            ListChicken1 = addChickens(8, 4, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 6, 2, Width/100, 10 * Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 4, 1, Width/100, 25*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 32:
            ListChicken1 = addChickens(8, 4, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 6, 2, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 4, 1, Width/100, 25*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 6, 2, Width/100, 40*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 33:
            ListChicken1 = addChickens(8, 4, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 6, 3, Width/100, 15*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 11, 2, Width/100, 30*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 34:
            ListChicken1 = addChickens(8, 4, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 4, 1, Width/100, 10*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 6, 2, Width/100, 20*Height/100, True, 1, -1)
            ListChicken4 = addChickens(8, 11, 2, Width/100, 35*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 35:
            Aster = 2
            secAster = 45
            AsteroidSpwn = True
            LevelLoad = True
        elif Wave == 36:
            ListChicken1 = addChickens(8, 6, 2, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 6, 3, Width/100, 15*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 11, 2, Width/100, 30*Height/100, False, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 37:
            ListChicken1 = addChickens(8, 6, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 6, 1, Width/100, 15*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 6, 2, Width/100, 30*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 11, 1, Width/100, 45*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 38:
            ListChicken1 = addChickens(8, 6, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 6, 2, Width/100, 15*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 6, 1, Width/100, 30*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 6, 3, Width/100, 45*Height/100, True, 1, -1)
            ListChicken5 = addChickens(8, 11, 1, Width/100, 60*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            Chickens.extend(ListChicken5)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 39:
            ListChicken1 = addChickens(8, 3, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 6, 2, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 6, 1, Width/100, 30*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 11, 1, Width/100, 45*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 40:
            ChickenBoss.append(Obiecte.ChickenBoss(Width/2, -Height/3, Width, Height, 4, Width/2, 25*Height/100))
            ChickenBoss.Health = 45000
            BossEggs = 2
            Boss = 4
            Progress = ChickenBoss.Health 
            LevelLoad = True
        elif Wave == 41:
            ListChicken1 = addChickens(8, 3, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 1, 2, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 1, 1, Width/100, 20*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 42:
            ListChicken1 = addChickens(8, 3, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 3, 2, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 1, 1, Width/100, 20*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 43:
            ListChicken1 = addChickens(8, 3, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 3, 3, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 3, 2, Width/100, 20*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 44:
            ListChicken1 = addChickens(8, 3, 1, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 3, 1, Width/100, 10*Height/100, True, 1, 1)
            ListChicken3 = addChickens(8, 3, 2, Width/100, 20*Height/100, True, 1, -1)
            ListChicken4 = addChickens(8, 11, 2, Width/100, 30*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 45:
            Aster = 2
            secAster = 65
            AsteroidSpwn = True
            LevelLoad = True
        elif Wave == 46:
            ListChicken1 = addChickens(8, 3, 2, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 3, 3, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 3, 2, Width/100, 20*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 3, 3, Width/100, 30*Height/100, True, 1, -1)
            ListChicken5 = addChickens(8, 11, 2, Width/100, 40*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            Chickens.extend(ListChicken5)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 47:
            ListChicken1 = addChickens(8, 3, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 3, 1, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 3, 2, Width/100, 20*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 12, 1, Width/100, 30*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 48:
            ListChicken1 = addChickens(8, 7, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 3, 2, Width/100, 15*Height/100, True, 1, -1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 49:
            ListChicken1 = addChickens(8, 7, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 7, 2, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 3, 1, Width/100, 30*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 50:
            ListChicken1 = addChickens(8, 7, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 7, 2, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 3, 1, Width/100, 20*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 11, 2, Width/100, 30*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 51:
            ListChicken1 = addChickens(8, 7, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 7, 2, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 7, 1, Width/100, 20*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 12, 2, Width/100, 30*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 52:
            ListChicken1 = addChickens(8, 7, 3, Width/100, Height/100, True, 1, 1)
            ListChicken2 = addChickens(8, 7, 2, Width/100, 10*Height/100, True, 1, -1)
            ListChicken3 = addChickens(8, 7, 1, Width/100, 20*Height/100, True, 1, 1)
            ListChicken4 = addChickens(8, 7, 1, Width/100, 30*Height/100, True, 1, -1)
            ListChicken5 = addChickens(8, 12, 2, Width/100, 40*Height/100, True, 1, 1)
            Chickens.extend(ListChicken1)
            Chickens.extend(ListChicken2)
            Chickens.extend(ListChicken3)
            Chickens.extend(ListChicken4)
            Chickens.extend(ListChicken5)
            for Chicken in Chickens:
                Chicken.move = True
            LevelLoad = True
        elif Wave == 53:
            ChickenBoss.append(Obiecte.ChickenBoss(90*Width/100, -Height/3, Width, Height, 1, 25*Width/100, 10*Height/100))
            ChickenBoss.append(Obiecte.ChickenBoss(10*Width/100, -Height/3, Width, Height, 1, 75*Width/100, 20*Height/100))
            ChickenBoss[0].Health = 20000
            ChickenBoss[1].Health = 20000
            BossEggs = 1
            Boss = 1
            Progress = ChickenBoss[0].Health * 2
            LevelLoad = True
        elif Wave == 54:
            ChickenBoss.append(Obiecte.ChickenBoss(90*Width/100, -Height/3, Width, Height, 2, 25*Width/100, 10*Height/100))
            ChickenBoss.append(Obiecte.ChickenBoss(10*Width/100, -Height/3, Width, Height, 3, 75*Width/100, 20*Height/100))
            ChickenBoss[0].Health = 35000
            ChickenBoss[1].Health = 35000
            BossEggs = 2
            Boss = 3
            Progress = ChickenBoss[0].Health * 2
            LevelLoad = True
        elif Wave == 55:
            ChickenBoss.append(Obiecte.ChickenBoss(90*Width/100, -Height/3, Width, Height, 4, 25*Width/100, 10*Height/100))
            ChickenBoss.append(Obiecte.ChickenBoss(10*Width/100, -Height/3, Width, Height, 4, 75*Width/100, 20*Height/100))
            ChickenBoss[0].Health = 45000
            ChickenBoss[1].Health = 45000
            BossEggs = 2
            Boss = 4
            Progress = ChickenBoss[0].Health * 2
            LevelLoad = True
        elif Wave == 56:
            ChickenBoss.append(Obiecte.ChickenBoss(90*Width/100, -Height/3, Width, Height, 5, 25*Width/100, 10*Height/100))
            ChickenBoss[0].Health = 80000
            BossEggs = 3
            Boss = 5
            Progress = ChickenBoss[0].Health
            LevelLoad = True
        else:
            Endgame = True
            LevelLoad = True

# Sound
Playing = False
PlayingSoundGame = False
Whichsound = 1
SoundChicken = mixer.Sound('Icons/Sounds/Chicken.mp3')
SoundChicken.set_volume(0.1)
SoundRocket = mixer.Sound('Icons/Sounds/Rocket.mp3')
SoundRocket.set_volume(0.2)
SoundUp = mixer.Sound('Icons/Sounds/Up.mp3')
SoundUp.set_volume(0.2)
SoundGun = mixer.Sound('Icons/Sounds/Gun.mp3')
SoundGun.set_volume(0.2)
SoundButton = mixer.Sound('Icons/Sounds/Button.mp3')
SoundButton.set_volume(0.2)

# Ecran
pygame.display.set_icon(pygame.image.load('Icons/Icon.png'))
Ecran = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
BackgroundImage = pygame.image.load('Icons/Background/background.jpg')
BackgroundTextImage = pygame.image.load('Icons/Background/Mainpic.png')
BackgroundText = pygame.transform.scale(BackgroundTextImage,(250,125))
x = pygame.display.get_window_size()
Width = x[0]
Height = x[1]
Background1 = pygame.transform.scale(BackgroundImage, (Width,Height))
BackgroundSpeed = 0

BackgroundPlayImage = pygame.image.load('Icons/Background/BackgroundPlay.jpeg')
Background2 = pygame.transform.scale(BackgroundPlayImage, (Width, Height))
Background = Background1

# Icons
Imgbifa = pygame.image.load('Icons/Background/Bifa.png')
Imgbif = pygame.transform.scale(Imgbifa,[20,30])
IconHeartz = pygame.image.load('Icons/Heart.png')
IconThunderz = pygame.image.load('Icons/Thunder.png')
IconRocketz = pygame.image.load('Icons/rocket.png')
IconLegChickenz = pygame.image.load('Icons/ChickenLeg.png')
IconHeart = pygame.transform.scale(IconHeartz,[20,20])
IconRocket = pygame.transform.scale(IconRocketz,[20,20])
IconThunder = pygame.transform.scale(IconThunderz,[20,20])
IconLegChicken = pygame.transform.scale(IconLegChickenz,[20,20])

SShipHITBOXx = 0
SShipHITBOXy = 0

EffectSize = 0
xRocket = 0
yRocket = 0

# Bool vars
Exit = False
Main = True
Pause = False
Controls = False
Writing = False
Empty = False
RocketEffect = False
RocketCoolDown = False
LevelLoad = False

MyCareerMenu = False
Last = False

Options = False
Music = True
Effects = True
Lag = False

StartGame = False
Rookie = True
Veteran = False
MyCareer = False
Choosed = False
AnotherName = False
Endgame = False

StartPlay = False
Shooting = False
Cooldown = False
LevelDraw = False
Dead = False
SSpawn = True
ShootAgain = True

Up = False
Gift = False

# Files
PlayerName = ''
Rookstats = ''
Wave = 1

try:
    SaveFile = open(r'Icons/save.txt', 'r+')
except:
    
    SaveFile = open(r'Icons/save.txt', 'w+')
    SaveFile.close()
    SaveFile = open(r'Icons/save.txt', 'r+')
SaveFileTemp = open(r'Icons/savetemp.txt', 'w+')
if SaveFile.readlines() != []:
    MyCareer = True
else:
    Empty = True
SaveFile.seek(0)

try:
    Config = open(r'Icons/config', 'r+')
    Linec = Config.read()
    Linew = Linec.split()
    if Linew[0] == 'False':
        Music = False
    else:
        Music = True
    if Linew[1] == 'False':
        Effects = False
    else:
        Effects = True
    Config.close()
    Config = open(r'Icons/config', 'w+')
except:
    Config = open(r'Icons/config', 'w+')

# Obiecte
Obiectcopy = 0
ButtonsMain = []
ButtonsMain.append(Obiecte.Button(Width/2, Height-Height/7, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'exit'))
ButtonsMain.append(Obiecte.Button(Width/2, Height-2*Height/7, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'options'))
ButtonsMain.append(Obiecte.Button(Width/2, ButtonsMain[1].posy-ButtonsMain[1].sizey, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'save the world'))
MMtext = Obiecte.Text(Width/2, ButtonsMain[1].posy-2.5*ButtonsMain[1].sizey, 50, Colors.MidDarkBlue)

ButtonsOption = []
ButtonsOption.append(Obiecte.Button(Width/2, Height-Height/7, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'done'))
ButtonsOption.append(Obiecte.Button(Width/2, Height-2*Height/7, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'music'))
ButtonsOption.append(Obiecte.Button(Width/2, ButtonsOption[1].posy-ButtonsOption[1].sizey, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'effects'))
Optiontext = Obiecte.Text(Width/2, ButtonsOption[1].posy-2.5*ButtonsOption[1].sizey, 50, Colors.MidDarkBlue)

ButtonsStart = []
ButtonsStart.append(Obiecte.Button(Width/9, Height-(3.5*Height)/100, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'back'))
ButtonsStart.append(Obiecte.Button(Width - Width/9, Height-(3.5*Height)/100, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'next'))
ButtonsStart.append(Obiecte.Button(Width/2, Height/2+(5*Height)/100, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'start new mission'))
ButtonsStart.append(Obiecte.Button(Width/2, ButtonsStart[2].posy-ButtonsStart[2].sizey, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'my carrer'))
ButtonsStart.append(Obiecte.Button(Width/2 + (5*Width)/100, ButtonsStart[2].posy + ButtonsStart[2].sizey + (2*Height)/100, (10*Width)/100, (3*Height)/100, Colors.ButtonPurple, 'rookie'))
ButtonsStart.append(Obiecte.Button(Width/2 + (5*Width)/100, ButtonsStart[2].posy + ButtonsStart[2].sizey + 3*(2*Height)/100, (10*Width)/100, (3*Height)/100, Colors.ButtonPurple, 'veteran'))
ButtonsStart.append(Obiecte.Button(Width/2, Height/2 + 20*Height/100, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'name'))
AnotherNameText = Obiecte.Text(Width/2, Height/2 + 2.5*Height/10, 20, Colors.White)

TextGUI = []
TextGUI.append(Obiecte.Text(4*Width/100, Height- 1.75*Height/100, int(1.4*Width/100), Colors.White))
TextGUI.append(Obiecte.Text(2*(4*Width/100), Height- 1.75*Height/100, int(1.4*Width/100), Colors.White))
TextGUI.append(Obiecte.Text(3*(4*Width/100), Height- 1.75*Height/100, int(1.4*Width/100), Colors.White))
TextGUI.append(Obiecte.Text(4*(4*Width/100), Height- 1.75*Height/100, int(1.4*Width/100), Colors.White))
TextGUI.append(Obiecte.Text(4*Width/100, 2.15*Height/100, int(1.8*Width/100), Colors.White))
PGbar = Obiecte.Progressbar(Width/2, Height/100, Width/4, Height/35, Colors.MidDarkBlue, 1, int(1.55*Width/100))

ButtonsPause = []
ButtonsPause.append(Obiecte.Button(Width/2, Height/2 - Height/10, Width/10, Height/30, Colors.ButtonPurple, 'save & quit'))
ButtonsPause.append(Obiecte.Button(Width/2, Height/2, Width/10, Height/30, Colors.ButtonPurple, 'controls'))
ButtonsPause.append(Obiecte.Button(Width/2, Height/2 + Height/10, Width/10, Height/30, Colors.ButtonPurple, 'back'))

ButtonsControls = [] 
TextControls = []
ButtonsControls.append(Obiecte.Button(Width/2, Height/2 + Height/10, Width/10, Height/30, Colors.ButtonPurple, 'back'))
TextControls.append(Obiecte.Text(Width/2, Height/2 - Height/10, int(1.4*Width/100), Colors.White))
TextControls.append(Obiecte.Text(Width/2, Height/2 - Height/7, int(1.4*Width/100), Colors.White))

WaveText = Obiecte.Text(Width/2, Height/2, 30, Colors.White)
WaveUp = False

Asteroids = []
AsteroidSpwn = False
Aster = 1

Saves = 0
Yx = Height/30
Ysaves = Height/2 - 4*Yx
ButtonsSaves = []
ButtonsSaves.append(Obiecte.Button(Width/9, Height-(3.5*Height)/100, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'back'))
ButtonsSaves.append(Obiecte.Button(Width - Width/9, Height-(3.5*Height)/100, (20*Width)/100, (3.5*Height)/100, Colors.ButtonPurple, 'next'))
NamesSaves = []
FileLoad()


SpaceShip = Obiecte.SpaceShip(0, 0, Width, Height)
RocketsObject = []

Weapon1 = Obiecte.Weapon(SpaceShip.posx + SpaceShip.Lenx/2, SpaceShip.posy, Width, Height, 2)
Chickens = []
Eggs = []
ChickenDrop = []
ChickenBoss = []
Boss = 0

# Player score
Progress = 0
Progress2 = 0
PlayerLevel = 1
WaveLevel = 1
Lives = 3
Rockets = 0
Thunders = 0
ChickenLegz = 0
Score = 0
Wwave = 1
Wpn = 0
PScore = [Lives, Rockets, Thunders, ChickenLegz, Score, Wwave, Wpn]
PScore.append(Obiecte.WeaponHeat(8*Width/100, 1*Height/100, 0, Width/185))

Clock = pygame.time.Clock()
Shoot = pygame.USEREVENT + 1
NotDraw = pygame.USEREVENT + 3
DropEgg = pygame.USEREVENT + 4
pygame.time.set_timer(DropEgg, 1500)
pygame.time.set_timer(NotDraw, 75)
pygame.time.set_timer(Shoot, 500)
Startticks = -1
Startticks2 = -1
Startticks3 = -1
Startticksegg = -1
StartticksWave = -1
StarttickCooldown = -1
secondsCooldown = 0
secondsWave = 0
seconds = 0
seconds2 = 0
secondsEgg = 0
secondsBoss = 0
Eggsec = 2
BossEggs = 5
secAster = 30
xbs = 0

CopyRightText = Obiecte.Text(Width/2, Height/2, 30, Colors.White)
CopyRightText1 = Obiecte.Text(Width/2, Height/2 + 5*Height/100, 30, Colors.White)
CopyRightText2 = Obiecte.Text(Width/2, Height/2 + 10*Height/100, 30, Colors.White)
CopyRightText0 = Obiecte.Text(Width/2, Height/2 - 20*Height/100, 40, Colors.White)
CopyRightText.draw(Ecran,'I don\'t own any rights of the game.')
CopyRightText1.draw(Ecran,'The credits goes to the owners.')
CopyRightText2.draw(Ecran,'This game clone is purely fan made, and will not be used for profit  or illegal sharing.')
CopyRightText0.draw(Ecran,'GAME CLONE')

pygame.display.update()
time.sleep(1)

while not Exit:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == DropEgg:
                for Drop in ChickenDrop:
                    if Drop.y_speed == 0:
                        Drop.remove -= 1
                        if Drop.remove <= 0:
                            ChickenDrop.remove(Drop)
        if event.type == NotDraw:
            SSpawn = True
        if event.type == Shoot:
            if not ShootAgain: 
                ShootAgain = True
            elif AsteroidSpwn:
                AsteroidSpawn(Aster, 3)
        if event.type == pygame.QUIT:
            Exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Main:
                for Button in ButtonsMain:
                    if (Button.CursorTrigx < pos[0] < Button.CursorTrigx + Button.sizex and
                    Button.CursorTrigy < pos[1] < Button.CursorTrigy + Button.sizey):
                        if Button == ButtonsMain[0]:
                            Exit = True
                            if PlayerName != '':
                                FileSave()
                        elif Button == ButtonsMain[1]:
                            Main = False
                            Options = True
                            Lag = True
                        elif Button == ButtonsMain[2]:
                            Main = False
                            StartGame = True
                            ButtonsStart[6].txt = 'name'
                SoundButton.play()
            if Options:
                if Lag:
                    Lag = False
                else:
                    for Button in ButtonsOption:
                        if (Button.CursorTrigx < pos[0] < Button.CursorTrigx + Button.sizex and
                        Button.CursorTrigy < pos[1] < Button.CursorTrigy + Button.sizey):
                            if Button == ButtonsOption[0]:
                                Options = False
                                Main = True
                            elif Button == ButtonsOption[1]:
                                if Music:
                                    Music = False
                                else: 
                                    Music = True
                            elif Button == ButtonsOption[2]:
                                if Effects: 
                                    Effects = False
                                else:
                                    Effects = True
                SoundButton.play()
            if StartGame:
                for Button in ButtonsStart:
                        if (Button.CursorTrigx < pos[0] < Button.CursorTrigx + Button.sizex and
                        Button.CursorTrigy < pos[1] < Button.CursorTrigy + Button.sizey):
                            if Button == ButtonsStart[0]:
                                Writing = False
                                StartGame = False
                                Main = True
                            elif Button == ButtonsStart[1] and ButtonsStart[6].txt and not Choosed:
                                for name in NamesSaves:
                                    if name == ButtonsStart[6].txt:
                                        AnotherName = True
                                if not AnotherName:
                                    PlayerName = ButtonsStart[6].txt
                                    if not Choosed:
                                        if Rookie:
                                            RookStats = '1'
                                        else:
                                            RookStats = '0'
                                        for j in range(7):
                                            if j == 0:
                                                PScore[j] = 3
                                            elif j == 5 or  j == 6:
                                                PScore[j] = 1 
                                            else:
                                                PScore[j] = 0  
                                    FileSave()
                                    Writing = False
                                    StartGame = False
                                    StartPlay = True
                                    BackgroundSpeed = 0
                                    Background = Background2
                            elif Button == ButtonsStart[1] and Choosed:
                                StartGame = False
                                MyCareerMenu = True
                            elif Button == ButtonsStart[2]:
                                Choosed = False
                                Writing = False
                                Exit = False
                            elif Button == ButtonsStart[3] and MyCareer:
                                Choosed = True
                                Writing = False
                            elif Button == ButtonsStart[4] and Veteran and not Choosed:
                                Writing = False
                                Veteran = False
                                Rookie = True
                            elif Button == ButtonsStart[5] and Rookie and not Choosed:
                                Writing = False
                                Veteran = True
                                Rookie = False
                            elif Button == ButtonsStart[6] and not Choosed:
                                Writing = True
                                ButtonsStart[6].txt = ''
                SoundButton.play()
            if StartPlay and pygame.mouse.get_pressed()[0] == True and ShootAgain and not Cooldown:
                Weapon1.addBullet(Weapon1.number)
                if Effects:
                    SoundGun.play()
                ShootAgain = False
                Shooting = True
                PScore[7].counter += 4.5
            elif StartPlay and pygame.mouse.get_pressed()[2] == True and not RocketCoolDown and PScore[1]>0:
                RocketsObject.append(Obiecte.Rocket(SpaceShip.posx, SpaceShip.posy, Width, Height, Width/2, Height/2 - Height/10))
                if Effects:
                    RocketCoolDown = True
                SoundRocket.play()
                PScore[1] -= 1
            if MyCareerMenu:
                for ButtonSaves in ButtonsSaves:
                    if (ButtonSaves.CursorTrigx < pos[0] < ButtonSaves.CursorTrigx + ButtonSaves.sizex and
                        ButtonSaves.CursorTrigy < pos[1] < ButtonSaves.CursorTrigy + ButtonSaves.sizey):
                            if ButtonSaves == ButtonsSaves[0]:
                                StartGame = True
                                MyCareerMenu = False
                            elif ButtonSaves == ButtonsSaves[1] and Obiectcopy:
                                MyCareerMenu = False
                                StartPlay = True
                                BackgroundSpeed = 0
                                Background = Background2
                                SaveFile.seek(0)
                                for i in range(Saves):
                                    Line = SaveFile.readline()
                                    LineWords = Line.split()
                                    if LineWords[0] == Obiectcopy.txt:
                                        PlayerName = LineWords[0]
                                        RookStats = LineWords[1]
                                        if RookStats == 'False':
                                            Rookie = False
                                        else:
                                            Rookie = True
                                        for j in range(7):
                                            PScore[j] = int(LineWords[j+2])
                                        Wave = int(PScore[5])
                                        Weapon1.number = int(PScore[6])
                                        break
                                Obiectcopy = 0
                            elif ButtonSaves != ButtonsSaves[1]:
                                Obiectcopy = ButtonSaves
                SoundButton.play()
            if Controls:
                if (ButtonsControls[0].CursorTrigx < pos[0] < ButtonsControls[0].CursorTrigx + ButtonsControls[0].sizex and
                    ButtonsControls[0].CursorTrigy < pos[1] < ButtonsControls[0].CursorTrigy + ButtonsControls[0].sizey):
                        Controls = False
                SoundButton.play()
            elif Pause:
                for ButtonPause in ButtonsPause:
                    if (ButtonPause.CursorTrigx < pos[0] < ButtonPause.CursorTrigx + ButtonPause.sizex and
                        ButtonPause.CursorTrigy < pos[1] < ButtonPause.CursorTrigy + ButtonPause.sizey):
                        if ButtonPause == ButtonsPause[0]:
                            Background = Background1
                            Main = True
                            LevelDraw = False
                            FileSave()
                            FileLoad()
                            Pause = False
                        elif ButtonPause == ButtonsPause[1]:
                            Controls = True
                        elif ButtonPause == ButtonsPause[2]:
                            Pause = False
                            StartPlay = True
                SoundButton.play()
        if event.type == pygame.MOUSEBUTTONUP:
            Shooting = False
        if event.type == Shoot and StartPlay and Shooting and not Cooldown:
            Weapon1.addBullet(Weapon1.number)
            if Effects:
                    SoundGun.play()
            PScore[7].counter += 5
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_BACKSPACE:
                if ButtonsStart[6].txt:
                    AnotherName = False
                    ButtonsStart[6].txt = ButtonsStart[6].txt[:-1]
            elif Writing and len(ButtonsStart[6].txt) < 20:
                ButtonsStart[6].txt += event.unicode
                AnotherName = False
            if event.key == pygame.K_ESCAPE and (StartPlay or Pause):
                if not Pause:
                    StartPlay = False
                    Pause = True
                else:
                    StartPlay = True
                    Pause = False
            if keys[pygame.K_0] and keys[pygame.K_9]:
                if Colors.Developer:
                    Colors.Developer = False
                else:
                    Colors.Developer = True
    if PScore[7].counter >= 0:
        PScore[7].counter -= 0.125
    if PScore[7].counter >30:
        Cooldown = True
    if Dead and Startticks == -1 or RocketCoolDown and Startticks == -1:
        Startticks = pygame.time.get_ticks()
    if Dead:
        seconds=(pygame.time.get_ticks()-Startticks)/1000
        if seconds > 3:
            Startticks =-1
            seconds = 0
            Dead = False
    elif RocketCoolDown:
        seconds=(pygame.time.get_ticks()-Startticks)/1000
        if seconds > 3:
            Startticks =-1
            seconds = 0
            RocketCoolDown = False
    if WaveUp and StartticksWave == -1:
        StartticksWave = pygame.time.get_ticks()
    if WaveUp:
        secondsWave = (pygame.time.get_ticks()-StartticksWave)/1000
        if secondsWave > 5:
            StartticksWave =-1
            secondsWave = 0
            WaveUp = False
    if Startticks3 == -1 and ChickenBoss:
        Startticks3 = pygame.time.get_ticks()
    if StarttickCooldown == -1 and Cooldown:
        StarttickCooldown = pygame.time.get_ticks()
    if Cooldown:
        secondsCooldown=(pygame.time.get_ticks()-StarttickCooldown)/1000
        if secondsCooldown > 5:
            StarttickCooldown = -1
            ssecondsCooldown = 0
            Cooldown = False
    if ChickenBoss:
        secondsBoss=(pygame.time.get_ticks()-Startticks3)/1000
        if len(ChickenBoss)>1:
            if xbs == 0:
                xbs = 1
            else:
                xbs = 0
        else:
            xbs = 0
        if secondsBoss > BossEggs:
            if Boss == 1 or Boss == 4:
                Eggs.append(Obiecte.ChickenDrop(ChickenBoss[xbs].posx + ChickenBoss[xbs].Lenx/2 ,ChickenBoss[xbs].posy + ChickenBoss[xbs].Leny, Width, Height, 9))
            else:
                Eggs.append(Obiecte.ChickenDrop(ChickenBoss[xbs].posx, ChickenBoss[xbs].posy + ChickenBoss[xbs].Leny , Width, Height, 1))
                Eggs.append(Obiecte.ChickenDrop(ChickenBoss[xbs].posx + ChickenBoss[xbs].Lenx/2 ,ChickenBoss[xbs].posy + ChickenBoss[xbs].Leny, Width, Height, 1))
                Eggs.append(Obiecte.ChickenDrop(ChickenBoss[xbs].posx + ChickenBoss[xbs].Lenx ,ChickenBoss[xbs].posy + ChickenBoss[xbs].Leny , Width, Height, 1))
            
            Startticks3 =-1
            secondsBoss = 0
    if Startticks2 == -1 and AsteroidSpwn:
        Startticks2 = pygame.time.get_ticks()
    if AsteroidSpwn:
        seconds2=(pygame.time.get_ticks()-Startticks2)/1000
        if seconds2 > secAster:
            Startticks2 =-1
            seconds2 = 0
            AsteroidSpwn = False
    if Startticksegg == -1 and Chickens:
        Startticksegg = pygame.time.get_ticks()
    if Chickens:
        secondsEgg=(pygame.time.get_ticks()-Startticksegg)/1000
        if secondsEgg > 2:
            Startticksegg = -1
            secondsEgg = 0
            ze = random.randint(0, len(Chickens)-1)
            if Chickens[ze].xdone == True and Chickens[ze].ydone == True:
                Eggs.append(Obiecte.ChickenDrop(Chickens[ze].posx  - Width/100,Chickens[ze].posy , Width, Height, 1))
    if not Pause:
        Ecran.fill(Colors.Black)
        drawBackground()
    if Main:
        if PlayingSoundGame:
            mixer.music.fadeout(250)
            PlayingSoundGame = False
        if not Playing and Music:
            mixer.music.load('Icons/Sounds/Main.mp3')
            mixer.music.set_volume(0.25)
            mixer.music.play()
            Playing = True
        elif Playing and not Music:
            mixer.music.fadeout(1000)
        drawButtonsMain()
    elif Options:
        if Playing and not Music:
            mixer.music.fadeout(1000)
        elif not Playing and Music:
            mixer.music.load('Icons/Sounds/Main.mp3')
            mixer.music.set_volume(0.25)
            mixer.music.play()
            Playing = True
        drawButtonsOptions()
    elif StartGame:
        if AnotherName:
            AnotherNameText.draw(Ecran, 'Please select another name')
        drawButtonsStart()
    elif MyCareerMenu:
        drawCarrerSelect()
    elif StartPlay:
        if Playing:
            Playing = False
            mixer.music.fadeout(500)
        if Music and not PlayingSoundGame:
            mixer.music.load('Icons/Sounds/Playing.mp3')
            PlayingSoundGame = True
            mixer.music.set_volume(0.15)
            mixer.music.play()
        if PlayingSoundGame and mixer.music.get_pos() == -1:
            if Whichsound == 1:
                mixer.music.load('Icons/Sounds/Playing2.mp3')
                Whichsound = 2
                mixer.music.set_volume(0.15)
            else:
                Whichsound = 1
                mixer.music.load('Icons/Sounds/Playing.mp3')
                mixer.music.set_volume(0.15)
            mixer.music.play()
        drawStart()
    elif Controls:
        drawControls()
    elif Pause:
        drawPause()
    pygame.display.update()
    Clock.tick(60)
    
pygame.quit

Config.write(str(Music) + ' ' + str(Effects))
Config.close()
SaveFile.close()
SaveFileTemp.close()
