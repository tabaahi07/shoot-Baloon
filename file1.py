def fun() :
    
    import pygame, sys
    pygame.init()
    pygame.font.init()
    mouse = pygame.mouse


    size = width,height = 1000,700
    screen = pygame.display.set_mode(size)
    front_img = pygame.image.load(r"C:\Users\akrat\OneDrive\Desktop\Python Programs\Program\Pygame\shoot Baloon\shooting_image.png")
    front_width = front_img.get_width()
    front_height = front_img.get_height()

    front_sound = pygame.mixer.Sound(r"C:\Users\akrat\OneDrive\Desktop\Python Programs\Program\Pygame\shoot Baloon\front_sound.mp3 ")
    front_sound.play( loops = -1 )

    pressed = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT : sys.exit()
            
            screen.blit(front_img , ( 0,0,front_width,front_height) )
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = my_font.render('START', False, (0, 0, 0))
            screen.blit(text_surface, (100 , height-200 , text_surface.get_width(), text_surface.get_height() ) )
            pygame.display.flip()

            if (mouse.get_pressed()[0] and not pressed ):
                (a,b) = mouse.get_pos()
                print(a,b)
                print(text_surface.get_width())
                print(text_surface.get_height())
                if( ( a>100 and a<( 100+text_surface.get_width() ) ) and ( b>(height-200) and b<( height-200 + text_surface.get_height() ) )) : 
                    front_sound.stop()
                    return
                   
                    
            
            # if (pressed and not mouse.get_pressed()[0]):
            #  pressed = False






