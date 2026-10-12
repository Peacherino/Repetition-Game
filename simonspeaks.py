from fltk import Fl, Fl_Window, Fl_Button, FL_RED, Fl_add_timeout, Fl_repeat_timeout, FL_BACKGROUND_COLOR, FL_BLUE, FL_YELLOW, FL_GREEN, fl_message
import random
import subprocess
import os


def play_sound(filename):
    sound_path = os.path.join(os.path.dirname(__file__), "simonmusic", filename)
    print(f"playing {filename}")
    subprocess.call(["mplayer", sound_path])

def error_sound():
    play_sound("error (1).mp3")

class GameButton(Fl_Button):
    def __init__(self, x, y, w, h, title, on_color, off_color, name):
        super().__init__(x, y, w, h, title)
        self.on_color = on_color
        self.off_color = off_color
        self.color(on_color, off_color)
        self.name = name
        self.callback(self.user_select)

    def flash_button(self):
        self.color(7)
        self.redraw()
        Fl.wait(0)
        Fl.add_timeout(0.8, self.clear_button)
        self.play_sound()

    def clear_button(self):
        self.color(self.on_color, self.off_color)
        self.redraw()

    def play_sound(self):
        play_sound(f"{self.name} (1).mp3")

    def user_select(self, widget):
        if app.mode != 'user_input':
            print('got input out of turn')
            return
        print('user selected', self.name)
        self.play_sound()
        choice_num = len(app.choices)
        if app.moves[choice_num] != self:
            error_sound()
            print('you lose!')
            fl_message('you got ' + (str(len(app.moves)-1) + ' right'))
            app.reset()
            app.mode = 'game'
            app.display_moves()
            return
        app.choices.append(self)
        if len(app.choices) == len(app.moves):
            print('you win!', len(app.choices))
            app.select_random_button()
            app.choices = []
            app.mode = 'game'
            app.display_moves()

class App(Fl_Window):
    def __init__(self, x, y, w, h, title):
        super().__init__(x, y, w, h, title)
        self.moves = []
        self.choices = []
        self.mode = 'game'  # can also be 'user_input'
        self.begin()
        # original_color = original_color.get(red_but)
        red_but = GameButton(0, 0, 100, 100, 'red_but', 9, 1, 'red')
        blue_but = GameButton(100, 0, 100, 100, 'blue_but', 12, 4, 'blue')
        yellow_but = GameButton(200, 0, 100, 100, 'yellow_but', 11, 3, 'yellow')
        green_but = GameButton(300, 0, 100, 100, 'green_but', 10, 20, 'green')
        self.buttons = [red_but, blue_but, yellow_but, green_but]

        self.reset()
        self.display_moves()

        self.end()
        self.show()

    def reset(self):
        self.moves = []
        self.choices = []
        self.select_random_button()

    def select_random_button(self):
        random_button = random.choice(self.buttons)
        self.moves.append(random_button)

    def display_moves(self):
        # show the user the sequence
        print("showing sequence")
        # for button in buttons:
            # button.deactivate()
        for i, button in enumerate(self.moves):
            print('showing', button.name)
            Fl.add_timeout(0.4 + i * 1.0, button.flash_button)
        Fl.add_timeout(0.7 + (1.0 * len(self.moves)), self.set_user_input)


    def set_user_input(self):
        print('setting mode to user input')
        self.mode = 'user_input'

app = App(100, 100, 1000, 100, 'SimonSays')





        
# class Buttonclass:   

Fl.run()

#FL_WHEN_NEVER
#iterate thru every button and when never then once sequence is over can out back to FL_WHEN_RELEASE so put it during the sequence and change afterwards

#.color(FL_RED/an integer 0-255, bg color) ok yeah we already learned this bruhhhh

#to-do list:
#use a mode other than deactivated to stop clicking cheat 5 done
#white flash for selected buttons 2 done
#buttons start on a colour 1 done
#buttons become a brighter version of themselves when selected 3 done
#reformat so it's pretty 6
#windows popup when you lose and your enumerated amount of wins 4
# add sound for all things 7 done

#I want a musical mode lolololol
#then i gotta do this all over again
