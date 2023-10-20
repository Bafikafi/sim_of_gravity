import pygame


class Ball():
    # do not touch this bool, otherwise the simulation breaks
    is_under = False
    dsx = 0
    dsy = 0
    def __init__(self, poss, screen, dt, floory, radius) -> None:
        self.start_poss = [poss[0], poss[1]]
        self.poss = poss
        self.started = False
        self.screen = screen
        self.dt = dt
        self.floory = floory
        self.radius = radius
        

    # updates the delta time value for this frame
    def update(self, dt, radius):
        self.dt = dt
        self.radius = radius

    # draws the circle, representing the ball with radius radius
    def draw(self):
        pygame.draw.circle(self.screen, "white", self.poss, self.radius)

    # moves the ball according to the velocity it has, 
    # as well as changes the direction of velocity when under the line
    def move(self, velocity):
        if self.started:

            # if self.poss[1] > self.floory and not self.is_under:
            #     self.dsx = self.floory - self.poss[1] 
            #     velocity.y = -abs(velocity.y)

            #     self.is_under = True
            #     return
            
            if self.poss[0] > (self.screen.get_width() - 300):
                self.poss[0] = 120
            
            self.poss[0] += velocity.x * self.dt
            self.poss[1] += velocity.y * self.dt
            # self.is_under = False


    def start_movement(self):
        self.started = True

    def restart(self):
        self.started = False
        self.poss[0], self.poss[1] = self.start_poss[0], self.start_poss[1]
        print(*self.start_poss, *self.poss)

# lines on the side
class Scale():
    
    def __init__(self, screen, scale, y_0, x, has_scale) -> None:
        self.scale = scale
        self.screen = screen
        self.y_0 = y_0
        self.x = x
        self.cm = 37.8 * scale
        self.img = None
        self.font = pygame.font.SysFont(None, 40)
        self.img = self.font.render('vyska [m]', True, 'White')
        self.has_scale = has_scale

    # draws the scale, as well as the line itself
    def draw(self):
        y = self.y_0
        dx = -20
        if self.has_scale:
            self.screen.blit(self.img, (self.x + 20, 50))
            dx = 0
        pygame.draw.rect(self.screen, 'White', [self.x, 10, 5, 700])
        for i in range(int(600 // self.cm)):
            pygame.draw.rect(self.screen, 'white', [self.x + dx, y, 20, 5])
            y -= self.cm * 100 / 5

    # can change the scale here
    def update_scale(self, scale):
        self.scale = scale
        self.cm = 37.8 * scale

# the line on the bottom
class bottom_line():
    startx = 120
    endx = 1160
    def __init__(self, screen,y_0) -> None:
        self.y_0 = y_0
        self.screen = screen
    
    def draw(self):
        x = self.startx
        for i in range (8):
            pygame.draw.rect(self.screen, 'White', [x, self.y_0, (self.endx - self.startx) // 20, 5])
            x+= (self.endx - self.startx) // 10

# button to press       
class button:
    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')

    def __init__(self, screen, x, y, width, height, text) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.font = pygame.font.SysFont(None, 30)
        self.img = self.font.render(text, True, 'black')

    
    def draw(self, is_mouse_on):
        if is_mouse_on:
            color = self.COLOR_ACTIVE
        else:
            color = self.COLOR_INACTIVE
        pygame.draw.rect(self.screen, color, [self.x, self.y, self.width, self.height])
        self.screen.blit(self.img, (self.x + self.width / 10, self.y + self.height / 4))

    # detects if the mouse or x, y coordinate is on the button
    def is_in(self, x, y) -> bool:
        return self.x+self.width > x > self.x and self.y + self.height > y > self.y
    
    # changes text of the button
    def change_text(self, text):
        self.img = self.font.render(text, True, 'black')


class InputBox:

    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')
 

    def __init__(self, x, y, w, h, FONT, text='', start_val=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.FONT = FONT
        self.txt_surface = self.FONT.render(text, True, self.COLOR_INACTIVE)
        self.active = True
        self.img_up = self.FONT.render(start_val, True, 'White')
        self.val = float(text)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.val = float(self.text)
                    # self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.img_up, (self.rect.x, self.rect.y - self.rect.height / 2))

    def get_value(self):
        return self.val




class Checkbox:
    def __init__(self, surface, x, y, color=(230, 230, 230), caption="", outline_color=(0, 0, 0),
                 check_color=(0, 0, 0), font_size=22, font_color=(0, 0, 0), text_offset=(28, 1)):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.caption = caption
        self.oc = outline_color
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        # checkbox object
        self.checkbox_obj = pygame.Rect(self.x, self.y, 25, 25)
        self.width = self.checkbox_obj.width
        self.checkbox_outline = self.checkbox_obj.copy()
        # variables to test the different states of the checkbox
        self.checked = False
        self.active = False
        self.unchecked = True
        self.click = False

    def _draw_button_text(self):
        self.font = pygame.font.Font(None, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x +60 / 2 - w / 2 + self.to[0], self.y + 25 / 2 - h / 2 + self.to[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_checkbox(self):
        if self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
            # pygame.draw.circle(self.surface, self.cc, (self.x + self.checkbox_obj.width/2, self.y + self.checkbox_obj.width/2), self.checkbox_obj.width/2 - 1)
            pygame.draw.line(self.surface, (0, 0, 0), (self.x, self.y), (self.x + self.width - 1, self.y + self.width - 1), 5)
            pygame.draw.line(self.surface, (0, 0, 0), (self.x - 1 + self.width, self.y), (self.x, self.y + self.width - 1), 5)
            # pygame.draw.line()

        elif self.unchecked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = event_object.pos
        # self.x, self.y, 12, 12
        px, py, w, h = self.checkbox_obj  # getting check box dimensions
        if px < x < px + w and py < y < py + w:
            self.active = True
        else:
            self.active = False
    def _mouse_up(self):
            if self.active and self.click:
                    self.checked = not self.checked


    def update_checkbox(self, event_object):
        if event_object.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            # self._mouse_down()
        if event_object.type == pygame.MOUSEBUTTONUP:
            self._mouse_up()
        if event_object.type == pygame.MOUSEMOTION:
            self._update(event_object)

    def is_checked(self):
        if self.checked is True:
            return True
        else:
            return False

    def is_unchecked(self):
        if self.checked is False:
            return True
        else:
            return False

