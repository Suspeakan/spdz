latin_to_spdz = {
    'A': 'А', 'a': 'а',
    'I': 'И', 'i': 'и',
    'Í': 'Ы', 'í': 'ы',
    'U': 'У', 'u': 'у',
    'E': 'Е', 'e': 'е',
    'À': 'Э', 'à': 'э',
    'Ë': 'Ё', 'ë': 'ё',
    'O': 'О', 'o': 'о',
    'Ö': 'О̄', 'ö': 'о̄',
    'J': 'Й', 'j': 'й',
    'L': 'Л', 'l': 'л',
    'R': 'Р', 'r': 'р',
    'M': 'М', 'm': 'м',
    'N': 'Н', 'n': 'н',
    'P': 'П', 'p': 'п',
    'T': 'Т', 't': 'т',
    'K': 'К', 'k': 'к',
    'C': 'Ц', 'c': 'ц',
    '´D': 'Җ', '´d': 'җ',
    '´T': 'Θ', '´t': 'θ',
    'D': 'Д', 'd': 'д',
    'S': 'С', 's': 'с',
    'Z': 'З', 'z': 'з',
    '´S': 'Ш', '´s': 'ш',
    '`Z': 'Ж', '`z': 'ж',
    '`S': 'Щ', '`s': 'щ',
    '´Z': 'З́', '´z': 'з́',
    'X': 'Х', 'x': 'х',
    'H': 'Ҳ', 'h': 'ҳ',
    '´J': 'Я', '´j': 'я',
    '`J': 'Ю', '`j': 'ю',
    'Ý': 'Ү', 'ý': 'ү',
    'G': 'Г', 'g': 'г'
}


def convert_to_cyrillic2(input_text):
    output_text = ""
    buffer = ""

    for char in input_text:
        if char == ' ':  
            output_text += buffer + ' '  
            buffer = ""  
        else:
            buffer += char
            if buffer in latin_to_spdz:
                output_text += latin_to_spdz[buffer]
                buffer = ""

    output_text += buffer

    return output_text
        
def conv_gate_cyrillic_2():
    while True:
        latin_input = input("   .. LATIN     // : ")
        cyrillic_output2 = convert_to_cyrillic2(latin_input)
        print("   .. CYRILLIC  // :", cyrillic_output2)

        if latin_input == '0':
            return
        elif latin_input == 'q':
            print(latin_to_spdz)

def select_transliteration():
    while True:
        print(" ")
        print("// ...")
        print("   SELECT TRANSLITERATION")
        print("// ... ")
        print(" ")
        print("   .. (1) ПОХОД ПАРХА СЫПЕҖ")
        print("          POXOD PARXA SÉPEDZ")
        print("          (Latin to Cyrillic)")
        print(" ")

        choice = input("   // : ")
            
        if choice == '1':
                print("   .. (input 'q' to show map)")
                conv_gate_cyrillic_2()
            
        elif choice == 'ebbing':
            print("   ..")
            print("Under sulfur skies, the drunken tides")
            print("Will pull us in")
            print("Unfolding, but not breathing")
            print("Upon your breast, I'll rest my head")
            print("In laziness")
            print("Gestating, just dreaming")
            print("But not breathing")
            print("My swallowed tongue, my wounded dove")
            print("Your eyes are mine")
            print("Occluding, we're sinking")
            print("Just drifting, not breathing")
            print("Releasing")
            print("In shallow ponds, within your palm")
            print("There lies a mind")
            print("Dissolving, not seeing")
            print("Unfolding, not thinking")
            print("Releasing, not breathing")

        elif choice == '0':
            break

if __name__ == "__main__":
    select_transliteration()