from pynput.keyboard import Controller

def write():
    key = Controller()
    key.type("My name is Kishore") #types this string where the cursor is present currently

write()