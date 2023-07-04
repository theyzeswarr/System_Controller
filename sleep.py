import os

def sleep_windows():
    if os.name == 'nt':  
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
    else:
        print("Sleep mode is only supported on Windows.")
        
sleep_windows()
