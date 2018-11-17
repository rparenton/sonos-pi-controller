import os
import json
from threading import Timer
from threading import Thread

from pygame import Rect
import requests

import soco

from controller.ui.scene import Scene
from controller.ui.image import Image
from controller.ui.button import Button
from controller.ui.window import Window
import color


# Environment Vars
API_URL = os.getenv('API_URL')

class NowPlaying(Scene):
    def __init__(self):
        Scene.__init__(self)        
        self.rooms = requests.get(API_URL + '/rooms').json()
        self.current_room = 'tvroom' #self.rooms[0]  
        print(self.current_room)  

        self.background_color = color.NAVY             
        ##### Play Button #####
        play_track_img = Image('play_track','play_track.png')
        #Center bottom positioning
        self.play_button = Button(Rect(130,330,60,60),image=play_track_img)
        #Touch Handler
        self.play_button.on_tapped.connect(self.play)
        self.add_child(self.play_button)

        ##### Pause Button #####
        pause_track_img = Image('pause_track','pause_track.png')
        #Center bottom positioning
        self.pause_button = Button(Rect(130,330,60,60),image=pause_track_img)
        #Hide to start
        self.pause_button.hidden = True        
        #Touch Handler
        self.pause_button.on_tapped.connect(self.pause)
        self.add_child(self.pause_button)

        


    def play(self, button): 
        self.play_button.hidden = True
        self.pause_button.hidden = False          
        requests.post(API_URL + '/rooms/{}/play'.format(self.current_room))

    def pause(self, button):
        self.play_button.hidden = False
        self.pause_button.hidden = True        
        requests.post(API_URL + '/rooms/{}/pause'.format(self.current_room))
       