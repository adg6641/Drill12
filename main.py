from pico2d import *
from boy import Boy
from grass import Grass

import game_world

running = True

def handle_events():
    global running, boy

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT or \
           (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False
        else:
            boy.handle_event(event)

def reset_world():
    global boy, grasses

    game_world.clear()

    grass1 = Grass(400, 30)  
    grass2 = Grass(400, 50)  

    game_world.add_object(grass1, 0)
    game_world.add_object(grass2, 2)

    boy = Boy()
    game_world.add_object(boy, 1)  


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True

open_canvas()
reset_world()

# 게임 루프 실행
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

# 최종화면 코드
close_canvas()
