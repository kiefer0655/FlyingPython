import pygame_gui
import pygame
import sys

def main():
    pygame.init()
    
    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((800, 600))
    
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))
    
    manager = pygame_gui.UIManager((800, 600))
    
    drone_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 275), (300, 50)),
                                                 text='drone',
                                                 manager=manager)
    webcam_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 275), (300, 50)),
                                                 text='webcam',
                                                 manager=manager)
    
    clock = pygame.time.Clock()
    is_running = True
    
    pygame.init()
    
    choice = ""
    
    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == drone_button:
                     choice = "drone"
                     is_running = False
                if event.ui_element == webcam_button:
                     choice = "webcam"
                     is_running = False
                     
    
            manager.process_events(event)
    
        manager.update(time_delta)
    
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
    
        pygame.display.update()
    
    pygame.quit()
    
    return choice