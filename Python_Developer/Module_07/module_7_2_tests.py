result = {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
for elem in result.items():
  print(elem)

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

for i in info:
  print(info.index(i), i)