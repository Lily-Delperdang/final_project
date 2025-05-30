from pygame import Rect
import random
import pgzrun
from pgzero import clock

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

'''
# Resized to be 20% smaller

WIDTH = 1280/1.2 #1536
HEIGHT = 720/1.2 #864

main_box = Rect(0, 0, 820/1.2, 240/1.2)
timer_box = Rect(0, 0, 240/1.2, 240/1.2)
answer_box1 = Rect(0, 0, 495/1.2, 165/1.2) #Rect(0, 0, 594, 198)
answer_box2 = Rect(0, 0, 495/1.2, 165/1.2)
answer_box3 = Rect(0, 0, 495/1.2, 165/1.2)
answer_box4 = Rect(0, 0, 495/1.2, 165/1.2)

main_box.move_ip(50, 40)
timer_box.move_ip(990/1.2, 40)
answer_box1.move_ip(90/1.2, 338/1.2)
answer_box2.move_ip(695/1.2, 338/1.2)
answer_box3.move_ip(90/1.2, 528/1.2)
answer_box4.move_ip(695/1.2, 528/1.2)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
'''

score = 0
time_left = 10
game_has_ended = False
game_is_won = False
end_message = ""

confetti_colors = ["sky blue", "pink", "gold", "lavender", (150, 110, 240)]
confetti_list = []

q1 = ["The following people helped create the 12 principles of animation EXCEPT:",
       "Frank Thomas", "Milt Kahl", "Brian Froud", "Ollie Johnston", 3]
q2 = ["Who founded Pixar?", 
      "Steve Jobs", "John Lasseter", "Edwin Catmull", "All of them", 4]
q3 = ["Who directed 'A Trip to the Moon', the 1902 science-fiction film?", 
      "D.W. Griffith", "Georges Melies", "Charlie Chaplin", "The Luiere Brothers", 2]
q4 = ["Which is NOT a type of animation?", 
      "Anime", "Stop-motion", "3D animation", "Hand drawn animation", 1]
q5 = ["The following are all principles of design EXCEPT:", 
      "Repetition", "Rule of thirds", "Contrast", "Hierarchy", 2]
q6 = ["What makes a good pose?", 
      "Line of action", "Clear silhouette", "Contrasting shapes", "All of these", 4]
q7 = ["Which software application is commonly used for creating Motion Graphics?", 
      "Adobe After Effects", "Unity", "Adobe Photoshop", "ZBrush", 1]
q8 = ["Which best describes graphic designer Saul Bass's style?", 
      "Simple, geometric, with eye-catching color", "Calm with light colors", "Minimalistic and colorless", "Realistic with very little typhography", 1]
q9 = ["Which is the first animated feature film?",
       "Steamboat Willie (1928)", "Snow White (1937)", "Sleeping Beauty (1959)", "Gertie the Dinosaur (1914)", 2]
q10 = ["What was the first feature length movie to integrate 3D CGI?", 
       "Tron (1982)", "Westworld (1973)", "Futureworld (1976)", "Jurassic Park (1993)", 3]
q11 = ["Who created Sketchpad in 1962, the first computer program to produce 3D objects?", 
       "Bill Reeves", "Ivan Sutherland", "Alvey Ray Smith", "Gunpei Yokoi", 2]
q12 = ["When was Adobe founded?", 
       "1982", "2001", "1979", "1988", 1]
q13 = ["Which was the first movie made by computer generated imaging?", 
       "Ice Age (2002)", "Goat Story (2008)", "Toy Story (1995)", "Garfield Gets Real (2007)", 3]
q14 = ["Who created the first animated film, 'Humorous Phases of Funny Faces'?", 
       "Winsor McCay", "James Stuart Blackton", "Emile Cohl", "Walt Disney", 2]
q15 = ["Who created Computer Animated Hand (1972), the first animation of a 3D mesh?", 
       "David Evans & Ivan Sutherland", "John Whitney Jr.", "Gary Demos", "Ed Catmull & Fred Parke", 4]

question_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]
questions = question_list.copy()
random.shuffle(questions)
question = questions.pop()
box_colors = ["gold", "gold", "gold", "gold"]

def draw():
    screen.fill((224, 255, 255))

    if game_has_ended:
        end_box = Rect(0, 0, WIDTH * 0.8, HEIGHT * 0.5)
        end_box.center = (WIDTH // 2, HEIGHT // 2)
        screen.draw.filled_rect(end_box, "orchid")
        screen.draw.textbox(end_message, end_box, color="white", align="center")
        return 

    if game_is_won:
        end_box = Rect(0, 0, WIDTH * 0.8, HEIGHT * 0.5)
        end_box.center = (WIDTH // 2, HEIGHT // 2)
        screen.draw.filled_rect(end_box, (255, 180, 10))
        screen.draw.textbox(end_message, end_box, color="white", align="center")
        confetti_animation()
        return

    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "plum")
    
    for i, box in enumerate(answer_boxes):
        screen.draw.filled_rect(box, box_colors[i])

    screen.draw.textbox(str(time_left), timer_box, color=("dark slate blue"))
    screen.draw.textbox(question[0], main_box, color=("dark blue"), align="center")

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color =("medium slate blue"), align="center")
        index += 1

def confetti_animation():
    global confetti_list

    if not confetti_list:
        for _ in range(80):#change to 100 if fine
            x = random.randint(0, WIDTH)
            y = random.randint(-HEIGHT, 0)
            speed_y = random.randint(25, 35) #change back to (4, 8) if too fast
            size = random.randint(6, 9)
            color = random.choice(confetti_colors)
            confetti_list.append([x, y, speed_y, size, color])

    for confetti in confetti_list:
        confetti[1] += confetti[2] 

        if confetti[1] > HEIGHT:
            confetti[0] = random.randint(0, WIDTH)
            confetti[1] = random.randint(-50, -10)

        screen.draw.filled_circle((confetti[0], confetti[1]), confetti[3], confetti[4])


def on_mouse_down(pos):
    global box_colors
    index = 1
    for i, box in enumerate(answer_boxes):
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it right!")
                correct_answer()
            else:
                print("Wrong answer!")
                box_colors[i] = "pink"

        index +=1

def game_won():
    global game_is_won, game_has_ended, end_message, questions, time_left

    end_message = "You won! You got %s questions correct" % str(score)
    game_is_won = True
    game_has_ended = False

    questions = question_list.copy()
    random.shuffle(questions)

def game_over():
    global game_is_won, game_has_ended, end_message, questions, time_left

    end_message = "Game over. You got %s questions correct" % str(score)
    game_has_ended = True
    game_is_won = False
    time_left = 0

    questions = question_list.copy()
    random.shuffle(questions)

def correct_answer():
    global question, score, time_left, box_colors

    score += 1
    box_colors = ["gold", "gold", "gold", "gold"]

    if questions:
        question = questions.pop(0)
        time_left = 15
    else:
        print("End of questions")
        game_won()

def update_time_left():
    global time_left

    if game_has_ended or game_is_won:
        return

    if time_left:
        time_left -= 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)
pgzrun.go()

