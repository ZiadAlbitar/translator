def on_received_number(receivedNumber):
    pass
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global morse_letter
    basic.clear_screen()
    morse_letter = "" + morse_letter + "."
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global string_to_send, morse_letter
    string_to_send = "" + string_to_send + alphabet[morse_alphabet.index(morse_letter)]
    morse_letter = "\"something else\""
    basic.show_string(string_to_send)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global morse_letter
    basic.clear_screen()
    morse_letter = "" + morse_letter + "-"
input.on_button_pressed(Button.B, on_button_pressed_b)

morse_letter = ""
alphabet: List[str] = []
morse_alphabet: List[str] = []
string_to_send = ""
radio.set_group(1)
string_to_send = ""
morse_alphabet = [".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--.."]
alphabet = ["a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"]
morse_letter = ""