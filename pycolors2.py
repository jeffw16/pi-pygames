import pygame
import random

pygame.init()

window = pygame.display.set_mode((800, 600))

r = 0
g = 0
b = 0
rup = True
gup = False
bup = True

while True:
	if r > 254:
		rup = False
	if g > 254:
		gup = False
	if b > 254:
		bup = False
	if r < 1:
		rup = True
	if g < 1:
		gup = True
	if b < 1:
		bup = True
	if rup:
		rui = random.randint(1,30)
		if (rui + r) > 255:
			r = 255
			rup = False
		else:
			r += rui
	if gup:
		gui = random.randint(1,30)
		if (gui + g) > 255:
			g = 255
			gup = False
		else:
			g += gui
	if bup:
		bui = random.randint(1,30)
		if (bui + b) > 255:
			b = 255
			bup = False
		else:
			b += bui
	if not rup:
		rdi = random.randint(1,30)
		if (r - rdi) < 0:
			r = 0
			rup = True
		else:
			r -= rdi
	if not gup:
		gdi = random.randint(1,30)
                if (g - gdi) < 0:
			g = 0
			gup = True
		else:
			g -= gdi
	if not bup:
		bdi = random.randint(1,30)
		if (b - bdi) < 0:
			b = 0
			bup = True
		else:
			b -= bdi
	pygame.draw.rect(window, (r,g,b), (0,0,800,600) )
	pygame.draw.circle(window, (255,255,255), (400,300), 200, 0)
	pygame.display.update()
