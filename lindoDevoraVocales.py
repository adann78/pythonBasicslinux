# Indicar al usuario que ingrese una palabra
word=input("Ingrese una palabra:")
word = word.upper()
# y asignarlo a la variable user_word.

for letter in word:
    # Completa el cuerpo del bucle for.
    if letter=='A':
        word_without_vowels=word.replace('A','')
        continue
    elif letter=='E':
        word_without_vowels=word.replace('E','')
        continue
    if letter=='I':
        word_without_vowels=word.replace('I','')    
        continue
    elif letter=='O':   
        word_without_vowels=word.replace('O','')
        continue
    elif letter=='U':
        word_without_vowels=word.replace('U','')
        continue
print(word_without_vowels)

  