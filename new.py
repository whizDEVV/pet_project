from googletrans import Translator

user_liblary = []
language_mapping = {
    '1': 'fr',
    '2': 'de',
    '3': 'es',
    '4': 'ru',
    '5': 'uk',
    '6': 'en',
    '7': 'nl'
}

user_first_language = input('''What is your original language?
1. French
2. German
3. Spanish
4. Russian
5. Ukrainian
6. English
7. Dutch
Choose a number from 1 to 7: ''')

defaul_first_language = language_mapping.get(user_first_language, 'en')

user_second_language = input('''What language do you want to translate to?: 
1. French
2. German
3. Spanish
4. Russian
5. Ukrainian
6. English
7. Dutch
Choose a number from 1 to 7: ''')

defaul_second_language = language_mapping.get(user_second_language, 'en')

#asking and translate fuction
translator = Translator()
user_input_words = input("Put here your words to translate: ")
translated_text = translator.translate(user_input_words, src=defaul_first_language, dest=defaul_second_language).text
print(f"Your translated text: {translated_text}")

#part of saving and add to SQL / Another database user words
user_saves = input("Do u want to save these ratios of words to learn? ('yes' or 'no')?: ").lower()
if user_saves == 'yes':
    user_liblary.append((user_input_words, translated_text))


#Потом добавлю сюда цикл while, а вообще завтра это все будет сохраняться в SQL и будет заебумба
print('''
      Ваш полный набор карточок: ''')

for user_input_words, translated_text in user_liblary:
    print(f"Оригинал: {user_input_words} | Перевод: {translated_text}")