import pygame
import Colors
import random
from Colors import Developer

class Text:
    def __init__(self, posx, posy, size, color):
        self.posx = posx
        self.posy = posy
        self.size = size
        self.color = color
        self.Font = pygame.font.Font('Fontregular.ttf',self.size)


    def draw(self, Ecran, text):
        Txt = self.Font.render(text, True, self.color)
        Txtrect = Txt.get_rect()
        Txtrect.center = (self.posx, self.posy)
        Ecran.blit(Txt, Txtrect)

class Button:
    def __init__(self, posx, posy, sizex, sizey, color, txt):
        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.color = color
        self.Text = Text(posx , posy, 25, Colors.White)
        self.CursorTrigx = self.posx - self.sizex/2
        self.CursorTrigy = self.posy - self.sizey/2
        self.txt = txt

    def draw(self, Ecran, hover):
        pygame.draw.rect(Ecran, self.color, pygame.Rect(self.CursorTrigx, self.CursorTrigy , self.sizex, self.sizey), 0, 15)
        if not hover:
            pygame.draw.rect(Ecran,Colors.ButtonLinePurple, pygame.Rect(self.CursorTrigx, self.CursorTrigy , self.sizex, self.sizey), 2, 15)
        else:
            pygame.draw.rect(Ecran,Colors.MidLightBlue, pygame.Rect(self.CursorTrigx, self.CursorTrigy , self.sizex, self.sizey), 4, 15) 
        self.Text.draw(Ecran, self.txt)

class WeaponHeat():
    def __init__(self, posx, posy, counter, x):
        self.posx = posx
        self.posy = posy
        self.counter = counter
        self.x = x
    def draw(self, Ecran):
        for i in range(35):
            if i <= self.counter:
                pygame.draw.line(Ecran, Colors.Green, [i*self.x + self.posx, self.posy], [i*self.x + self.posx, 3.5*self.posy], 4)
            else:
                pygame.draw.line(Ecran, Colors.MidLightBlue, [i*self.x + self.posx, self.posy], [i*self.x + self.posx, 3.5*self.posy], 4)

class Progressbar():
    def __init__(self, posx, posy, sizex, sizey, color, txt, fsize):
        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.color = color
        self.txt = txt
        self.Text = Text(posx, posy + fsize/2, fsize, Colors.White)
    def draw(self, Ecran):
        pygame.draw.rect(Ecran, self.color, pygame.Rect(self.posx-self.sizex/2, self.posy , self.sizex, self.sizey), 0, 15)
        pygame.draw.rect(Ecran,Colors.MidLightBlue, pygame.Rect(self.posx-self.sizex/2, self.posy , self.sizex, self.sizey), 4, 15)
        self.Text.draw(Ecran, str(self.txt) + '%')

class SpaceShip():
    def __init__(self, posx, posy, sizex, sizey):
        self.sizex = sizex
        self.sizey = sizey
        Imgf = pygame.image.load('Icons/p1.png')
        self.Lenx = 8*self.sizex/100
        self.Leny2 = 20*self.sizey/100
        self.Leny = self.Leny2/2
        self.img = pygame.transform.scale(Imgf,(self.Lenx, self.Leny2))
        self.posx = posx
        self.posy = posy
        self.weapon = 0
    def draw(self, Ecran, pos):
        if 6*self.sizey/100 < pos[1] < self.sizey - 5*self.sizey/100:
            self.posy = pos[1]
        self.posx = pos[0] - 4*self.sizex/100
        Ecran.blit(self.img, (self.posx, self.posy))
        if Colors.Developer:
            pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.Lenx, self.Leny], 3)

class Bullet():
    def __init__(self, posx, posy, x_speed, y_speed, sizex, sizey, Bulletnumber, degrees):
        self.posx = posx
        self.posy = posy
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.sizex = sizex
        self.sizey = sizey
        self.degrees = degrees
        self.damage = 0
        self.Bulletnumber = Bulletnumber
        if Bulletnumber == 1:
            self.Lenx = 2*sizex/100
            self.Leny = 10*self.sizey/100
            Imgf = pygame.image.load('Icons/Bullets/Bullet' + str(Bulletnumber) + '.png')
            self.Img = pygame.transform.scale(Imgf, (self.Lenx, self.Leny))
            self.Img = pygame.transform.rotate(self.Img, self.degrees)
        elif Bulletnumber == 2:
            self.Lenx = 2*sizex/100
            self.Leny = 10*self.sizey/100
            Imgf = pygame.image.load('Icons/Bullets/Bullet' + str(Bulletnumber) + '.png')
            self.Img = pygame.transform.scale(Imgf, (self.Lenx, self.Leny))
            self.Img = pygame.transform.rotate(self.Img, self.degrees)
        elif Bulletnumber == 3:
            self.Lenx = 4*sizex/100
            self.Leny = 4*sizey/100
        self.posx = self.posx - self.Lenx/2
    def draw(self, Ecran):
        if self.Bulletnumber != 3:
            Ecran.blit(self.Img, (self.posx, self.posy))
        else:
            pygame.draw.rect(Ecran, Colors.MidDarkBlue,[self.posx,  self.posy, self.Lenx, self.Leny], 3)
        if Colors.Developer:
            pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.Lenx, self.Leny], 3)
        self.posx += self.x_speed
        self.posy += self.y_speed

class Weapon():
    def __init__(self, posx, posy, sizex, sizey, number):
        self.posx = posx
        self.number = number
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.level = 0
        if number == 1:
            self.damage = 100
        elif number == 2:
            self.damage = 200
        else:
            self.damage = 150
        self.bulletspeed = -7
        self.Bullets = []
    def addBullet(self, number):
        if number == 1:
            if self.level == 0:
                self.Bullets.append(Bullet(self.posx ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 1, 0))
            elif self.level < 2:
                self.Bullets.append(Bullet(self.posx - self.sizex/100 ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 1, 0))
                self.Bullets.append(Bullet(self.posx + self.sizex/100,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 1, 0))
            elif self.level < 4:
                self.Bullets.append(Bullet(self.posx - 3*self.sizex/100 ,self.posy, -0.5, self.bulletspeed, self.sizex, self.sizey, 1, 35))
                self.Bullets.append(Bullet(self.posx ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 1, 0))
                self.Bullets.append(Bullet(self.posx + self.sizex/100,self.posy, +0.5, self.bulletspeed, self.sizex, self.sizey, 1, -35))
            elif self.level < 6:
                self.Bullets.append(Bullet(self.posx - 5*self.sizex/100 ,self.posy + 2*self.sizey/100, -1, self.bulletspeed, self.sizex, self.sizey, 1, 35))
                self.Bullets.append(Bullet(self.posx - 1.75*self.sizex/100 ,self.posy, -0.15, self.bulletspeed, self.sizex, self.sizey, 1, 15))
                self.Bullets.append(Bullet(self.posx + 0.5*self.sizex/100 ,self.posy, +0.15, self.bulletspeed, self.sizex, self.sizey, 1, -15))
                self.Bullets.append(Bullet(self.posx + 3*self.sizex/100 ,self.posy + 2*self.sizey/100, +1, self.bulletspeed, self.sizex, self.sizey, 1, -35))
            elif self.level < 8:
                self.Bullets.append(Bullet(self.posx - 5*self.sizex/100 ,self.posy + 3*self.sizey/100, -2, self.bulletspeed, self.sizex, self.sizey, 1, 25))
                self.Bullets.append(Bullet(self.posx - 2.75*self.sizex/100 ,self.posy + self.sizey/100, -1.75, self.bulletspeed, self.sizex, self.sizey, 1, 15))
                self.Bullets.append(Bullet(self.posx ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 1, 0))
                self.Bullets.append(Bullet(self.posx + 1.25*self.sizex/100 ,self.posy + self.sizey/100, +1.75, self.bulletspeed, self.sizex, self.sizey, 1, -15))
                self.Bullets.append(Bullet(self.posx + 3*self.sizex/100 ,self.posy + 3*self.sizey/100, +2, self.bulletspeed, self.sizex, self.sizey, 1, -25))
            else:
                self.damage = 300
                self.Bullets.append(Bullet(self.posx - 4.3*self.sizex/100 ,self.posy + 2*self.sizey/100, -2, self.bulletspeed, self.sizex, self.sizey, 1, 35))
                self.Bullets.append(Bullet(self.posx - 3*self.sizex/100 ,self.posy + self.sizey/100, -1.75, self.bulletspeed, self.sizex, self.sizey, 1, 15))
                self.Bullets.append(Bullet(self.posx - 0.75*self.sizex/100,self.posy, -1, self.bulletspeed, self.sizex, self.sizey, 1, 5))
                self.Bullets.append(Bullet(self.posx + 0.5*self.sizex/100 ,self.posy, +1, self.bulletspeed, self.sizex, self.sizey, 1, -5))
                self.Bullets.append(Bullet(self.posx + 2*self.sizex/100 ,self.posy + self.sizey/100, +1.75, self.bulletspeed, self.sizex, self.sizey, 1, -15))
                self.Bullets.append(Bullet(self.posx + 2.5*self.sizex/100 ,self.posy + 2*self.sizey/100, +2, self.bulletspeed, self.sizex, self.sizey, 1, -35))
        elif number == 2:
            if self.level == 0:
                self.Bullets.append(Bullet(self.posx ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
            elif self.level < 2:
                self.Bullets.append(Bullet(self.posx - self.sizex/100 ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx + self.sizex/100 ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
            elif self.level < 4:
                self.Bullets.append(Bullet(self.posx - self.sizex/100 ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx + self.sizex/100 ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
            elif self.level < 6:
                self.Bullets.append(Bullet(self.posx - 3*self.sizex/100 ,self.posy + 3*self.sizey/100, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx - self.sizex/100 ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx + self.sizex/100 ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx + 3*self.sizex/100 ,self.posy + 3*self.sizey/100, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
            elif self.level < 1000:
                self.damage = 350
                self.Bullets.append(Bullet(self.posx - 3*self.sizex/100 ,self.posy + 3*self.sizey/100, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx - self.sizex/100 ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx + self.sizex/100 ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
                self.Bullets.append(Bullet(self.posx + 3*self.sizex/100 ,self.posy + 3*self.sizey/100, 0, self.bulletspeed, self.sizex, self.sizey, 2, 0))
        elif number == 3:
            if self.level == 0:
                self.Bullets.append(Bullet(self.posx ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 3, 0))
            elif self.level < 2:
                self.Bullets.append(Bullet(self.posx - self.sizex/100,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx + self.sizex/100,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 3, 0))
            elif self.level < 4:
                self.Bullets.append(Bullet(self.posx - 3*self.sizex/100,self.posy + self.sizey/100, 3, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx + 3*self.sizex/100,self.posy + self.sizey/100, 3, self.bulletspeed, self.sizex, self.sizey, 3, 0))
            elif self.level < 6:
                self.Bullets.append(Bullet(self.posx - 3*self.sizex/100,self.posy + self.sizey/100, 3, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx - self.sizex/100,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx + self.sizex/100,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx + 3*self.sizex/100,self.posy + self.sizey/100, 3, self.bulletspeed, self.sizex, self.sizey, 3, 0))
            elif self.level < 1000:
                self.damage = 300
                self.Bullets.append(Bullet(self.posx - 5*self.sizex/100,self.posy + 3*self.sizey/100, 5, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx - 3*self.sizex/100,self.posy + self.sizey/100, 3, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx ,self.posy, 0, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx + 3*self.sizex/100,self.posy + self.sizey/100, 3, self.bulletspeed, self.sizex, self.sizey, 3, 0))
                self.Bullets.append(Bullet(self.posx + 5*self.sizex/100,self.posy + 3*self.sizey/100, 5, self.bulletspeed, self.sizex, self.sizey, 3, 0))
    def draw(self, Ecran):        
        for Bullet in self.Bullets:
            Bullet.damage = 10
            if Bullet.posy < -5:
                self.Bullets.remove(Bullet)
            Bullet.draw(Ecran)

class Chicken():
    def __init__(self, posx, posy, x_speed, y_speed, sizex, sizey, number, xposition, yposition, xfloat, xlimit, olimit):
        while True:
            x = random.randint(-1,1)
            if x != 0:
                break
        self.limit = random.randint(2,7)
        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.degrees = 0
        self.number = number
        self.xposition = xposition
        self.yposition = yposition
        self.xfloat = xfloat
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.xdone = False
        self.ydone = False
        self.Floatt = 0.25
        self.move = False
        self.Floatx = x
        self.Health = 100
        self.Lenx = 0
        self.Leny = 0
        self.xlimit = xlimit
        self.olimit = olimit
        if number > 10:
            Imgf = pygame.image.load('Icons/Chickens/Barrier'+str(number)+'.png')
            self.Lenx = 10*self.sizex/100
            self.Leny = 4*self.sizey/100
            self.Img = pygame.transform.scale(Imgf, (self.Lenx, self.Leny))
            self.Health = 2000
            if number == 12:
                self.Health = 3500
        else:
            Imgf = pygame.image.load('Icons/Chickens/Chicken'+str(number)+'.png')
        if number == 1:
            self.Lenx = 6*self.sizex/100
            self.Leny = 6.2*self.sizey/100
            self.Img = pygame.transform.scale(Imgf, (self.Lenx, self.Leny))
            self.Health = 800
        elif number == 5:
            self.Lenx = 4.5*self.sizex/100
            self.Leny = 5*self.sizey/100
            self.Img = pygame.transform.scale(Imgf, (self.Lenx, self.Leny))
            self.Health = 400
        elif number == 4:
            self.Lenx = 6.6*self.sizex/100
            self.Leny = 7.2*self.sizey/100
            self.Img = pygame.transform.scale(Imgf, (self.Lenx, self.Leny))
            self.Health = 1200
        elif number == 6:
            self.Lenx = 7*self.sizex/100
            self.Leny = 11*self.sizey/100
            self.Img = pygame.transform.scale(Imgf, (self.Lenx, self.Leny))
            self.Health = 1400
        elif number == 3:
            self.Lenx = 9*self.sizex/100
            self.Leny = 7*self.sizey/100
            self.Img = pygame.transform.scale(Imgf, (self.Lenx, self.Leny))
            self.Health = 2000
        elif number == 7:
            self.Lenx = 8*self.sizex/100
            self.Leny = 8*self.sizey/100
            self.Img = pygame.transform.scale(Imgf, (self.Lenx, self.Leny))
            self.Health = 4000
    def draw(self, Ecran):
        if self.Floatt > self.limit:
            self.Floatx = -1
        elif self.Floatt < -self.limit:
            self.Floatx = 1
        self.Floatt += 0.25 * self.Floatx
        if not self.xdone:
            if abs(self.posx - self.xposition) < 3:
                self.xdone = True
            elif self.posx <= self.xposition:
                self.posx += self.x_speed
            elif self.posx >= self.xposition:
                self.posx -= self.x_speed
        elif not self.ydone:
            if abs(self.posy - self.yposition) < 3:
                self.ydone = True
            elif self.posy >= self.yposition:
                self.posy -= self.y_speed
            elif self.posy <= self.yposition:
                self.posy += self.y_speed
        if self.xdone and self.ydone and self.move:
            self.x_speed = 2 
            if self.posx > self.xlimit:
                self.xfloat = -1
            elif self.posx < self.olimit:
                self.xfloat = 1
            self.posx += self.xfloat * self.x_speed
        Ecran.blit(self.Img, (self.posx, self.posy + self.Floatt))
        if Colors.Developer:
            pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy + self.Floatt, self.Lenx, self.Leny], 3)

class ChickenDrop():
    def __init__(self, posx ,posy ,sizex, sizey, number):
        self.velo = 5
        self.fall = True
        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.y_speed = 5
        if number == 4:
            self.y_speed = 2
        self.number = number
        self.remove = 2
        self.counter = 0
        self.GiftLenx = 4*self.sizex/100
        self.GiftLeny = 4*self.sizey/100
        Gift1 = pygame.image.load('Icons/Bullets/Gift2.png')
        Gift2 = pygame.image.load('Icons/Bullets/Gift1.png')
        Gift3 = pygame.image.load('Icons/Bullets/Gift3.png')
        self.Gift1 = pygame.transform.scale(Gift1, (self.GiftLenx, self.GiftLeny))
        self.Gift2 = pygame.transform.scale(Gift2, (self.GiftLenx, self.GiftLeny))
        self.Gift3 = pygame.transform.scale(Gift3, (self.GiftLenx, self.GiftLeny))
        ImgUpgrade1 = pygame.image.load('Icons/Chickens/Up1.4.png')
        ImgUpgrade2 = pygame.image.load('Icons/Chickens/Up1.3.png')
        ImgUpgrade3 = pygame.image.load('Icons/Chickens/Up1.2.png')
        ImgUpgrade4 = pygame.image.load('Icons/Chickens/Up1.1.png')
        self.UPLenx = 3.5*self.sizex/100
        self.UPLeny = 5*self.sizey/100
        self.UP1 = pygame.transform.scale(ImgUpgrade1, (self.UPLenx, self.UPLeny))
        self.UP2 = pygame.transform.scale(ImgUpgrade2, (self.UPLenx, self.UPLeny))
        self.UP3 = pygame.transform.scale(ImgUpgrade3, (self.UPLenx, self.UPLeny))
        self.UP4 = pygame.transform.scale(ImgUpgrade4, (self.UPLenx, self.UPLeny))
        self.UP = self.UP1
        Img1= pygame.image.load('Icons/Chickens/Egg.png')
        Img2= pygame.image.load('Icons/Chickens/Chick.png')
        Img3= pygame.image.load('Icons/Chickens/Leg.png')
        Img4= pygame.image.load('Icons/Chickens/Burger.png')
        self.EggLenx = 2*self.sizex/100
        self.EggLeny = 3*self.sizey/100
        self.LegLenx = 3*self.sizex/100
        self.LegLeny = 4*self.sizey/100
        self.BurgerLenx = 4*self.sizex/100
        self.BurgerLeny = 6*self.sizey/100
        self.ChickLenx = 2*self.sizex/100
        self.ChickLeny = 2*self.sizey/100
        if number == 9:
            self.number = 1
            self.EggLenx = 4*self.sizex/100
            self.EggLeny = 7*self.sizey/100
            self.Egg = pygame.transform.scale(Img1,(self.EggLenx, self.EggLeny))
        else:
            self.Egg = pygame.transform.scale(Img1,(self.EggLenx, self.EggLeny))
        self.Leg = pygame.transform.scale(Img3,(self.LegLenx, self.LegLeny))
        self.Burger = pygame.transform.scale(Img4,(self.BurgerLenx, self.BurgerLeny))
        self.Chick = pygame.transform.scale(Img2,(self.ChickLenx, self.ChickLeny))
    def draw(self, Ecran):
        if self.number == 1:
            self.posy += self.y_speed
            Ecran.blit(self.Egg,(self.posx, self.posy))
            if Colors.Developer:
                pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.EggLenx, self.EggLeny], 3)
        elif self.number == 2:
            self.posy += self.y_speed
            Ecran.blit(self.Leg,(self.posx, self.posy))
            if Colors.Developer:
                pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.LegLenx, self.LegLeny], 3)
        elif self.number == 3:
            self.posy += self.y_speed
            Ecran.blit(self.Burger,(self.posx, self.posy))
            if Colors.Developer:
                pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.BurgerLenx, self.BurgerLeny], 3)
        elif self.number == 4:
            if self.counter == 15:
                self.counter = 0
                if self.UP == self.UP1:
                    self.UP = self.UP2
                elif self.UP == self.UP2:
                    self.UP = self.UP3
                elif self.UP == self.UP3:
                    self.UP = self.UP4
                elif self.UP == self.UP4:
                    self.UP = self.UP1
            self.posy += self.y_speed
            Ecran.blit(self.UP, (self.posx, self.posy))
            if Colors.Developer:
                pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.UPLenx, self.UPLeny], 3)
            self.counter += 1
        elif self.number == 5:
            self.posy += self.y_speed
            Ecran.blit(self.Chick, (self.posx, self.posy))
            if Colors.Developer:
                pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.ChickLenx, self.ChickLeny], 3)
        elif self.number == 6:
            self.posy += self.y_speed
            Ecran.blit(self.Gift1, (self.posx, self.posy))
            if Colors.Developer:
                pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.GiftLenx, self.GiftLeny], 3)
        elif self.number == 7:
            self.posy += self.y_speed
            Ecran.blit(self.Gift2, (self.posx, self.posy))
            if Colors.Developer:
                pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.GiftLenx, self.GiftLeny], 3)
        elif self.number == 8:
            self.posy += self.y_speed
            Ecran.blit(self.Gift3, (self.posx, self.posy))
            if Colors.Developer:
                pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.GiftLenx, self.GiftLeny], 3)

class Rocket():
    def __init__(self, posx, posy, sizex, sizey, xpos, ypos):
        self.RotateFig = False
        self.Rotate = 45
        self.Rotateinit = 0
        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.xpos = xpos
        self.ypos = ypos
        self.x_speed = 0
        self.y_speed = 0
        self.ImgR = pygame.image.load('Icons/Rocket2.png')
        self.Img = pygame.transform.scale(self.ImgR, (sizex/100, sizey/100))
        if posx - xpos > 100:
            self.Img = pygame.transform.rotate(self.Img, self.Rotate)
            self.y_speed = -3
            self.x_speed = -4
        elif xpos - posx > 100:
            self.Rotate *= -1
            self.Img = pygame.transform.rotate(self.Img, self.Rotate)
            self.y_speed = -3
            self.x_speed = 4
        else:
            self.y_speed = -4
    def draw(self, Ecran):
        Ecran.blit(self.Img,(self.posx, self.posy))
        if self.x_speed !=0 and self.y_speed !=0:
            if abs(self.posx - self.xpos) > 3 and abs(self.posy - self.ypos) < 3:
                self.RotateFig = True
                self.y_speed = 0
            elif abs(self.posx - self.xpos) < 3 and abs(self.posy - self.ypos) > 3:
                self.RotateFig = True
                self.x_speed = 0
        if self.RotateFig:
            if self.Rotate == -35:
                self.Rotate = 5
                self.Rotateinit = 5
            elif self.Rotate == 35:
                self.Rotate = -5
                self.Rotateinit = -5
            else:
                if self.Rotateinit > 0 and self.Rotateinit < 35:
                    self.Rotateinit += 5
                    self.Img = pygame.transform.rotate(self.Img, self.Rotate)
                elif self.Rotateinit < 0 and self.Rotateinit > -35:
                    self.Rotateinit -= 5
                    self.Img = pygame.transform.rotate(self.Img, self.Rotate)
                else:
                    if self.x_speed == 0:
                        self.Img = pygame.transform.scale(self.ImgR, (self.sizex/50, self.sizey/25))
                    elif self.x_speed < 0:
                        self.Img = pygame.transform.scale(self.ImgR, (self.sizex/50, self.sizey/25))
                        self.Img = pygame.transform.rotate(self.Img, 90)
                    elif self.x_speed > 0:
                        self.Img = pygame.transform.scale(self.ImgR, (self.sizex/50, self.sizey/25))
                        self.Img = pygame.transform.rotate(self.Img, -90)
                    self.Rotate = False
        self.posy += self.y_speed
        self.posx += self.x_speed

class Asteroids():
    def __init__(self ,sizex ,sizey, number, directie):
        self.sizex = sizex
        self.sizey = sizey
        self.number = number
        self.directie = directie
        self.imgR = pygame.image.load('Icons/Asteroid'+ str(number) + '.png')
        if directie == 1:
            self.posx = random.randint(50, self.sizex)
            self.posy = -5
            self.x_speed = 0
            self.y_speed = random.randint(4, 7)
            self.x= random.randint(7, 12)
            self.Img = pygame.transform.scale(self.imgR, (self.x*self.sizex/100, self.x*self.sizey/100))
        elif directie == 2:
            self.posx = random.randint(-200, -20)
            self.posy = random.randint(-100*self.sizey/100, 70*self.sizey/100)
            self.x_speed = random.randint(2,6)
            self.y_speed = random.randint(2, self.x_speed)
            self.x= random.randint(7, 12)
            self.Img = pygame.transform.scale(self.imgR, (self.x*self.sizex/100, self.x*self.sizey/100))
        elif directie == 3:
            self.posx = random.randint(self.sizex, self.sizex + 50)
            self.posy = random.randint(-100*self.sizey/100, 90*self.sizey/100)
            self.x_speed = -random.randint(2, 7)
            self.y_speed = random.randint(2, -self.x_speed)
            self.x= random.randint(7, 12)
            self.Img = pygame.transform.scale(self.imgR, (self.x*self.sizex/100, self.x*self.sizey/100))
        if number == 1:
            self.health = self.x * 100
        else:
            self.health = self.x * 200
    def draw(self, Ecran):
        Ecran.blit(self.Img, (self.posx, self.posy))
        self.posx += self.x_speed
        self.posy += self.y_speed
        if Colors.Developer:
            pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy, self.x*self.sizex/100, self.x*self.sizey/100], 3)

class ChickenBoss():
    def __init__(self, posx ,posy ,sizex ,sizey ,number ,xposition, yposition):
        while True:
            x = random.randint(-1,1)
            if x != 0:
                break
        self.limit = random.randint(2,7)
        self.Floatt = 0.25
        self.Floatx = x
        self.xFloat = 3
        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.number = number
        self.xdone = False
        self.ydone = False
        self.moved = False
        self.xposition = xposition
        self.yposition = yposition
        self.Lenx = 26*self.sizex/100
        self.Leny = 32*self.sizey/100
        self.xlimit = 0 + self.Lenx/2
        self.xposition = self.xposition - self.Lenx/2
        self.Health = 15000
        self.x_speed = 3
        self.y_speed = 4
        ImgR = pygame.image.load('Icons/Chickens/ChickenBoss' + str(self.number) + '.png')
        if number == 1:
            self.Leny = 34*self.sizey/100
        self.Img = pygame.transform.scale(ImgR, (self.Lenx, self.Leny))
    def draw(self, Ecran):
        if self.Floatt > self.limit:
            self.Floatx = -1
        elif self.Floatt < -self.limit:
            self.Floatx = 1
        self.Floatt += 0.25 * self.Floatx
        if abs(self.posy - self.yposition) > 3 and not self.ydone:
            if self.posy > self.yposition:
                self.posy -= self.y_speed
            else:
                self.posy += self.y_speed
        elif abs(self.posx - self.xposition) > 3 and not self.xdone:
            self.ydone = True
            if self.posx > self.xposition:
                self.posx -= self.x_speed
            else:
                self.posx += self.x_speed
        else:
            self.xdone = True
        if self.xdone and self.ydone:
            self.x_speed = 3
            if self.posx >= self.sizex - self.Lenx and not self.moved:
                self.moved = True
                self.xFloat = -1
            elif self.posx <= 0 and self.moved:
                self.xFloat = 1
                self.moved = False
            self.posx += self.x_speed * self.xFloat
        Ecran.blit(self.Img, (self.posx, self.posy + self.Floatt))
        if Colors.Developer:
            pygame.draw.rect(Ecran, Colors.Red,[self.posx,  self.posy + self.Floatt, self.Lenx, self.Leny], 3)
