import pandas as pd

nato = pd.read_csv('nato_phonetic_alphabet.csv')
# print(nato.head(2))

nato_alpha = {row.letter: row.code for (index, row) in nato.iterrows()}

word = input('Enter word: ')
ans = [nato_alpha[letter.upper()] for letter in word]
print(ans)
