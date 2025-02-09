import pygame
import sys

# Initialize pygame
pygame.init()

# Load the map image
map_image = pygame.image.load("map_3000.jpg")

# Set screen dimensions based on image size
SCREEN_WIDTH, SCREEN_HEIGHT = map_image.get_size()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fantasy Map Adventure")

# Define locations with clickable areas (x, y, width, height)
locations = {
    "Octavia": (200, 200, 100, 100),
    "Diomira": (300, 400, 100, 100),
    "Adelma": (600, 100, 100, 150),
    "Zemrude": (500, 300, 100, 100),
    "Tamara": (700, 600, 90, 90),
    "river Alahorn": (300, 100, 110, 110),
    "Zoe archepelagos": (50, 50, 10, 10)
}

# Define event messages for locations
events = {
    "Octavia": "keep going!",
    "Diomira": "keep going!!",
    "Adelma": "coddiwople around the place!!it's about the journey mostly",
    "Zemrude": "go!",
    "Tamara": "Ancient runes glow under the moonlight!",
    "river Alahorn": "You struggle against the icy winds!",
    "Zoe archepelagos": "You found a hidden treasure chest!"
}

# Function to check if a point is inside a rectangle
def is_inside(x, y, rect):
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh

# Game loop
running = True
while running:
    screen.blit(map_image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for location, rect in locations.items():
                if is_inside(mx, my, rect):
                    print(events[location])  # Display event message in console

    pygame.display.flip()

pygame.quit()
sys.exit()
