#!/bin/bash

# سكربت لإعداد أدوات الأمن السيبراني الأساسية على توزيعة Ubuntu أو Kali Linux

echo "تحديث النظام..."
sudo apt update && sudo apt upgrade -y

echo "تثبيت Wireshark..."
sudo apt install -y wireshark

echo "تثبيت Nmap..."
sudo apt install -y nmap

echo "تثبيت Snort..."
sudo apt install -y snort

echo "تثبيت hping3 (أداة محاكاة هجمات DDoS)..."
sudo apt install -y hping3

echo "تثبيت net-tools (لأوامر مثل ifconfig)..."
sudo apt install -y net-tools

echo "تثبيت tcpdump..."
sudo apt install -y tcpdump

echo "تم تثبيت الأدوات الأساسية بنجاح ✅"
