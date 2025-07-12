from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from datetime import datetime

KV = """
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 20

    Label:
        id: status_label
        text: "Selamat Datang di AbsenKu"
        font_size: '20sp'
        halign: 'center'
        valign: 'middle'
        size_hint_y: None
        height: self.texture_size[1]

    Button:
        text: "Absen Masuk"
        font_size: '18sp'
        on_press: app.absen("Masuk")

    Button:
        text: "Absen Pulang"
        font_size: '18sp'
        on_press: app.absen("Pulang")

    Button:
        text: "Lihat Riwayat Absen"
        font_size: '18sp'
        on_press: app.show_riwayat()
"""

class AbsenKu(App):
    riwayat_file = "riwayat_absen.txt"

    def build(self):
        return Builder.load_string(KV)

    def absen(self, jenis):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{waktu} - Absen {jenis}\n"
        with open(self.riwayat_file, "a") as f:
            f.write(entry)
        self.root.ids.status_label.text = f"Berhasil Absen {jenis}!\n{waktu}"

    def show_riwayat(self):
        try:
            with open(self.riwayat_file, "r") as f:
                data = f.read()
            if not data.strip():
                data = "Belum ada riwayat absen."
        except FileNotFoundError:
            data = "Belum ada riwayat absen."
        self.root.ids.status_label.text = data

if __name__ == "__main__":
    AbsenKu().run()
