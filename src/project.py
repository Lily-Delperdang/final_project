from pygame import Rect

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(90, 338)
answer_box2.move_ip(695, 338)
answer_box3.move_ip(90, 528)
answer_box4.move_ip(695, 528)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    screen.fill((224, 255, 255))
    screen.draw.filled_rect(main_box, "skyblue")
    screen.draw.filled_rect(timer_box, "plum")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "gold")


def confetti_animation():
    pass

def on_mouse_down(pos):
    pass

def game_over():
    pass

def correct_answer():
    pass

def update_time_left():
    pass
