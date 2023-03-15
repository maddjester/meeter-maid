from time import sleep

from clicknium import clicknium as cc
from clicknium import locator, ui
from pymem import Pymem, process

handle = "voicemeeter8x64.exe"
address = (0x135708)

window = locator.voicemeeter8x64.register_window

def skip_wait():
    '''
    Edits VoiceMeeter memory address for the countdown timer and re-writes it to 0.
    '''
    pm = Pymem(handle)
    module = process.module_from_name(pm.process_handle, handle).lpBaseOfDll
    value = pm.read_int(module + address)
    if value > 0 and value < 40:
        pm.write_int(module + address, 0)

if __name__ == "__main__":
    while True:
        if cc.is_existing(window):
            skip_wait()
            main_win = ui(window).parent.parent
            child_wins = main_win.children
            try:
                for win in child_wins:
                    win.send_hotkey("%{F4}", preaction="click")
            except Exception as err:
                print(err)
            finally:
                main_win.send_hotkey("%{F4}", preaction="click")
        sleep(1)
