import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800,500
display_surfae = pygame.display.set_moe((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('adding image and backgorund')
background_image = pygame.transform.scale(pygame.image.load('#image').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
my_image = pygame.transform.scale(pygame.image.load('#back_img').convert_alpha(),(400,400))
my_react = my_image.get_react(center=(SCREEN_WIDTH// 2,SCREEN_HEIGHT,SCREEN_HEIGHT//2-30))
text = pygame.font.Font(None,36).render('welcome to shornochuri',True,pygame.Color('yellow'))
text_react = text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+110))
def game_loop():
    Clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surfae.blit(background_image,(0,0))
        display_surfae.blit(my_image,my_react)
        display_surfae.blit(text,text_react)


        pygame.display.flip()
        Clock.tick(30)

        pygame.quit()

if __name__ == '__main__':
    game_loop()











