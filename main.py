from kivymd.app import MDApp
from specialbuttons import LabelButton, ImageButton
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from kivy.core.window import Window
from homemapview import HomeMapView
from searchpopumenu import SearchPopupMenu
from homegpshelper import HomeGpsHelper
import os 


Window.size = (375, 750)

class HomeScreen(Screen):
    pass
 

class MainApp(MDApp):	

  search_menu = None

  current_lat = -23.6687
  current_lon =  -46.4614

  if os.path.isfile("profile_source.txt"):
    with open("profile_source.txt", "r") as f:
        some_path = f.read()
        if len(some_path) > 0:
            img_source_path = some_path
        else:
            img_source_path = "empty.png"
  else:
   img_source_path = "empty.png"

def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        # Initialize GPS
        HomeGpsHelper().run()

        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

def navigation_draw(self, args):
        print("Navigation")

def change_screen(self, screen_name, direction='forward', mode = ""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager
 
        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return
 
        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name
 
        if screen_name == "home_screen":
            self.root.ids.titlename.title = "Aqui tem medicamento"   
 
MainApp().run()