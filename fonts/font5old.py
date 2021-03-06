from functools import reduce

_ = 0
X = 1

class FontBase(UserDict):
    def __init__(self, chars):
        self.data = chars
        # for k, v in chars.items:
        #     self.data[k] = v
    
    def measure(self, text):
        size = 0
        for c in text:
            size += len(self[c][0])
        return size

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        print(f'missing character "{key}"')
        return self.data['?']

Font5 = FontBase({
    ' ': [
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _]
    ],
    # ' ': [
    #     [_, _, _, _],
    #     [_, _, _, _],
    #     [_, _, _, _],
    #     [_, _, _, _],
    #     [_, _, _, _],
    #     [_, _, _, _],
    #     [_, _, _, _],
    #     [_, _, _, _]
    # ],
    'A': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'B': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, _, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'C': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, _, _, _],
        [X, _, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'D': [
        [_, _, _, _],
        [X, X, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'E': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'F': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, _, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'G': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'H': [
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'I': [
        [_, _],
        [X, _],
        [X, _],
        [X, _],
        [X, _],
        [X, _],
        [_, _],
        [_, _]
    ],
    'J': [
        [_, _, _, _],
        [_, _, X, _],
        [_, _, X, _],
        [_, _, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'K': [
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'L': [
        [_, _, _, _],
        [X, _, _, _],
        [X, _, _, _],
        [X, _, _, _],
        [X, _, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'M': [
        [_, _, _, _, _, _],
        [X, _, _, _, X, _],
        [X, X, _, X, X, _],
        [X, _, X, _, X, _],
        [X, _, _, _, X, _],
        [X, _, _, _, X, _],
        [_, _, _, _, _, _],
        [_, _, _, _, _, _]
    ],
    'N': [
        [_, _, _, _, _],
        [X, _, _, X, _],
        [X, X, _, X, _],
        [X, _, X, X, _],
        [X, _, _, X, _],
        [X, _, _, X, _],
        [_, _, _, _, _],
        [_, _, _, _, _]
    ],
    'O': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'P': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, _, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'Q': [
        [_, _, _, _, _],
        [X, X, X, X, _],
        [X, _, _, X, _],
        [X, _, _, X, _],
        [X, _, X, X, _],
        [X, X, X, X, _],
        [_, _, _, X, _],
        [_, _, _, _, _]
    ],
    'R': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'S': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, X, X, _],
        [_, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'T': [
        [_, _, _, _],
        [X, X, X, _],
        [_, X, _, _],
        [_, X, _, _],
        [_, X, _, _],
        [_, X, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'U': [
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'V': [
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, X, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'W': [
        [_, _, _, _, _, _],
        [X, _, _, _, X, _],
        [X, _, _, _, X, _],
        [X, _, _, _, X, _],
        [X, _, X, _, X, _],
        [_, X, _, X, _, _],
        [_, _, _, _, _, _],
        [_, _, _, _, _, _]
    ],
    'X': [
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, X, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'Y': [
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, X, _, _],
        [_, X, _, _],
        [_, X, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'Z': [
        [_, _, _, _],
        [X, X, X, _],
        [_, _, X, _],
        [_, X, _, _],
        [X, _, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'a': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, X, X, _],
        [X, _, X, _],
        [_, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'b': [
        [_, _, _, _],
        [X, _, _, _],
        [X, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'c': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'd': [
        [_, _, _, _],
        [_, _, X, _],
        [_, _, X, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'e': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'f': [
        [_, _, _],
        [_, X, _],
        [X, _, _],
        [X, X, _],
        [X, _, _],
        [X, _, _],
        [_, _, _],
        [_, _, _]
    ],
    'g': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, X, _],
        [X, X, X, _]
    ],
    'h': [
        [_, _, _, _],
        [X, _, _, _],
        [X, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'i': [
        [_, _],
        [X, _],
        [_, _],
        [X, _],
        [X, _],
        [X, _],
        [_, _],
        [_, _]
    ],
    'j': [
        [_, _],
        [X, _],
        [_, _],
        [X, _],
        [X, _],
        [X, _],
        [X, _],
        [_, _]
    ],
    'k': [
        [_, _, _, _],
        [X, _, _, _],
        [X, _, _, _],
        [X, _, X, _],
        [X, X, _, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'l': [
        [_, _],
        [X, _],
        [X, _],
        [X, _],
        [X, _],
        [X, _],
        [_, _],
        [_, _]
    ],
    'm': [
        [_, _, _, _, _, _],
        [_, _, _, _, _, _],
        [_, _, _, _, _, _],
        [X, X, X, X, X, _],
        [X, _, X, _, X, _],
        [X, _, X, _, X, _],
        [_, _, _, _, _, _],
        [_, _, _, _, _, _]
    ],
    'n': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'o': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'p': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, _, _, _]
    ],
    'q': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, X, _],
        [_, _, X, _]
    ],
    'r': [
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [X, X, _],
        [X, _, _],
        [X, _, _],
        [_, _, _],
        [_, _, _]
    ],
    's': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, X, X, _],
        [_, X, _, _],
        [X, X, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    't': [
        [_, _, _],
        [_, _, _],
        [X, _, _],
        [X, X, _],
        [X, _, _],
        [_, X, _],
        [_, _, _],
        [_, _, _]
    ],
    'u': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'v': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, X, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'w': [
        [_, _, _, _, _, _],
        [_, _, _, _, _, _],
        [_, _, _, _, _, _],
        [X, _, X, _, X, _],
        [X, _, X, _, X, _],
        [_, X, _, X, _, _],
        [_, _, _, _, _, _],
        [_, _, _, _, _, _]
    ],
    'x': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, _, X, _],
        [_, X, _, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    'y': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, X, _],
        [X, X, X, _]
    ],
    'z': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, X, _, _],
        [_, X, _, _],
        [_, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '0': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '1': [
        [_, _, _, _],
        [_, _, X, _],
        [_, X, X, _],
        [_, _, X, _],
        [_, _, X, _],
        [_, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '2': [
        [_, _, _, _],
        [X, X, X, _],
        [_, _, X, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '3': [
        [_, _, _, _],
        [X, X, X, _],
        [_, _, X, _],
        [X, X, X, _],
        [_, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '4': [
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, X, _],
        [_, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '5': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, X, X, _],
        [_, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '6': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '7': [
        [_, _, _, _],
        [X, X, X, _],
        [_, _, X, _],
        [_, _, X, _],
        [_, _, X, _],
        [_, _, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '8': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '9': [
        [_, _, _, _],
        [X, X, X, _],
        [X, _, X, _],
        [X, X, X, _],
        [_, _, X, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '!': [
        [_, _],
        [X, _],
        [X, _],
        [X, _],
        [_, _],
        [X, _],
        [_, _],
        [_, _]
    ],
    '"': [
        [_, _, _, _],
        [X, _, X, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '#': [
        [_, _, _, _, _, _],
        [_, X, _, X, _, _],
        [X, X, X, X, X, _],
        [_, X, _, X, _, _],
        [X, X, X, X, X, _],
        [_, X, _, X, _, _],
        [_, _, _, _, _, _],
        [_, _, _, _, _, _]
    ],
    '$': [
        [_, X, _, _],
        [X, X, X, _],
        [X, _, _, _],
        [X, X, X, _],
        [_, _, X, _],
        [X, X, X, _],
        [_, X, _, _],
        [_, _, _, _]
    ],
    '£': [
        [_, _, _, _],
        [_, X, X, _],
        [_, X, _, _],
        [X, X, X, _],
        [_, X, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '%': [
        [_, _, _, _, _],
        [_, _, _, _, _],
        [X, _, _, X, _],
        [_, _, X, _, _],
        [_, X, _, _, _],
        [X, _, _, X, _],
        [_, _, _, _, _],
        [_, _, _, _, _]
    ],
    # '&': [
    #     [_, _, _, _, _],
    #     [X, X, X, _, _],
    #     [X, _, X, _, _],
    #     [X, X, X, X, _],
    #     [X, _, X, _, _],
    #     [X, X, X, X, _],
    #     [_, _, _, _, _],
    #     [_, _, _, _, _]
    # ],
    '&': [
        [_, _, _, _, _],
        [X, X, _, _, _],
        [X, _, X, _, _],
        [_, X, _, X, _],
        [X, _, X, _, _],
        [X, X, X, X, _],
        [_, _, _, _, _],
        [_, _, _, _, _]
    ],
    '\'': [
        [_, _],
        [X, _],
        [X, _],
        [_, _],
        [_, _],
        [_, _],
        [_, _],
        [_, _]
    ],
    '(': [
        [_, X, _],
        [X, _, _],
        [X, _, _],
        [X, _, _],
        [X, _, _],
        [X, _, _],
        [_, X, _],
        [_, _, _]
    ],
    ')': [
        [X, _, _],
        [_, X, _],
        [_, X, _],
        [_, X, _],
        [_, X, _],
        [_, X, _],
        [X, _, _],
        [_, _, _]
    ],
    '{': [
        [_, _, X, _],
        [_, X, _, _],
        [_, X, _, _],
        [X, X, _, _],
        [_, X, _, _],
        [_, X, _, _],
        [_, _, X, _],
        [_, _, _, _]
    ],
    '}': [
        [X, _, _, _],
        [_, X, _, _],
        [_, X, _, _],
        [_, X, X, _],
        [_, X, _, _],
        [_, X, _, _],
        [X, _, _, _],
        [_, _, _, _]
    ],
    '[': [
        [X, X, _],
        [X, _, _],
        [X, _, _],
        [X, _, _],
        [X, _, _],
        [X, _, _],
        [X, X, _],
        [_, _, _]
    ],
    ']': [
        [X, X, _],
        [_, X, _],
        [_, X, _],
        [_, X, _],
        [_, X, _],
        [_, X, _],
        [X, X, _],
        [_, _, _]
    ],
    '*': [
        [_, _, _, _],
        [X, _, X, _],
        [_, X, _, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '+': [
        [_, _, _, _],
        [_, _, _, _],
        [_, X, _, _],
        [X, X, X, _],
        [_, X, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '-': [
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '/': [
        [_, _, _, _, _, _],
        [_, _, _, _, X, _],
        [_, _, _, X, _, _],
        [_, _, X, _, _, _],
        [_, X, _, _, _, _],
        [X, _, _, _, _, _],
        [_, _, _, _, _, _],
        [_, _, _, _, _, _]
    ],
    '\\': [
        [_, _, _, _, _, _],
        [X, _, _, _, _, _],
        [_, X, _, _, _, _],
        [_, _, X, _, _, _],
        [_, _, _, X, _, _],
        [_, _, _, _, X, _],
        [_, _, _, _, _, _],
        [_, _, _, _, _, _]
    ],
    '=': [
        [_, _, _, _],
        [_, _, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [X, X, X, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '.': [
        [_, _],
        [_, _],
        [_, _],
        [_, _],
        [_, _],
        [X, _],
        [_, _],
        [_, _]
    ],
    ',': [
        [_, _],
        [_, _],
        [_, _],
        [_, _],
        [_, _],
        [X, _],
        [X, _],
        [_, _]
    ],
    ':': [
        [_, _],
        [_, _],
        [X, _],
        [_, _],
        [X, _],
        [_, _],
        [_, _],
        [_, _]
    ],
    ';': [
        [_, _],
        [_, _],
        [_, _],
        [X, _],
        [_, _],
        [X, _],
        [X, _],
        [_, _]
    ],
    '<': [
        [_, _, _],
        [_, _, _],
        [_, X, _],
        [X, _, _],
        [_, X, _],
        [_, _, _],
        [_, _, _],
        [_, _, _]
    ],
    '>': [
        [_, _, _],
        [_, _, _],
        [X, _, _],
        [_, X, _],
        [X, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _]
    ],
    '?': [
        [_, _, _, _],
        [X, X, X, _],
        [_, _, X, _],
        [_, X, X, _],
        [_, _, _, _],
        [_, X, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '^': [
        [_, _, _, _],
        [_, X, _, _],
        [X, _, X, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _],
        [_, _, _, _]
    ],
    '°': [
        [_, _, _],
        [X, X, _],
        [X, X, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _]
    ],
    '`': [
        [_, _, _],
        [X, _, _],
        [_, X, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _],
        [_, _, _]
    ],
    '|': [
        [X, _],
        [X, _],
        [X, _],
        [X, _],
        [X, _],
        [X, _],
        [X, _],
        [_, _]
    ]
})

# Font5["’"] = Font5["'"]
# Font5["‘"] = Font5["'"]
# Font5['“'] = Font5['"']
# Font5['”'] = Font5['"']
# Font5["—"] = Font5["-"]

# Font5['À'] = Font5['A']
# Font5['Á'] = Font5['A']
# Font5['Â'] = Font5['A']
# Font5['Ä'] = Font5['A']
# Font5['Å'] = Font5['A']
# Font5['Ã'] = Font5['A']
# Font5['à'] = Font5['a']
# Font5['á'] = Font5['a']
# Font5['â'] = Font5['a']
# Font5['ä'] = Font5['a']
# Font5['å'] = Font5['a']
# Font5['ã'] = Font5['a']
# Font5['È'] = Font5['E']
# Font5['É'] = Font5['E']
# Font5['Ê'] = Font5['E']
# Font5['Ë'] = Font5['E']
# Font5['è'] = Font5['e']
# Font5['é'] = Font5['e']
# Font5['ê'] = Font5['e']
# Font5['ë'] = Font5['e']
# Font5['Ì'] = Font5['I']
# Font5['Í'] = Font5['I']
# Font5['Î'] = Font5['I']
# Font5['Ï'] = Font5['I']
# Font5['ì'] = Font5['i']
# Font5['í'] = Font5['i']
# Font5['î'] = Font5['i']
# Font5['ï'] = Font5['i']
# Font5['Ò'] = Font5['O']
# Font5['Ó'] = Font5['O']
# Font5['Ô'] = Font5['O']
# Font5['Ö'] = Font5['O']
# Font5['Õ'] = Font5['O']
# Font5['ò'] = Font5['o']
# Font5['ó'] = Font5['o']
# Font5['ô'] = Font5['o']
# Font5['ö'] = Font5['o']
# Font5['õ'] = Font5['o']
# Font5['Ù'] = Font5['U']
# Font5['Ú'] = Font5['U']
# Font5['Û'] = Font5['U']
# Font5['Ü'] = Font5['U']
# Font5['ù'] = Font5['u']
# Font5['ú'] = Font5['u']
# Font5['û'] = Font5['u']
# Font5['ü'] = Font5['u']
# Font5['Ñ'] = Font5['N']
# Font5['ñ'] = Font5['n']

if __name__ == "__main__":
    for k in Font5.data:
        # print(k)
        char = list(map(lambda c: reduce(lambda a,b: str(a)+str(b), c), Font5.data[k]))
        nums = list(map(lambda a: '0x'+hex(int(a[::-1], 2))[2:].zfill(2).upper(), char))
        # print(nums)

        print(f'\'{k}\': ({len(char[0])-1}, [{", ".join(nums)}]),')