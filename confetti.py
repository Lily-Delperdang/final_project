import pygame
import random

pygame.init()

# Screen dimensions
width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Confetti Animation")

# Confetti colors
confetti_colors = ["sky blue", "pink", "gold", "lavender", (150, 110, 240)]

# Confetti list
confetti_list = []

# Function to create confetti
def create_confetti():
    x = random.randint(0, width)
    y = random.randint(-height, 0)  # Start above screen
    speed_y = random.randint(2, 5)
    size = random.randint(3, 7)
    color = random.choice(confetti_colors)
    return [x, y, speed_y, size, color]

# Create initial confetti
for _ in range(100):
    confetti_list.append(create_confetti())

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Clear the screen
    screen.fill((0, 0, 0))

    # Update and draw confetti
    for confetti in confetti_list:
        x, y, speed_y, size, color = confetti
        y += speed_y

        # Reset if it goes off screen
        if y > height:
            y = random.randint(-50, -10)
            x = random.randint(0, width)

        # Save updated position
        confetti[0] = x
        confetti[1] = y

        pygame.draw.circle(screen, color, (x, y), size)

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
