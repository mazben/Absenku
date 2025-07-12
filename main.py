from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from datetime import datetime

KV = """..."""  # kode layout seperti sebelumnya
class AbsenKu(App):
    riwayat_file = "riwayat_absen.txt"
    ...
if __name__ == "__main__":
    AbsenKu().run()
