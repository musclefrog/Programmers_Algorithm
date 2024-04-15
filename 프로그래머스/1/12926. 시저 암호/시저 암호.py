from string import ascii_uppercase
from string import ascii_lowercase

def solution(s, n):
    answer = []
    s = list(s)
    alphabet_up = list(ascii_uppercase)
    alphabet_low = list(ascii_lowercase)
    
    for letter in s:
        if letter == ' ':
            answer.append(letter)
        elif letter.isupper():
            new_i = (alphabet_up.index(letter) + n) % 26
            answer.append(alphabet_up[new_i])
        elif letter.islower():
            new_i = (alphabet_low.index(letter) + n) % 26
            answer.append(alphabet_low[new_i])
    return ''.join(answer)