import pygame
import random

pygame.init()


WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

bg_img = pygame.image.load("background-1.png")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
car_img = pygame.image.load("12.png")
coin_img = pygame.image.load("Coin2.png")
obstacle_img = pygame.image.load("spr_boulder_0.png")

car_img = pygame.transform.scale(car_img, (50, 100))
coin_img = pygame.transform.scale(coin_img, (30, 30))
obstacle_img = pygame.transform.scale(obstacle_img, (50, 50))

car = pygame.Rect(225, 500, 50, 100)
coin = pygame.Rect(random.randint(50, WIDTH - 50), -50, 30, 30)
obstacle = pygame.Rect(random.randint(50, WIDTH - 50), -150, 50, 50)

car_speed = 5
object_speed = 5
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.blit(bg_img, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.x > 0:
        car.x -= car_speed
    if keys[pygame.K_RIGHT] and car.x < WIDTH - car.width:
        car.x += car_speed
    
    coin.y += object_speed
    obstacle.y += object_speed
    
    if car.colliderect(coin):
        score += 1
        coin.y = -50
        coin.x = random.randint(50, WIDTH - 50)
    
    if car.colliderect(obstacle):
        running = False
    
    if coin.y > HEIGHT:
        coin.y = -50
        coin.x = random.randint(50, WIDTH - 50)
    if obstacle.y > HEIGHT:
        obstacle.y = -150
        obstacle.x = random.randint(50, WIDTH - 50)
    
    screen.blit(car_img, (car.x, car.y))
    screen.blit(coin_img, (coin.x, coin.y))
    screen.blit(obstacle_img, (obstacle.x, obstacle.y))
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (350, 20))
    
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
