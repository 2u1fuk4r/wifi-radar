import tkinter as tk
from datetime import datetime
from scapy.all import *
import time

# WiFi sembolünü çizmek için fonksiyon
def draw_wifi_symbol(canvas):
    canvas.create_line(50, 75, 50, 25, width=5, tags="wifi")
    canvas.create_line(50, 75, 75, 40, width=5, tags="wifi")
    canvas.create_line(50, 75, 25, 40, width=5, tags="wifi")
    canvas.create_oval(40, 60, 60, 80, width=5, tags="wifi")

# WiFi sinyali animasyonunu oluşturmak için fonksiyon
def draw_signal_animation(canvas):
    colors = ["#00ff00", "#80ff00", "#bfff00", "#ffff00", "#bfff00", "#80ff00"]
    for color in colors:
        canvas.itemconfig("wifi", fill=color)
        canvas.update()
        time.sleep(0.2)

# Saldırıyı algıladığında çağrılan fonksiyon
def packet_callback(packet):
    if packet.haslayer(Dot11Deauth):
        mac_address = packet.addr2
        attack_type = "Deauth"
        update_display(mac_address, attack_type)

# Ekranı güncellemek için fonksiyon
def update_display(mac_address, attack_type):
    label_mac.config(text=f"Saldırgan MAC adresi: {mac_address}", fg="red")
    label_attack.config(text=f"Saldırı tipi: {attack_type}", fg="red")

# Saat/tarih bilgisini güncellemek için fonksiyon
def update_time():
    label_time.config(text=f"Saat/Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    root.after(1000, update_time)

# Paketleri dinlemek ve ekranı güncellemek için fonksiyon
def sniff_packets():
    sniff(iface="wlan0", prn=packet_callback, store=0, timeout=1)
    root.after(1000, sniff_packets)

# Pencere kapatıldığında gerçekleşecek işlemler için fonksiyon
def on_closing():
    root.destroy()

# Ana pencereyi oluşturma ve ayarları yapma
root = tk.Tk()
root.title("WiFi Güvenlik İzleyicisi")
root.configure(bg="white")
root.geometry("600x300")  # Pencere boyutu 600x300 olarak güncellendi
root.option_add("*Font", "Arial 20 bold")  # Font büyüklüğü 2x artırıldı

# Pencere içeriğini oluşturma
frame = tk.Frame(root, bg="white")
frame.pack(padx=20, pady=20, fill="both", expand=True)

label_mac = tk.Label(frame, text="Saldırgan MAC adresi: ", bg="white", fg="green", anchor="w")
label_mac.pack(anchor="w", fill="x")

label_attack = tk.Label(frame, text="Saldırı tipi: ", bg="white", fg="green", anchor="w")
label_attack.pack(anchor="w", fill="x")

label_time = tk.Label(frame, text="Saat/Tarih: ", bg="white", fg="green", anchor="w")
label_time.pack(anchor="w", fill="x")

label_iface = tk.Label(frame, text="Ağ Kartı Arayüzü: wlan0", bg="white", fg="green", anchor="w")
label_iface.pack(anchor="w", fill="x")

# Canvas oluşturma
wifi_canvas = tk.Canvas(frame, width=100, height=100, bg="white", highlightthickness=0)
wifi_canvas.pack()

# Kapanma olayını yakalama
root.protocol("WM_DELETE_WINDOW", on_closing)

# Sürekli saat/tarih bilgisini güncellemeye başlama
update_time()

# Paketleri dinlemeyi başlatma
try:
    root.after(1000, sniff_packets)
    # WiFi sembolünü çiz
    draw_wifi_symbol(wifi_canvas)
    # WiFi sinyali animasyonunu başlat
    while True:
        draw_signal_animation(wifi_canvas)
except KeyboardInterrupt:
    on_closing()

root.mainloop()
