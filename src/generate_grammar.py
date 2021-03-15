import ntlk
import string
from ntlk.parse.generate import generate
import sys

productions = [
    "ROOT -> WORD",
    "WORD -> ' '",
    "WORD -> NUMBER LETTER",
    "WORD -> LETTER NUMBER"
]

digits = list(string.digits)
for digit in digits[:4]:
    productions.append("NUMBER -> '{w}'".format(w=digit))

letters = "' | '".join(list(string.ascii_lowercase)[:4])
productions.append("LETTER -> '{w}'".format(w=letters))

grammatString = "\n".join(productions)

grammar = ntlk.CFG.fromstring(grammatString)

print(grammar)

for sentence in generate(grammar, n=5, depth=5):
    palindrome = "".join(sentence).replace(" ", "")
    print("Generated word: {}, Size: {}".format(palindrome, len(palindrome)))
