![giphy (2)](https://github.com/2u1fuk4r/wifi-radar/assets/48758393/1a18f2ac-601a-4f69-916b-b65e9cc32e88)
# WiFi Güvenlik İzleyicisi

Bu araç, WiFi ağınızı izlemek ve deauth saldırılarını tespit etmek için kullanılır. Saldırı tespit edildiğinde, saldırganın MAC adresini ve saldırı türünü tespit eder.

![wifi-radar](https://github.com/2u1fuk4r/wifi-radar/assets/48758393/500f3bbc-814c-4573-adbd-de1ac8e6cf7a)

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

```bash
ifconfig wlan0 down
iwconfig wlan0 mode monitor
ifconfig wlan0 up

```bash
python3 wifi-radar.py
