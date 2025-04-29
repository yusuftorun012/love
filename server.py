import http.server
import webbrowser
import socket
import os
import threading

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Herhangi bir dış IP'ye bağlanmaya çalışıyoruz (8.8.8.8 Google DNS)
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def run_server():
    # Port numarası
    PORT = 8000
    
    # IP adresini al
    IP = get_local_ip()
    
    # Web sunucusunu başlat
    handler = http.server.SimpleHTTPRequestHandler
    httpd = http.server.HTTPServer(('0.0.0.0', PORT), handler)
    
    print(f"\nSunucu başlatıldı!")
    print(f"Yerel ağınızdaki diğer cihazlardan erişmek için:")
    print(f"http://{IP}:{PORT}/love_page.html")
    print("\nSunucuyu durdurmak için Ctrl+C tuşlarına basın...")
    
    # Sunucuyu başlat
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nSunucu durduruldu.")
        httpd.server_close()

if __name__ == "__main__":
    run_server() 