#!/bin/bash

# Paket listesi güncelleme ve temel araçları yükleme
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Scapy ve diğer Python bağımlılıklarını yükleme
pip3 install scapy

# Tkinter'ın yüklenmesi (genellikle Python ile birlikte gelir, ancak eksikse aşağıdaki komutu çalıştırın)
sudo apt-get install -y python3-tk

# Kullanıcıya başarıyla yüklendiğini bildirme
echo "Gerekli paketler yüklendi. Şimdi scripti çalıştırabilirsiniz."
