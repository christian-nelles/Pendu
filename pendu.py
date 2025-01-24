import pygame
import random
import os
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("None", 30)
score_display = 0

def initialize_game():

    global random_word, hidden_word, lives, input_letter, wrong_letters, current_step, animating, current_image_index, score_display
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mots.txt'), 'r') as file:
        allText = file.read() 
        random_word = random.choice(list(map(str, allText.split())))
    hidden_word = "_ " * len(random_word)
    lives = 6 
    input_letter = None
    wrong_letters = []
    current_step = -1
    animating = False
    current_image_index = 0


def start_animation(current_step):
    global animating, step_start_index, step_images, next_change_time, current_image_index
    animating = True
    current_image_index = 0
    step_start_index = sum(animation_steps[:current_step])
    step_images = images_with_durations[step_start_index:step_start_index + animation_steps[current_step]]
    next_change_time = time.time() + step_images[0][1]

def score(score_display):
    score_display += 1
    return score_display

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

running = True
while running:
    initialize_game()
    game_active = True

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_active = False

            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and not animating: 
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
            score_display = score(score_display)
            hidden_word = ""
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
        # screen.blit(score_display + 1)
        # score_display += 1

        screen.blit(font.render(f"score : {score_display}", True, (0, 255, 0)), (300, 200))

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


            # score_display = score(score_display)