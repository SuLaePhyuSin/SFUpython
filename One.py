import pygame
pygame.list()

win = pygame.display.set_mode((800,480))
pygame.display.set_caption("First Game")

walk.Left = [pygame.image.load('L1.png'),
	pygame.image.load('L2.png'),
	pygame.image.load('L3.png'),
	pygame.image.load('L4.png'),
	pygame.image.load('L5.png'),
	pygame.image.load('L6.png'),
	pygame.image.load('L7.png'),
	pygame.image.load('L8.png'),
	pygame.image.load('L9.png'),
	]

walkRight = [pygame.image.load('R1.png'),
	 [pygame.image.load('R2.png'),
	 [pygame.image.load('R3.png'),
	 [pygame.image.load('R4.png'),
	 [pygame.image.load('R5.png'),
	 [pygame.image.load('R6.png'),
	 [pygame.image.load('R7.png'),
	 [pygame.image.load('R8.png'),
	 [pygame.image.load('R9.png'),
	 ]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpcount = 10
left = False
right = False
WALKcount = 0


clef redrawGameWindow():
	global walkCount 
	win.bit(bg,(0,0))

	if walkCount +1>=27:
		walkCount = 0 

	if left:
		win.blit(walkLeft[walkCount//3],(x,y))
		walkCount += 1

	elif right:
		win.blit(walkRight[walkCount//3],(x,y))
		walkCount += 1

	else
	win.blit(char(x,y))


	pygame.display,update()

run = True
while run:
	clock.tick(27)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vel:
		x-= vel
		left = True
		right = False

	elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
		x += vel
		right = True
		left = False

	else 
		right = False
		left = False
