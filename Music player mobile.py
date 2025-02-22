import os
import fnmatch
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from pygame import mixer

# Initialize mixer
mixer.init()

class MusicPlayer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        self.file_chooser = FileChooserListView()
        self.add_widget(self.file_chooser)
        
        self.play_button = Button(text="Play")
        self.play_button.bind(on_press=self.play_song)
        self.add_widget(self.play_button)
        
        self.pause_button = Button(text="Pause")
        self.pause_button.bind(on_press=self.pause_song)
        self.add_widget(self.pause_button)
        
        self.resume_button = Button(text="Resume")
        self.resume_button.bind(on_press=self.resume_song)
        self.add_widget(self.resume_button)
        
        self.stop_button = Button(text="Stop")
        self.stop_button.bind(on_press=self.stop_song)
        self.add_widget(self.stop_button)
        
        self.volume_slider = Slider(min=0, max=1, value=0.7)
        self.volume_slider.bind(value=self.set_volume)
        self.add_widget(Label(text="Volume"))
        self.add_widget(self.volume_slider)
    
    def play_song(self, instance):
        if self.file_chooser.selection:
            mixer.music.load(self.file_chooser.selection[0])
            mixer.music.play()
    
    def pause_song(self, instance):
        mixer.music.pause()
    
    def resume_song(self, instance):
        mixer.music.unpause()
    
    def stop_song(self, instance):
        mixer.music.stop()
    
    def set_volume(self, instance, value):
        mixer.music.set_volume(value)

class MusicPlayerApp(App):
    def build(self):
        return MusicPlayer()

if __name__ == "__main__":
    MusicPlayerApp().run()