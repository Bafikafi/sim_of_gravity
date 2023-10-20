import pygame
import objects
import logic

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# scale of the height


# radius of the ball

ball_going = False

handled = False

mouse_clicked = False

# bottom line
floor = objects.bottom_line(screen, 600)

# buttons

button_start = objects.button(screen, 0, 0, 120, 60, 'START')
mouse_on_button_start = False

button_exit = objects.button(screen, 0, 660, 120, 60, 'EXIT')

# parameters, all the values we can use in our code
v_x = 0
v_y = 0
scaleF = logic.scale_change(1)
radius = 0.1
mass = 1
gravity = 9.81
height = 1
f =  pygame.font.Font(None, 32)
v_x_box = objects.InputBox(screen.get_width() - 250, screen.get_height() * 2 / 13, 200, 50, f, '0', 'v_x_0')
v_y_box = objects.InputBox(screen.get_width() - 250, screen.get_height() * 4 / 13, 200, 50, f, '0', 'v_y_0')
scale_box = objects.InputBox(screen.get_width() - 250, screen.get_height() * 6 / 13, 200, 50, f, '1', 'výška')
gravity_box = objects.InputBox(screen.get_width() - 250, screen.get_height() * 10 / 13, 200, 50, f, '9.81', 'gravitačné zrýchlenie')
buttons = [v_x_box, v_y_box, scale_box, gravity_box]

# velocity of the ball
velocity = pygame.Vector2(v_x, v_y)

# ball itself
ball = objects.Ball([screen.get_width() / 4, 120], screen, dt, 600, radius * 37.8)

# side lines
scale_left = objects.Scale(screen, scaleF, 600, 120, True)
scale_right = objects.Scale(screen, scaleF, 600, screen.get_width() - 300, False)

while running:

    poss_mouse = pygame.mouse.get_pos()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
        
        for button in buttons:
            button.handle_event(event)
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # drawing of all the objects
    ball.draw()

    scale_left.draw()

    scale_right.draw()

    v_x_box.draw(screen)

    for button in buttons:
        button.draw(screen)

    v_x_box.update()
    # getting the possition of the mouse
    

    button_start.draw(mouse_on_button_start)
    button_exit.draw(button_exit.is_in(poss_mouse[0], poss_mouse[1]))

    floor.draw()

    # updating the delta time value with current frame
    ball.update(dt, radius * 37.8 * 10)

    if not ball_going:
        
        velocity.x = v_x_box.get_value()
        velocity.y = v_y_box.get_value()
        
        gravity = gravity_box.get_value()
        scaleF = logic.scale_change(scale_box.get_value())
        height = scale_box.get_value()
        scale_left.update_scale(scaleF)
        scale_right.update_scale(scaleF)

    # calculates the velocity, based on the gravity 
    # and can be altered in the non vacuum area
    if ball_going:
        velocity.x = logic.calculate_velocity(velocity.x, dt, 0)
        velocity.y = logic.calculate_velocity(velocity.y, dt, gravity)
        

    ball.move(velocity)
    
    mouse_on_button_start = button_start.is_in(poss_mouse[0], poss_mouse[1])

    # clicking mouse and checking if mouse clicked on a button
    if mouse_clicked:
        # start button
        if  mouse_on_button_start and not ball_going and not handled:
            handled = True
            ball_going = True
            ball.start_movement()
            button_start.change_text('RESTART')
            velocity.x = v_x_box.get_value()
            velocity.y = -v_y_box.get_value()
        
        # restart button
        elif mouse_on_button_start and ball_going and not handled:
            handled = True
            ball_going = False
            ball.restart()
            button_start.change_text('START')
            velocity.x, velocity.y = 0, 0

        # exit button
        if button_exit.is_in(poss_mouse[0], poss_mouse[1]) and not handled:
            running = False
        
        mouse_clicked = False

    # handeling, so if you click the button it only clicks once        
    elif (not mouse_clicked or not mouse_on_button_start) and handled:
        handled = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick() * 37.8/ 1000 * scaleF
    

pygame.quit()