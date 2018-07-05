import pygame
import time as tm
import random
pygame.init()
width=800
height=600
tck=20

screen=pygame.display.set_mode((width,height))
time=pygame.time.Clock()
t=int(tm.time())

def score_count(dodged):
	font=pygame.font.SysFont(None,25)
	text=font.render("Score : " + str(dodged),True,(255,255,255))
	screen.blit(text,(0,0))

def text_obj(text,font):
	text_Surf=font.render(text,True,(255,0,0))
	return text_Surf,text_Surf.get_rect()

def message_display(text):
	font=pygame.font.Font("freesansbold.ttf",70)
	font_surf,font_rect=text_obj(text,font)
	font_rect.center=(width/2,height/2)
	screen.blit(font_surf,font_rect)

	pygame.display.update()

	tm.sleep(3)

	process()



def obstacles(x_pos,y_pos,obj_width,obj_height,color):
	pygame.draw.rect(screen,color,[x_pos,y_pos,obj_width,obj_height])

def lane(lane_widht,x_pos):
	pygame.draw.rect(screen,(2,2,2),[x_pos,0,lane_widht,height])


def crash():
	message_display('YOU CRASHED!!')


def process():
	
	pygame.display.set_caption('First Project')
	crashed=False
	x=(width/2)
	y=height-90
	x_change=0
	y_change=5
	y_pos=-400
	x_width=80
	y_width=80
	car_widht=86
	car_height=68
	start=0
	end=width
	lane_width=0
	dodged=0
	x_pos=random.randrange(start,end)


	color=(random.randint(0,100),random.randint(0,150),random.randint(0,200))
	while not crashed:
		for even in pygame.event.get():
			if even.type==pygame.QUIT:			
				pygame.quit()
				quit()

			if even.type==pygame.KEYDOWN:
				if even.key==pygame.K_LEFT:
					x_change=-5
				elif even.key==pygame.K_RIGHT:
					x_change=5
				
			if even.type==pygame.KEYUP:
				if even.key==pygame.K_LEFT or even.key==pygame.K_RIGHT:
					x_change=0
				

			

				
		x+=x_change					
		screen.fill((200,150,0))
		car(x,y)
		lane(lane_width,0)
		lane(lane_width,width-lane_width)
		score_count(dodged)
		obstacles(x_pos,y_pos,x_width,y_width,color)
		y_pos+=y_change




		if(x<start or x>end-84):
			crash()

		if(y_pos>height):
			y_pos=0
			x_pos=random.randrange(start,end)
			color=(random.randint(0,100),random.randint(0,150),random.randint(0,200))
			dodged+=1
			y_change+=0.2
			if(dodged%10==0 and dodged!=0):
				if(lane_width<=200):
					lane_width+=80
					start+=lane_width
					end-=lane_width
				
					x_width+=20
					y_width+=20


		


		if((x_pos>=x and x_pos<=x+car_widht) or (x_pos+x_width>=x and x_pos+x_width<=x+car_widht)):
			if((y_pos>=y and y_pos<=y+car_height) or (y_pos+y_width>+y and y_pos+y_width<=y+car_height)):
				crash()




		pygame.display.update()
		time.tick(50)
		# time.tick(tck)
		# if(int(tm.time()-t)%30==0 and tck<=60):
		# 	tck=tck+10


		# if(y>0):
		# 	y=y-5+y_change
		# else:
		# 	y=height*0.8	
						
			



def car(x,y):
	screen.blit(carImg,(x,y))


if __name__ == '__main__':
	carImg=pygame.image.load('D://car.png')
	process()
