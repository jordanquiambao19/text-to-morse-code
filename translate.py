ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

MORSE_TO_ENGLISH = {}
for key, value in ENGLISH_TO_MORSE.items():
    MORSE_TO_ENGLISH[value] = key

LOGO = """ _______  _______  __   __  _______    _______  _______    __   __  _______  ______    _______  _______ 
|       ||       ||  |_|  ||       |  |       ||       |  |  |_|  ||       ||    _ |  |       ||       |
|_     _||    ___||       ||_     _|  |_     _||   _   |  |       ||   _   ||   | ||  |  _____||    ___|
  |   |  |   |___ |       |  |   |      |   |  |  | |  |  |       ||  | |  ||   |_||_ | |_____ |   |___ 
  |   |  |    ___| |     |   |   |      |   |  |  |_|  |  |       ||  |_|  ||    __  ||_____  ||    ___|
  |   |  |   |___ |   _   |  |   |      |   |  |       |  | ||_|| ||       ||   |  | | _____| ||   |___ 
  |___|  |_______||__| |__|  |___|      |___|  |_______|  |_|   |_||_______||___|  |_||_______||_______|
 __   __  _______  ______    _______  _______    _______  _______    _______  _______  __   __  _______ 
|  |_|  ||       ||    _ |  |       ||       |  |       ||       |  |       ||       ||  |_|  ||       |
|       ||   _   ||   | ||  |  _____||    ___|  |_     _||   _   |  |_     _||    ___||       ||_     _|
|       ||  | |  ||   |_||_ | |_____ |   |___     |   |  |  | |  |    |   |  |   |___ |       |  |   |  
|       ||  |_|  ||    __  ||_____  ||    ___|    |   |  |  |_|  |    |   |  |    ___| |     |   |   |  
| ||_|| ||       ||   |  | | _____| ||   |___     |   |  |       |    |   |  |   |___ |   _   |  |   |  
|_|   |_||_______||___|  |_||_______||_______|    |___|  |_______|    |___|  |_______||__| |__|  |___|  """


def encode(text):
    morse = []
    for letter in text:
        if letter == " ":
            morse.append("/")
        elif letter.upper() in ENGLISH_TO_MORSE:
            morse.append(ENGLISH_TO_MORSE[letter.upper()])
    return " ".join(morse)

def decode(code):
    english = []
    for item in code.split(" "):
        if item == "/" or item == " ":
            english.append(" ")
        elif item in MORSE_TO_ENGLISH:
            english.append(MORSE_TO_ENGLISH[item])
    return "".join(english).capitalize()

print(LOGO)

choice = input("Please type 'encode' or 'decode':")

message = input("Input word to encode or Morse code to decode:")

if choice == 'encode':
    print(encode(message))
else:
    print(decode(message))