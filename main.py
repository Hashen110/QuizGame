from random import randrange
import pygame

pygame.init()
screen = pygame.display.set_mode([1300, 800])
running, new_question, is_correct, answering, game_over = True, True, True, False, False
operators, question = ['+', '-'], []
answer = ''
question_number, lives = 0, 5


def render_text(text, y, color=(randrange(256), randrange(256), randrange(256)), size=25, x=None):
    font = pygame.font.SysFont("monospace", size)
    text_render = font.render(str(text), True, color)
    if x is None:
        text_rect = text_render.get_rect(center=(1300 / 2, y))
        return screen.blit(text_render, text_rect)
    return screen.blit(text_render, (x, y))


while running:
    screen.fill((0, 0, 0))
    render_text('QUIZ GAME', 100, size=100)
    if game_over:
        render_text('Game Over', 300, size=75)
        render_text(f'Score {question_number}', 500, size=50)
        render_text('Press enter for new game', 700)
    else:
        if new_question and not answering:
            if not is_correct:
                lives -= 1
            if lives == 0:
                game_over = True
            question = [randrange(11), operators[randrange(len(operators))], randrange(11)]
            answering = True
            new_question = False
            answer = ''
            question_number += 1
        render_text(question[0], 300, x=200, size=100)
        render_text(question[1], 300, x=400, size=100)
        render_text(question[2], 300, x=600, size=100)
        render_text('=', 300, x=800, size=100)
        render_text(answer, 300, x=1000, size=100)
        render_text(f'Question: {question_number}', 775, x=0)
        render_text(f'Lives: {lives}', 775, x=1175)
    if not answering and not new_question and answer:
        if question[1] == '+':
            if int(answer) == question[0] + question[2]:
                render_text('Correct', 500, size=75, color=(0, 255, 0))
                is_correct = True
            else:
                render_text(f'Wrong! Correct answer is: {question[0] + question[2]}', 500, size=50, color=(255, 0, 0))
                is_correct = False
        elif question[1] == '-':
            if int(answer) == question[0] - question[2]:
                render_text('Correct', 500, size=75, color=(0, 255, 0))
                is_correct = True
            else:
                render_text(f'Wrong! Correct answer is: {question[0] - question[2]}', 500, size=50, color=(255, 0, 0))
                is_correct = False
        render_text('Press enter for next question', 700)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if not game_over and answering and (event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS):
                answer += '-'
            elif not game_over and answering and (event.key == pygame.K_0 or event.key == pygame.K_KP0):
                answer += '0'
            elif not game_over and answering and (event.key == pygame.K_1 or event.key == pygame.K_KP1):
                answer += '1'
            elif not game_over and answering and (event.key == pygame.K_2 or event.key == pygame.K_KP2):
                answer += '2'
            elif not game_over and answering and (event.key == pygame.K_3 or event.key == pygame.K_KP3):
                answer += '3'
            elif not game_over and answering and (event.key == pygame.K_4 or event.key == pygame.K_KP4):
                answer += '4'
            elif not game_over and answering and (event.key == pygame.K_5 or event.key == pygame.K_KP5):
                answer += '5'
            elif not game_over and answering and (event.key == pygame.K_6 or event.key == pygame.K_KP6):
                answer += '6'
            elif not game_over and answering and (event.key == pygame.K_7 or event.key == pygame.K_KP7):
                answer += '7'
            elif not game_over and answering and (event.key == pygame.K_8 or event.key == pygame.K_KP8):
                answer += '8'
            elif not game_over and answering and (event.key == pygame.K_9 or event.key == pygame.K_KP9):
                answer += '9'
            elif not game_over and answering and event.key == pygame.K_BACKSPACE:
                answer = ''
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if answer:
                    if not answering:
                        new_question = True
                    answering = False
                if game_over:
                    game_over = False
                    question_number, lives = 0, 5
    pygame.display.update()
pygame.quit()
