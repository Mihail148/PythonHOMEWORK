# 27. Пользователь вводит текст(строка). Словом считается последовательность 
# непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки. 
# Определите, сколько различныхслов содержится в этом тексте.

input_text = input("Введите текст: ").upper()
count = 1
word_list = set(input_text)
word = ""
for char in input_text:
    if char != " ":
        word += char
    else:
        word_list.add(word)
        word = ""
print(len(word_list))            