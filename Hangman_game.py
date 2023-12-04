# Pygame Hangman


import sys, pygame
import random, math


# -----window stuffs--------------------------
screen = pygame.display.set_mode((900,600))
pygame.init()
clock = pygame.time.Clock()

# -------color variables-------
clrWhite = (255,255,255)
clrBlack = (0,0,0)
clrBlue = (0,0,255)
clrLightGray = (211,211,211)
# -------Fonts & Background----------------------------------------------------------
font = pygame.font.Font('Font.ttf', 50) #load new font instead of system font
small_font = pygame.font.SysFont('Calibri', 25, True, True)
Background = pygame.image.load('background1.jpg') #load an image for background


# -------------class for creating button on the screen and pressing button-----
class button:
	def __init__(self, text, x, y, w, h, textSize):
		# variables that are neccessary for creating button
		self.rect = pygame.Rect(x,y,w,h)
		self.text = text
		self.textSize = textSize
		self.mouse = False
		self.clicked = False
		self.font = pygame.font.Font('Font.ttf',self.textSize)
		
	def draw(self):
		# Deals with mouseover display
		if self.mouse == True:
			pygame.draw.rect(screen, (clrWhite), self.rect, 0,10)
			self.letter = self.font.render(self.text, True, clrBlue)
			screen.blit(self.letter, (self.rect.x+10, self.rect.y-2))
		else:
			pygame.draw.rect(screen, (clrWhite), self.rect, 3, 10)
			self.letter = self.font.render(self.text, True, clrWhite)
			screen.blit(self.letter, (self.rect.x+12, self.rect.y-2))
	
			
	def buttonclicked (self):
		# Deals with click and returned values
		pos = pygame.mouse.get_pos()
		letterclicked = None
		if self.rect.collidepoint(pos):
			self.mouse = True
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				letterclicked = self.text
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
		else:
			self.mouse = False
		if letterclicked == None:
			return ''
		else:
			return letterclicked

#------------buttons------------------------------------
Easy_Button = button('Easy', 375, 200, 140, 50, 50)	
Medium_Button = button('Medium', 370, 310, 190, 50, 50)
Hard_Button = button('Hard', 375, 420, 140, 50, 50)
Back_Button = button('Back', 380, 560, 90, 30,30)
Play_Button = button('PLAY', 384, 480, 140, 50, 50)
Quit_Button = button('Quit', 420, 560, 90, 30, 30)

# -------------variables for displaying words-----------
LetterGuessed = ''
words = open("Dictionary.txt").read().split("\n")
Answer = random.choice(words) #choose a random word from the Dictionary 
Reveal = ''
#As Error is added by one, gallow gets added one
Errors = 0 

# --------------class for word displaying------------------------------------------
class word:
	def __init__(self, text, textsize, level):
		#when a level is chosen, word that is in range of the level becomes Answer
		self.Answer = random.choice(words)
		self.Selection = level
		r, R = 0, 0
		if True:
			if self.Selection == 'Easy' :
				r = 10
				R = 100
			elif self.Selection == 'Medium':
				r = 6
				R = 9
			elif self.Selection == 'Hard ':
				r = 1
				R = 5
		
		while (len(self.Answer) < r or len(self.Answer) > R):
			self.Answer = random.choice(words)
			if len(self.Answer) >= r and len(self.Answer) <= R:
				break
		self.x = 100
		self.y = 450
		
		self.textsize = textsize
		self.text = text
		self.font = pygame.font.Font('Font.ttf',self.textsize)
		self.letter = self.font.render(letter, True, clrWhite)

	def draw(self):
		#determines how many underlines are needed
		self.word = self.font.render(self.Answer, True, clrWhite)
		Reveal = ''
		Errors = 0
		for char in self.Answer:
			if char in LetterGuessed: # p i _ _ a 
				Reveal += char + ' '
			else:
				Reveal += '_ '
				
		if len(self.Answer) >= 9:
			screen.blit(self.word, (320,200))
			
		else:
			screen.blit(self.word, (400,200))
			
		for char in LetterGuessed:
			if char not in self.Answer:
				Errors += 1
			if char in LetterGuessed:
				Errors == Errors		
				
	def word_display(self):
		#draws the words with underlines
		position = 0
		
		for char in LetterGuessed:
			position += 1
			
			if char == '_':
				pygame.draw.line(screen, clrWhite, (self.x + position*30, self.y), (self.x + position*30 + 15, self.y), 2)
			else:
				
				self.Font = self.letter
				#another variable = self.letter
				screen.blit(self.FONT, (self.x + position*30 + 2, self.y - 30))
				
	
# level in word class-----------------
Level1 = word(Answer, 50, 'Easy')
Level2 = word(Answer, 50, 'Medium')
Level3 = word(Answer, 50, "Hard")
# keyboard alphabets--------------------
Alphabet = "abcdefghijklmnopqrstuvwxyz"
Keyboard = []	

# class for displaying hangman----------------------------------------------------
class HangingMan:
	def __init__(self,x,y):
		#displays hangman gallows
		self.x = x
		self.y = y
		self.image = []
		self.words = word
		self.clicked = False
		
		self.mouse = False
		for x in range (0,7):
			# display hangman gallows on the screen
			self.image.append(pygame.image.load('hangman' + str(x) + '.png'))		
			
	def draw(self,errors):
		#displays hangman gallows depending on the number of Errors
		screen.blit(self.image[Errors], (self.x, self.y))
		
	def letterbutton(self):
		#buttons disappear when they are clicked
		index = 0
		Alphabet = "abcdefghijklmnopqrstuvwxyz"
		for letter in Alphabet:
			if letter >= 'a' and letter <= 'm':
				Keyboard.append(button(letter,10*index, 375, 50,50, 50))
				index += 7
				if self.mouse == True:
					Alphabet = Alphabet.replace(LetterGuessed, '')
					print(Alphabet)
					for letter in Alphabet:
						Keyboard.append(button(letter,10*index, 375, 50,50, 50))
				
			elif letter >= 'n' and letter <= 'z':
				Keyboard.append(button(letter,(index-91)*10, 450, 50,50,50))
				index += 7

# Create a Haninging Object Instance------------------
HangingMan = HangingMan(30,55)

#==================button functions=====================================			
def quit():
	#Pre: creates quit button on the game screen
	#Post: quit the game when quit button is pressed
	rungame = True
	
	while rungame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				rungame = False
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				if Quit_Button.buttonclicked():
					pygame.quit()
					sys.exit()
		
		pygame.display.update()
		
def gameover():
	#Pre: determines whether the user wins or loses
	#Post: Depending on the user's score, win or lose screen gets displayed
	
	rungame = True
	win = font.render("Congrats! You win!", True, (clrWhite))
	lost = font.render("Oops, You lose!", True, clrWhite)
	while rungame:
		for event in pygame.event.get():
			if pygame.type == pygame.QUIT:
				rungame = False
				pygame.quit()
				sys.exit()
				
			if Reveal == Answer:
				screen.blit(win, [150,300])
				if event.type == pygame.MOUSEBUTTONDOWN:
					if Quit_Button.buttonclicked():
						quit()
				
				
			elif Errors == 6:
				screen.blit(lose, [150,300])
				if event.type == pygame.MOUSEBUTTONDOWN:
					if Quit_Button.buttonclicked():
						quit()
				
		screen.blit(Background, (-200,0))	
				
		key = ''
		key += Quit_Button.buttonclicked()
		Quit_Button.draw()	


def easy():
	#Pre: creates a button for easy level on Play screen
	# Post: lead to easy level game when easy button is pressed
	pygame.display.set_caption("Easy Mode")

	rungame = True
	while rungame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				rungame = False
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				if Back_Button.buttonclicked():
					play()
				
		screen.blit(Background, (-200,0))
		key = ''
		key += Back_Button.buttonclicked()
		key += Quit_Button.buttonclicked()
		#displays keyboard
		for letter in range (len(Keyboard)):
			key += Keyboard[letter].buttonclicked()
			Keyboard[letter].draw()
			
		Back_Button.draw()
		Quit_Button.draw()
		HangingMan.draw(Errors)
		HangingMan.letterbutton()
		
		Level1.draw()
		word.word_display(LetterGuessed)

		pygame.display.update()	

def medium():
	#Pre: creates medium button on Play screen
	#Post: leads to medium level game when medium button is pressed
	
	#name of the screen
	pygame.display.set_caption("Medium Mode")
	
	rungame = True
	while rungame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				rungame = False
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				if Back_Button.buttonclicked():
					play()
					
		screen.blit(Background, (-200,0))
		key = ''
		key += Back_Button.buttonclicked()
		key += Quit_Button.buttonclicked()
		HangingMan.draw(Errors) # draws gallows depending on the number of errors
		Back_Button.draw() 
		Quit_Button.draw() 
		#displays keyboard
		for letter in range (len(Keyboard)):
			key += Keyboard[letter].buttonclicked()
			Keyboard[letter].draw()
			
		HangingMan.letterbutton()
		Level2.draw()
		word.word_display(LetterGuessed)
		pygame.display.update()	
		
def hard():
	#Pre: creates hard button on Play screen
	#Post: leads to hard level game when hard button is pressed
	
	#name of the screen
	pygame.display.set_caption("Hard Mode")
	
	sLettersUsed = ''
	rungame = True
	while rungame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				rungame = False
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				if Back_Button.buttonclicked():
					play()
					
		screen.blit(Background, (-200,0))
		key = ''
		key += Back_Button.buttonclicked()
		key += Quit_Button.buttonclicked()
		HangingMan.draw(Errors)
		Back_Button.draw()
		Quit_Button.draw()
		#displays keyboard
		for letter in range (len(Keyboard)):
			key += Keyboard[letter].buttonclicked()
			Keyboard[letter].draw()
			
		HangingMan.letterbutton()
		Level3.draw()
		word.word_display(LetterGuessed)
		pygame.display.update()	
		
	
def play():
	#Pre: creates Play button on the welcome screen
	#Post: leads to Choose Level screen when Play button is pressed
	sLettersUsed = ''
	
	pygame.display.set_caption("Let's play!")
	
	ChooseLevel = font.render("Choose level:", True, clrWhite)
	rungame = True
	while rungame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				rungame = False
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.MOUSEBUTTONDOWN:
			
				if Easy_Button.buttonclicked():
					easy() # choose easy level game
				if Medium_Button.buttonclicked():
					medium() # choose medium level game
				if Hard_Button.buttonclicked():
					hard() # choose hard level game
				if Back_Button.buttonclicked():
					welcome() # when Back button is pressed, go to the very first screen
				
		
				
		screen.blit(Background, (-200,0))
		screen.blit(ChooseLevel, [275,90])
		
		
		key = ''
		key += Easy_Button.buttonclicked()
		key += Medium_Button.buttonclicked()
		key += Hard_Button.buttonclicked()
		key += Back_Button.buttonclicked()
		
		#displays level buttons
		Easy_Button.draw()
		Medium_Button.draw()
		Hard_Button.draw()
		Back_Button.draw()
		
		if key != None:
			sLettersUsed += key
			

		
		pygame.display.update()
		

def welcome ():
	# Pre: creates welcome screen with the title and the instruction of the game
	# Post: displays the instruction and the Play button on the screen to start
	sLettersUsed = ''
	pygame.display.set_caption("Hangman Welcome")
	# welcoming and instruction of Hangman game
	text = font.render("Welcome to Hangman game", True, (0,0,255))
	text_1 = small_font.render("Let's play Hangman! Determine the word by guessing letters that are in the word.", True, clrWhite)
	text_2 = small_font.render("Every time you guess a letter, gallows will be drawn.", True, clrWhite)
	text_3 = small_font.render("Guess the word before all gallows are used!", True, clrWhite)
	text_4 = small_font.render("Good luck!", True, clrWhite)
	
	
	rungame = True				
	while rungame:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				rungame = False
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.MOUSEBUTTONDOWN:
			
				if Play_Button.buttonclicked():
					play()
					
		screen.fill(clrWhite)
		screen.blit(Background, (-200,0))
		screen.blit(text, [120,150])
		screen.blit(text_1, [25, 250])
		screen.blit(text_2, [185, 300])
		screen.blit(text_3, [223,380])
		screen.blit(text_4, [398,415])
		key = ''
		key += Play_Button.buttonclicked()
		
		Play_Button.draw()
		
		if key != None:
			sLettersUsed += key
			

		
		pygame.display.update()
		clock.tick(60)

welcome()
	




x = input()
pygame.quit()
