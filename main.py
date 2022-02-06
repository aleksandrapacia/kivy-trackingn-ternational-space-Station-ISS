from kivymd.app import MDApp
from kivy.lang import Builder
import requests
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapMarker
from kivy.clock import Clock


class Maps_Iss(FloatLayout):

    # Atualizara a posição do ISS a cada 1 segundo
    def __init__(self, **kwargs):
        super().__init__(**kwargs)        
        Clock.schedule_interval(self.update_map, 1)        

    # Usando api do ISS para pegar a posição da estação espacial internacional e atualizar o mapa
    def update_map(self, dt):
        r = requests.get('http://api.open-notify.org/iss-now.json')
        data = r.json()
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']
        self.map = self.ids.map
        self.marker = MapMarker( lat=lat, lon=lon, source = 'iss.png')
        self.map.add_widget(self.marker)   

class MyApp(MDApp):

    def build(self):
        Builder.load_file('main.kv')
        self.title = 'ISS Tracker'
        return Maps_Iss()

MyApp().run()