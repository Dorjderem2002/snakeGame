import pygame
import random

pygame.init()

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake Challenge")

snakeSize = 30

snakeX = [300,300,300,300]
snakeY = [300,330,360,390]

velX = 0
velY = 0

speed = 30

newPosX = 300
newPosY = 300

score = 0

fruitX = random.randrange(0,20)
fruitY = random.randrange(0,20)

print(fruitX)

isRunning = True

while isRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False

	window.fill((0,0,0))

	keys=pygame.key.get_pressed()

	if keys[pygame.K_RIGHT]:
		velX = 1
		velY = 0
	if keys[pygame.K_LEFT]:
		velX = -1
		velY = 0
	if keys[pygame.K_DOWN]:
		velY = 1
		velX = 0
	if keys[pygame.K_UP]:
		velY = -1
		velX = 0

	snakeX.pop()
	snakeY.pop()

	newPosX = snakeX[0] + speed * velX
	newPosY = snakeY[0] + speed * velY

	snakeX.insert(0,newPosX)
	snakeY.insert(0,newPosY)

	pygame.draw.rect(window, (255,0,0), (fruitX * snakeSize,fruitY * snakeSize,snakeSize,snakeSize))

	for i in range(0,len(snakeX)):
		pygame.draw.rect(window, (255,255,255), (snakeX[i],snakeY[i],snakeSize,snakeSize))

	if snakeX[0] == fruitX * snakeSize and snakeY[0] == fruitY * snakeSize:
		fruitX = random.randrange(0,20)
		fruitY = random.randrange(0,20)
		score += 1
		print(score)

	pygame.display.update()

	pygame.time.delay(100)
pygame.quit()
