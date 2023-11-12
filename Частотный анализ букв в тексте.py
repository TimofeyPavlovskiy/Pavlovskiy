# TODO  Напишите функцию count_letters

def count_letters(text):
    small_letters = text.lower()

    how_many_letters = {}
    for every_char in small_letters:
        if every_char.isalpha():
            if every_char in how_many_letters:
                how_many_letters[every_char] += 1
            else:
                how_many_letters[every_char] = 1
    return how_many_letters

# TODO Напишите функцию calculate_frequency

def calculate_frequency(how_many_letters):
    total_amount = sum(how_many_letters.values())

    letter_frequency = {}
    for current_letter, count in how_many_letters.items(): letter_frequency[current_letter] = count / total_amount

    return letter_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

letters_in_current_text = count_letters(main_str)
frequency_in_current_text = calculate_frequency(letters_in_current_text)

for letter, frequency in frequency_in_current_text.items():
    print(f"{letter}: {frequency:.2f}")