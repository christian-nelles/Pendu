import pygame
import random
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 30)

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mots.txt'), 'r') as file:
    allText = file.read() 
    word_to_guess = random.choice(list(map(str, allText.split())))
guessed_word = ['_'] * len(word_to_guess)
incorrect_guesses = []
max_attempts = 6
attempts_left = max_attempts

def draw_hangman(attempts_left):
    if attempts_left <= 5:
        pygame.draw.circle(screen, BLACK, (650, 320), 25, 5) #tete
    if attempts_left <= 4:
        pygame.draw.line(screen, BLACK, (650, 340), (650, 450), 5) #corp
    if attempts_left <= 3:
        pygame.draw.line(screen, BLACK, (650, 350), (630, 430), 5) #bras.g
    if attempts_left <= 2:
        pygame.draw.line(screen, BLACK, (650, 350), (670, 430), 5) #bras.d
    if attempts_left <= 1:
        pygame.draw.line(screen, BLACK, (650, 450), (630, 530), 5) #jambe.g
    if attempts_left <= 0:
        pygame.draw.line(screen, BLACK, (650, 450), (670, 530), 5) #jambe.d

def draw_text(text, x, y, font, color):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (500, 250), (500, 550), 5) #poutre
    pygame.draw.line(screen, BLACK, (425, 550), (575, 550), 5) #sol
    pygame.draw.line(screen, BLACK, (500, 250), (650, 250), 5) #barre
    pygame.draw.line(screen, BLACK, (650, 250), (650, 300), 5) #corde
    pygame.draw.line(screen, BLACK, (500, 250), (550, 250), 5) #raccord
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            guess = pygame.key.name(event.key).lower()
            if guess.isalpha() and guess not in incorrect_guesses and guess not in guessed_word:
                if guess in word_to_guess:
                    for i in range(len(word_to_guess)):
                        if word_to_guess[i] == guess:
                            guessed_word[i] = guess
                else:
                    incorrect_guesses.append(guess)
                    attempts_left -= 1

    draw_text("Mot à deviner: " + " ".join(guessed_word), 50, 50, font, BLACK)
    
    draw_text("Lettres incorrectes: " + ", ".join(incorrect_guesses), 50, 100, small_font, BLACK)
    
    draw_text(f"Tentatives restantes: {attempts_left}", 50, 150, small_font, BLACK)

    draw_hangman(attempts_left)

    if "".join(guessed_word) == word_to_guess:
        draw_text("Gagné! Le mot était: " + word_to_guess, 50, 200, font, GREEN)
        pygame.display.update()
        pygame.time.wait(2000)
        running = False

    if attempts_left == 0:
        draw_text(f"Perdu! Le mot était: {word_to_guess}", 50, 200, font, RED)
        pygame.display.update()
        pygame.time.wait(2000)
        running = False

    pygame.display.update()

pygame.quit()