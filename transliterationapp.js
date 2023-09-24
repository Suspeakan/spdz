const latinToCyrillic = {  'A': 'А', 'a': 'а',
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
'´T': 'Ѳ', '´t': 'ѳ',
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
}; 

function convertToCyrillic() {
    const latinInput = document.getElementById('latin-input').value;
    let cyrillicOutput = '';

    // Perform transliteration
    let buffer = '';
    for (let char of latinInput) {
        if (char === ' ') {
            cyrillicOutput += buffer + ' ';
            buffer = '';
        } else {
            buffer += char;
            if (buffer in latinToCyrillic) {
                cyrillicOutput += latinToCyrillic[buffer];
                buffer = '';
            }
        }
    }
    cyrillicOutput += buffer;

    // Display the result
    const cyrillicOutputDiv = document.getElementById('cyrillic-output');
    cyrillicOutputDiv.textContent = cyrillicOutput;
}