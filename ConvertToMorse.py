import MorseDict


def convert_to_morse(text):
    morse = []
    upper_text = text.upper()
    morse_dict = MorseDict.MorseDict
    for char in upper_text:
        morse.append(morse_dict[char])

    return morse


def convert_input_to_morse():
    keep_going = True
    try:
        while keep_going:
            text = input("Enter some text: ")
            print(convert_to_morse(text))
    except KeyboardInterrupt:
        keep_going = False


convert_input_to_morse()
