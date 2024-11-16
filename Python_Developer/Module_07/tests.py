def remove_punctuation(text):
    # Строка с пунктуационными символами, которые нужно удалить
    punctuation = [',', '.', '=', '!', '?', ';', ':']
    # Новая строка без пунктуации
    no_punctuation = ''.join(char for char in text if char not in punctuation)
    no_punctuation_list = no_punctuation.split()
    for i in no_punctuation_list:
        if i == '-':
            no_punctuation_list.remove(i)
    return no_punctuation_list


# Исходная строка с пунктуацией
text_with_punctuation = "Пример текста с пунктуацией: здесь, там! и вот: елки - палки и елки-палки."

# Удаление пунктуации
text_without_punctuation = remove_punctuation(text_with_punctuation)

print(text_without_punctuation)
