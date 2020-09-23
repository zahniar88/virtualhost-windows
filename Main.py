import os
from subprocess import call

DIR_FILE = os.path.dirname(__file__) + "/"
TARGET_DIR = "C:/xampp/apache/conf/extra/site-available/"
HOST_FILE = "C:/Windows/System32/drivers/etc/hosts"
INCLUDE =  'Include "conf/extra/site-available/#FILE#.conf"'
TARGET_FILE = "C:/xampp/apache/conf/extra/httpd-vhosts.conf"
TARGET_SSL = "C:/xampp/ssl/"

# read http file sample
http = open(DIR_FILE + 'host/http.conf', 'r')
HTTP_READ = http.read()
http.close()

# read https file sample\
https = open(DIR_FILE + 'host/https.conf', 'r')
HTTPS_READ = https.read()
https.close()

menu = open(DIR_FILE + 'menu.text', 'r')
MENU_READ = menu.read()
menu.close()

class Main():
    # memulai aplikasi
    def start(self):
        self.cmd()
        self.get_select_menu()

    # memulai command
    def cmd(self):
        call('cls', shell=True)
        self.QUSTION = input(MENU_READ)

    # mengambil menu yang dipilih
    def get_select_menu(self):
        if self.QUSTION not in ("1", "2", "3", "0"):
            self.start()
        elif self.QUSTION == "1":
            self.http()
            self.question()
            call('cls', shell=True)
            print('success')
        elif self.QUSTION == "2":
            self.https()
            self.question()
            call('cls', shell=True)
            print('success')
        elif self.QUSTION == "3":
            self.remove_host()
        else:
            call('cls', shell=True)
            print('Bye!')
        
    # jika http
    def http(self):
        call('cls', shell=True)
        self.FILENAME = input('Masukkan nama file (tanpa .conf) >>> ')
        self.DIR = input('Masukkan lokasi direkotri "C:/xampp/htdocs/ >>> ')
        self.DOMAIN = input('Masukkan nama domain >>> ')

        C1 = HTTP_READ.replace("#DOMAIN", self.DOMAIN)
        C2 = C1.replace("#DIR", self.DIR)

        self.HAS_CHANGE = C2

    # jika https
    def https(self):
        call('cls', shell=True)
        self.FILENAME = input('Masukkan nama file (tanpa .conf) >>> ')
        self.DIR = input('Masukkan lokasi direkotri "C:/xampp/htdocs/ >>> ')
        self.DOMAIN = input('Masukkan nama domain >>> ')
        self.SSL = input('Masukkan lokasi ssl C:/xampp/ssl/ >>> ')
        self.SSL_KEY = input('Masukkan lokasi ssl key C:/xampp/ssl/ >>> ')

        C1 = HTTPS_READ.replace("#DOMAIN", self.DOMAIN)
        C2 = C1.replace("#DIR", self.DIR)
        C3 = C2.replace("#SSLC", self.SSL)
        C4 = C3.replace("#SSL_KEY", self.SSL_KEY)

        self.HAS_CHANGE = C4

        call('cd C:/xampp/ssl/ && mkcert ' + self.DOMAIN)

    # pertanyaan konfirmasi
    def question(self):
        confirm = input(self.HAS_CHANGE + "\n\nApakah data sudah benar? (y|n) >>> ")

        if confirm not in ("Y", "y", "N", "n"):
            self.question()
        elif confirm in ("Y", "y"):
            make_file = open(TARGET_DIR + self.FILENAME + '.conf', 'w')
            make_file.write(self.HAS_CHANGE)
            make_file.close()

            call('code ' + HOST_FILE, shell=True)
            call('code ' + TARGET_FILE, shell=True)
        elif confirm in ("N", "n"):
            self.start()
    
    # menghapus host
    def remove_host(self):
        call('cls', shell=True)
        filename = input('Masukkan nama file yang akan dihapus (tanpa .conf) >>> ')

        confirm = input('Apakah kamu yakin akan menghapus ' + filename + '.conf? (y|n) >>> ')
        if confirm not in ("Y", "y", "N", "n"):
            self.remove_host()
        elif confirm in ("Y", "y"):
            call('rm ' + TARGET_DIR + filename + '.conf', shell=True)
            call('code ' + HOST_FILE, shell=True)
            call('code ' + TARGET_FILE, shell=True)
        elif confirm in ("N", "n"):
            self.start()

if os.path.exists('C:/xampp/apache/conf/extra/site-available') and os.path.exists('C:/xampp/ssl'):
    Main().start()
else:
    call('cd C:/xampp/apache/conf/extra/ && mkdir site-available', shell=True)
    call('cd C:/xampp/ && mkdir ssl', shell=True)
    Main().start()
