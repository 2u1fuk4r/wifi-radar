# WiFi Güvenlik İzleyicisi

Bu araç, WiFi ağınızı izlemek ve deauth saldırılarını tespit etmek için kullanılır. Saldırı tespit edildiğinde, saldırganın MAC adresini ve saldırı türünü ekranda gösterir.

![logo](https://img.lovepik.com/free-png/20220125/lovepik-radar-material-png-image_401719625_wh860.png)

## Gereksinimler

- Python 3
- pip (Python paket yöneticisi)
- Scapy
- Tkinter

## Kurulum

Aşağıdaki adımları izleyerek gerekli bağımlılıkları kurabilirsiniz:

1. `install.sh` scriptini çalıştırın:

    ```bash
    chmod +x install.sh
    ./install.sh
    ```

2. Yukarıdaki komutlar gerekli tüm paketleri ve bağımlılıkları kuracaktır.

## Kullanım

Kurulum tamamlandıktan sonra, aracı başlatmak için aşağıdaki komutu kullanabilirsiniz:
Wifi kartınızın dinleme modunda oolması gerekmektedir.

ifconfig wlan0 down
iwconfig wlano mode manitor
ifconfig wlan0 up

```bash
python3 wifi-radar.py