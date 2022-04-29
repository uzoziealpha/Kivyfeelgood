from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime



Builder.load_file("design.kv")

#create classes to match design.kv
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager):
    pass



class SignUpScreen(Screen):
    def add_user(self, uname, pword): 
        with open("users.json") as file:
            users = json.load(file)
        print(users)

        #to allow us create another pair of values
        users[uname] = {'username': uname, 'password': pword,
            'created' : datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    pass



class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()