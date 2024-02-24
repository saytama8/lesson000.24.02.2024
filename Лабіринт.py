from pygame import *


fps = time.Clock()
Fps = 60



class game(sprite.Sprite):
    def __init__(self,player_image, p_x, p_y, p_s):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(100,100))
        self.speed = p_s
        self.rect= self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y



    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



class Move(game):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -=  self.speed
        if keys[K_RIGHT] and self.rect.x<620:
            self.rect.x +=  self.speed
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -=  self.speed
        if keys[K_DOWN] and self.rect.y<420:
            self.rect.y +=  self.speed


window = display.set_mode((700,500))
display.set_caption("levron mr olimpia )))")


backgroud = transform.scale(image.load("cl.jpeg"),(700,500))
levron = Move("levron.png",5,420,4)
coleman = game("coleman.gif",550,280,2)
medal = game("medal.png",550,400,0)


game = True

mixer.init()
mixer.music.load("cevin.mp3")
mixer.music.play()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False





    window.blit(backgroud,(0,0))
    coleman.reset()
    levron.reset()
    medal.reset()


    display.update()
    fps.tick(Fps)













