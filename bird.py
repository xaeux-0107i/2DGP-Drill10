from pico2d import get_time, load_image, load_font
from state_machine import *
import game_world
import game_framework
from random import randint

class Bird:
    def __init__(self):
        self.x, self.y = randint(50, 1550), 510
        self.face_dir = 1
        self.action = 2
        self.frame = randint(0, 4)
        self.image = load_image('bird_animation.png') #184 168
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Idle:
    @staticmethod
    def enter(bird, e):
        pass

    @staticmethod
    def exit(bird, e):
        pass

    @staticmethod
    def do(bird):
        #boy.frame = (boy.frame + 1) % 8
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        bird.x += bird.face_dir * RUN_SPEED_PPS * game_framework.frame_time
        if bird.x > 1550:
            bird.face_dir = -1
        elif bird.x < 50:
            bird.face_dir = 1

    @staticmethod
    def draw(bird):
        if bird.face_dir == 1:
            bird.image.clip_draw(int(bird.frame) * 184, bird.action * 168, 170, 168, bird.x, bird.y, 100, 100)
        elif bird.face_dir == -1:
            bird.image.clip_composite_draw(int(bird.frame) * 184, bird.action * 168, 170, 168, 0, 'h', bird.x, bird.y, 100, 100)



