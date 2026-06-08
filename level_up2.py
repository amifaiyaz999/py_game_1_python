import pygame
import random

# 1) & 2) Initialize Pygame
pygame.init()

# 3) Custom event IDs
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# 4) Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

# 5) Create a Sprite class that inherits from pygame.sprite.Sprite
class Sprite(pygame.sprite.Sprite):

    # 6) Define the constructor
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    # 7) Define an update(self) method to move the sprite and detect boundary hits
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        
        # Check left/right edges
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
            
        # Check top/bottom edges
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        # Post events if a boundary was hit
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    # 8) Define a method change_color(self) in Sprite
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))


# 9) Define a function change_background_color()
def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])


# 10) Create a sprite group
all_sprites_list = pygame.sprite.Group()

# 11) Create one sprite object
sp1 = Sprite(WHITE, 20, 30)

# 12) Set the sprite’s starting position randomly
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

# 13) Add the sprite to the group
all_sprites_list.add(sp1)

# 14) Create the game window (screen) of size 500x400 and set title
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Color Changing Bouncing Box")

# 15) Set the initial background color and fill the screen once
bg_color = BLUE
screen.fill(bg_color)

# 16) Create loop control variable and clock object
exit_game = False  # Avoided using 'exit' as a variable name since it's a built-in function
clock = pygame.time.Clock()

# 17) Start the main game loop
while not exit_game:

    # 18) Inside the loop, handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    # 19) Update all sprites
    all_sprites_list.update()

    # 20) Redraw the screen each frame
    screen.fill(bg_color)
    all_sprites_list.draw(screen)

    # 21) Update the display
    pygame.display.flip()

    # 22) Limit the frame rate
    clock.tick(240)

# 23) Close pygame
pygame.quit()