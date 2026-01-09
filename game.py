import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Catch the Apple Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

basket = pygame.image.load(r"C:\Users\VEMBU DHARSINI\Desktop\healthcare\basket.png")
apple = pygame.image.load(r"C:\Users\VEMBU DHARSINI\Desktop\healthcare\apple.png")

basket = pygame.transform.scale(basket, (100, 60))
apple = pygame.transform.scale(apple, (40, 40))

catch_sound = pygame.mixer.Sound(r"C:\Users\VEMBU DHARSINI\Desktop\healthcare\Notification Sound.mp3")

basket_x = 250
basket_y = 330
apple_x = random.randint(50, 550)
apple_y = 0

score = 0
missed = 0
apple_speed = 7
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -= 6
    if keys[pygame.K_RIGHT]:
        basket_x += 6

    apple_y += apple_speed

    basket_rect = pygame.Rect(basket_x, basket_y, 100, 60)
    apple_rect = pygame.Rect(apple_x, apple_y, 40, 40)

    if basket_rect.colliderect(apple_rect):
        score += 1
        catch_sound.play()
        apple_x = random.randint(50, 550)
        apple_y = 0
        if apple_speed < 15:
            apple_speed += 0.3

    if apple_y > 400:
        missed += 1
        apple_x = random.randint(50, 550)
        apple_y = 0

    if missed >= 5:
        screen.fill(WHITE)
        game_over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
        screen.blit(game_over_text, (150, 180))
        pygame.display.update()
        pygame.time.wait(3000)
        break

    screen.blit(apple, (apple_x, apple_y))
    screen.blit(basket, (basket_x, basket_y))

    score_text = font.render(f"Score: {score}  Missed: {missed}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
