import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE, BLACK, RED, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 0, 255)
colors = [BLACK, RED, BLUE]
color_index = 0
current_color = colors[color_index]

mode = "pen"
screen.fill(WHITE)
pygame.display.flip()

drawing, start_pos = False, None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: mode = "rect"
            if event.key == pygame.K_c: mode = "circle"
            if event.key == pygame.K_e: mode = "eraser"
            if event.key == pygame.K_p: mode = "pen"
            if event.key == pygame.K_SPACE:
                color_index = (color_index + 1) % len(colors)
                current_color = colors[color_index]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing, start_pos = True, event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if mode == "rect":
                pygame.draw.rect(screen, current_color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif mode == "circle":
                pygame.draw.circle(screen, current_color, start_pos, abs(end_pos[0] - start_pos[0]) // 2, 2)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pen":
                pygame.draw.line(screen, current_color, start_pos, event.pos, 2)
                start_pos = event.pos
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, 10)
    
    pygame.display.flip()

pygame.quit()