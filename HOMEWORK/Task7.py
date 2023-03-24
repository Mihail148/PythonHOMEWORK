# Дана строка(возможно,пустая),состоящая из букв 
# A-Z:AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE,которая на выходе даст строку вида:A4B3C2XYZD4E3F3A6B28
# И сгенерируе тошибку,если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def convert(s: str) -> str:
  result: List[str] = []
  last_sym = None  # последний символ, что мы видели
  count = 0  # и сколько мы его видели
  
  # мы будем идти по строке и записывать в result при смене символа
  for sym in (list(s) + [None]): # последний None искусственно триггерит посленюю смену символа
      if last_sym and sym != last_sym:  # если случилась смена символа
          if count == 1:
              result.append(last_sym)
          else:
              result.append(last_sym + str(count))
              
          # начнаем запоминать новый символ    
          count = 1
          last_sym = sym
      else:  # символ просто повторился
          count += 1  # запомнили что символ видели на 1 раз больше
  return ''.join(result)