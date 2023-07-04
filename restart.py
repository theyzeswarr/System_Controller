import os

def restart_windows():
    if os.name == 'nt':  
        os.system('shutdown /r /t 0')
    else:
        print("Restarting is only supported on Windows.")

restart_windows()