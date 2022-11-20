import pygame, random ,threading
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
score = 0
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space XS")
clock = pygame.time.Clock() 	 	

def scores(surface, text, size, x , y ):
	font = pygame.font.Font("scoree.ttf", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite, threading.Thread):
	def __init__(self):
		super().__init__()
		threading.Thread.__init__(self)
		self.image = pygame.image.load("novita.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0

	def update(self):
		pos_mouse = pygame.mouse.get_pos()
		player.rect.x = pos_mouse[0]
		player.rect.y = 500
		

	def dispara(self):
		laser =  Laser(self.rect.centerx, self.rect.top)
		all_sprites.add(laser)
		laser_list.add(laser)


class Asteroide(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("asteroide3.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width) 
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-3, 3)
	
	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)

class Laser(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.image.load("laser4.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.y = y
		self.speedy = -10


	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()


class Enemigos(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("ovni1.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = random.randrange(HEIGHT - self.rect.height)
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.speedy = random.randrange(1, 10)
	def update(self):
		# self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)
			# if self.rect.left < 0 :
			
		
asteroides_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
enemige_list = pygame.sprite.Group()

player = Player()
# player.start()

all_sprites.add(player)

background = pygame.image.load("uni.png").convert()


for i in range(10):
	astero = Asteroide()
	all_sprites.add(astero)
	asteroides_list.add(astero)

# dato = 0
# if score > 10:
	for i in range(3):	
		enemige = Enemigos()
		all_sprites.add(enemige)
		enemige_list.add(enemige)	
# Game start
nova = True
while nova:
	# Velocidad de FDS
	clock.tick(60)
	# Eventos
	for event in pygame.event.get():
		# Verifica el cierre de ventana
		print(event)
		if event.type == pygame.QUIT:
			running = False
	
		elif event.type == pygame.MOUSEBUTTONDOWN:
			player.dispara()
			
	# Actualiza

	all_sprites.update()

	# COLOSIONES LASER
	disparo = pygame.sprite.groupcollide(asteroides_list, laser_list, True, True)
	for d in disparo:
		score += 2
		astero = Asteroide()
		all_sprites.add(astero)
		asteroides_list.add(astero)

	disparo =  pygame.sprite.spritecollide(player, asteroides_list , True)
	if disparo:
		nova = False
	# Color de Fondo
	# screen.fill(BLACK)
	screen.blit(background, [0, 0])
	all_sprites.draw(screen)

	# Puntos
	scores(screen, str(score), 25, WIDTH // 2, 20)
	pygame.display.flip()

pygame.quit()

# if __name__ == '__main__':
# 	player = Player()
# 	# player.start()
# 	all_sprites.add(player)
	