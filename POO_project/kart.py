import pygame
from math import sin, cos
from track import Track

MAX_ANGLE_VELOCITY = 0.05
MAX_ACCELERATION = 0.25


class Kart():  # Vous pouvez ajouter des classes parentes
    """
    Classe implementant l'affichage et la physique du kart dans le jeu
    """

    def __init__(self, controller):
        self.has_finished = False
        self.controller = controller
        self.controller.kart = self

        self.is_moving_forward = False
        self.is_moving_backward = False
        self.is_turning_left = False
        self.is_turning_right = False

        self.a_c = 0  # Acceleration linear constant
        self.alpha_c = 0  # Acceleration angulaire constant
        self.angle = 0
        self.a = 0
        self.v = 0
        self.pos_x = 0
        self.pos_y = 0
        self.position = [self.pos_x,self.pos_y]

        self.next_checkpoint_id = 0
        self.checkpoint_x = 0
        self.checkpoint_y = 0
        self.checkpoint_angle = 0
        pass

    def reset(self, initial_position, initial_angle):
        self.angle = initial_angle
        self.pos_x = initial_position[0]
        self.pos_y = initial_position[1]
        self.checkpoint_x = initial_position[0]
        self.checkpoint_y = initial_position[1]
        self.checkpoint_angle = initial_angle

    def forward(self):
        self.is_moving_forward = True
        self.a_c = MAX_ACCELERATION

    def backward(self):
        self.is_moving_backward = True
        self.a_c = -MAX_ACCELERATION

    def turn_left(self):
        self.is_turning_left = True
        self.alpha_c = -MAX_ANGLE_VELOCITY

    def turn_right(self):
        self.is_turning_right = True
        self.alpha_c = MAX_ANGLE_VELOCITY

    def update_position(self, string, screen):
        width, height = screen.get_size()

        if self.pos_x > width or self.pos_x < 0 or self.pos_y > height or self.pos_y < 0:
            area_type = "L"
        else:
            # Calculer col et ligne de kart
            kart_x = int(self.pos_x // 50)
            kart_y = int(self.pos_y // 50)

            track_lines = string.split('\n')
            area_type = track_lines[kart_y][kart_x]

        # Verifier les situations des commandes
        if self.is_moving_forward == self.is_moving_backward:
            self.a_c = 0
        if self.is_turning_left == self.is_turning_right:
            self.alpha_c = 0

        track_element_dict = Track.char_to_track_element
        if area_type in ["C", "D", "E", "F"]:
            if area_type == "F":
                if self.next_checkpoint_id == track_element_dict["F"]['params'][0]:
                    self.has_finished = True
                    print(f"Player {self.controller.kart} finished the game.")
            else:
                if self.next_checkpoint_id  == track_element_dict[area_type]['params'][0]:
                    self.next_checkpoint_id += 1
                self.checkpoint_x = self.pos_x
                self.checkpoint_y = self.pos_y
                self.checkpoint_angle = self.angle
            f = 0.02
            self.angle = self.angle + self.alpha_c
            self.a = self.a_c - f * self.v * cos(self.alpha_c)
            self.v = self.a + self.v * cos(self.alpha_c)
            self.pos_x = self.pos_x + self.v * cos(self.angle)
            self.pos_y = self.pos_y + self.v * sin(self.angle)
        elif area_type == "L":
            self.pos_x = self.checkpoint_x
            self.pos_y = self.checkpoint_y
            self.angle = self.checkpoint_angle
            self.v = 0
        elif area_type == "R":
            f = 0.02
            self.angle = self.angle + self.alpha_c
            self.a = self.a_c - f * self.v * cos(self.alpha_c)
            self.v = self.a + self.v * cos(self.alpha_c)
            self.pos_x = self.pos_x + self.v * cos(self.angle)
            self.pos_y = self.pos_y + self.v * sin(self.angle)

        elif area_type == "G":
            f = 0.2
            self.angle = self.angle + self.alpha_c
            self.a = self.a_c - f * self.v * cos(self.alpha_c)
            self.v = self.a + self.v * cos(self.alpha_c)
            self.pos_x = self.pos_x + self.v * cos(self.angle)
            self.pos_y = self.pos_y + self.v * sin(self.angle)

        elif area_type == "B":
            self.angle = self.angle + self.alpha_c
            self.v = 25
            self.pos_x = self.pos_x + self.v * cos(self.angle)
            self.pos_y = self.pos_y + self.v * sin(self.angle)

        self.is_moving_forward = False
        self.is_moving_backward = False
        self.is_turning_left = False
        self.is_turning_right = False

    def draw(self, screen):
        # A modifier et completer
        kart_position = [self.pos_x, self.pos_y]
        kart_radius = 20
        kart_head_radius = 10
        kart_head_position = [self.pos_x + (kart_radius - kart_head_radius) * cos(self.angle),
                              self.pos_y + (kart_radius - kart_head_radius) * sin(self.angle)]
        # Draw a circle
        pygame.draw.circle(screen, (255, 255, 255), kart_position, kart_radius)
        pygame.draw.circle(screen, (0, 0, 255), kart_head_position, kart_head_radius)

    # Completer avec d'autres methodes si besoin (ce sera probablement le cas)
