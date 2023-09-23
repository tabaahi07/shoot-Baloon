def Score_board (score) :
    if( score >= 0 ) :
        return 
    
    else :
        import pygame, sys
        pygame.init()
        pygame.font.init()
        mouse = pygame.mouse


        size = width,height = 1000,700
        screen = pygame.display.set_mode(size)
        end_img = pygame.image.load( r"C:\Users\akrat\OneDrive\Desktop\Python Programs\Program\Pygame\shoot Baloon\game_over_img.jpg " )
        end_width =  end_img.get_width()
        end_height = end_img.get_height()

        end_sound = pygame.mixer.Sound(r"C:\Users\akrat\OneDrive\Desktop\Python Programs\Program\Pygame\shoot Baloon\front_sound.mp3 ")
        end_sound.play( loops = -1 )

    pressed = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT : sys.exit()
            
            screen.blit(end_img , ( 0,0,end_width,end_height) )
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = my_font.render(f' YOUR SCORE is : {score} ', False, (0, 0, 0) )
            screen.blit(text_surface, (10 , height-100 , text_surface.get_width(), text_surface.get_height() ) )
            pygame.display.flip()  

                   
                    

