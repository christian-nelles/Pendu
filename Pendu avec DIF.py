import pygame
import random
import os
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("None", 30)


def start_animation(current_step):
    global animating, step_start_index, step_images, next_change_time, current_image_index
    animating = True
    current_image_index = 0
    step_start_index = sum(animation_steps[:current_step])
    step_images = images_with_durations[step_start_index:step_start_index + animation_steps[current_step]]
    next_change_time = time.time() + step_images[0][1]

images_with_durations = []
default_duration = 0.1  
specific_durations = {
    11: 0.05,
    12: 0.02,
    13: 0.03,
    36: 0.12,
    37: 0.12,
    38: 0.12,
    39: 0.12,
    40: 0.12,
    60: 1,
    68: 1,
}

for x in range(68):
    image_path = os.path.join("images", f"image ({x}).png")
    if os.path.exists(image_path):
        duration = specific_durations.get(x, default_duration)
        images_with_durations.append((pygame.image.load(image_path), duration))

animation_steps = [11, 10, 6, 8, 11, 23]

def load_words_from_file():
    words = {"Facile": [], "Moyen": [], "Difficile": []}
    with open("mots.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        current_difficulty = None
        for line in lines:
            line = line.strip()
            if line in words:
                current_difficulty = line
            elif current_difficulty and line:   
                words[current_difficulty].append(line)
    return words

difficulty_levels = load_words_from_file()
print(difficulty_levels) 

def select_difficulty():
    selected = False
    difficulty = ""
    while not selected:
        screen.fill((255, 255, 255))
        screen.blit(font.render("Choisissez une difficulté :", True, (0, 0, 0)), (250, 200))
        screen.blit(font.render("1. Facile", True, (0, 255, 0)), (250, 250))
        screen.blit(font.render("2. Moyen", True, (255, 165, 0)), (250, 300))
        screen.blit(font.render("3. Difficile", True, (255, 0, 0)), (250, 350))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "Facile"
                    selected = True
                elif event.key == pygame.K_2:
                    difficulty = "Moyen"
                    selected = True
                elif event.key == pygame.K_3:
                    difficulty = "Difficile"
                    selected = True
    return difficulty


def initialize_game(difficulty):
    global random_word, difficulty_levels, hidden_word, lives, input_letter, wrong_letters, current_step, animating, current_image_index
    random_word = random.choice(difficulty_levels[difficulty])
    hidden_word = "_ " * len(random_word)
    lives = 6
    input_letter = None
    wrong_letters = []
    current_step = -1
    animating = False
    current_image_index = 0

running = True
while running:
    difficulty = select_difficulty()
    initialize_game(difficulty)
    game_active = True

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_active = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    input_letter = event.unicode.lower() 

                    if input_letter.isalpha() and input_letter not in wrong_letters and input_letter not in hidden_word:
                        if input_letter in random_word:
                            hidden_word_list = hidden_word.split()
                            for i in range(len(random_word)):
                                if input_letter == random_word[i]:
                                    hidden_word_list[i] = input_letter
                            hidden_word = " ".join(hidden_word_list)
                        else:
                                if input_letter not in random_word:
                                    if lives > 0:
                                        lives -= 1
                                        wrong_letters.append(input_letter)
                                        current_step += 1
                                        start_animation(current_step)

        if not running:
            break

        if hidden_word.replace(" ", "") == random_word:
            game_active = False
        elif lives == 0 and not animating:
            current_step += 1
            start_animation(current_step)

        if animating and time.time() >= next_change_time:
            current_image_index += 1
            if current_image_index >= len(step_images):
                animating = False
                if lives == 0:
                    game_active = False
            else:
                next_change_time = time.time() + step_images[current_image_index][1]

        screen.fill((255, 255, 255))

        if animating and current_image_index < len(step_images):
            screen.blit(step_images[current_image_index][0], (0, 0))
        elif not animating and current_step >= 0:
            screen.blit(step_images[-1][0], (0, 0))
        else:
            screen.blit(images_with_durations[0][0], (0, 0))

        screen.blit(font.render(f"Lettres incorrectes : {', '.join(wrong_letters)}", True, (127.5, 0, 0)), (50, 450))
        screen.blit(font.render(f"Mot à deviner : {hidden_word}", True, (0, 0, 0)), (50, 500))

        pygame.display.update()

    if not running:
        break

    if lives > 0:
        screen.fill((255, 255, 255))
        screen.blit(font.render("Bravo ! Vous avez gagné !", True, (0, 255, 0)), (200, 200))
        screen.blit(font.render(f"Mot trouvé : {random_word}", True, (0, 0, 0)), (50, 400))
        pygame.display.update()
    else:
        screen.blit(font.render(f"Le mot était : {random_word}", True, (0, 0, 0)), (50, 550))
        pygame.display.update()
        
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    waiting = False
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    waiting = False