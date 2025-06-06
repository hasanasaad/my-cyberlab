from scapy.all import sniff, IP
from collections import defaultdict
import time

# إعدادات المراقبة
monitor_interface = "eth0"  # غيّر إلى واجهة الشبكة المناسبة (مثلاً wlan0 أو ens33)
time_window = 10  # ثواني: نافذة الوقت التي يتم فيها حساب عدد الحزم
packet_threshold = 100  # إذا أرسل IP أكثر من هذا العدد خلال time_window، يُعتبر مشبوهاً

# قاعدة بيانات مؤقتة لتخزين عدد الحزم لكل IP
packet_counter = defaultdict(int)
start_time = time.time()

def process_packet(packet):
    global start_time, packet_counter

    if IP in packet:
        src_ip = packet[IP].src
        packet_counter[src_ip] += 1

    current_time = time.time()
    if current_time - start_time > time_window:
        print("\n📊 تحليل عدد الحزم خلال آخر", time_window, "ثوانٍ:")
        for ip, count in packet_counter.items():
            if count > packet_threshold:
                print(f"🚨 اشتباه بهجوم DDoS من IP: {ip} - عدد الحزم: {count}")
            else:
                print(f"✅ {ip}: {count} حزمة")
        
        # إعادة الضبط للدورة التالية
        packet_counter.clear()
        start_time = current_time

print(f"🔍 بدء مراقبة الواجهة: {monitor_interface}...")
sniff(iface=monitor_interface, prn=process_packet, store=0)
