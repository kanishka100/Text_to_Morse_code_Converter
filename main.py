to_continue = True
while to_continue:
    letter = input('Enter the string that you want to convert:').upper()
    Morse_code_word = ''
    Dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

    for i in letter:
        for key in Dict.keys():
            if key == i:
                Morse_code_word += Dict[key]
    print(f'Original word:{letter}')
    print(f"Morse Code:{Morse_code_word}")

    to_continue = input('Do you want to convert a word again(Yes/No):').title()
    if to_continue == 'Yes':
        continue
    else:
        break
