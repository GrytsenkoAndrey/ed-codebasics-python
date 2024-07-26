import random


def choose_word():
    words = ["книга", "месяц", "ручка", "шарик", "олень", "носок"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '\u25A0' for letter in word)


def play_game():
    word = choose_word()
    guessed_letters = set()
    lives = 5

    print("Добро пожаловать в игру 'Угадай слово'!")

    while lives > 0:
        print(f"\nСлово: {display_word(word, guessed_letters)}")
        print(f"Жизни: {lives}")
        guess = input("Введите букву или слово целиком: ").strip().lower()

        if guess == word:
            print(f"Поздравляем! Вы угадали слово: {word}")
            break
        elif len(guess) == 1:
            if guess in word:
                guessed_letters.add(guess)
                if all(letter in guessed_letters for letter in word):
                    print(f"Поздравляем! Вы угадали слово: {word}")
                    break
            else:
                lives -= 1
                print(f"Неправильная буква! У вас осталось {lives} жизней.")
        else:
            lives -= 1
            print(f"Неправильное слово! У вас осталось {lives} жизней.")

        if lives == 0:
            print(f"Вы проиграли! Загаданное слово было: {word}")


if __name__ == "__main__":
    play_game()

# ''.join(letter if letter in guessed_letters else '\u25A0' for letter in word)
# Давайте разберем её по частям:
#
#     letter if letter in guessed_letters else '\u25A0':
#         Это тернарный оператор. Он проверяет условие letter in guessed_letters.
#         Если условие истинно (буква уже была угадана и находится в множестве guessed_letters), в результирующую строку добавляется эта буква (letter).
#         Если условие ложно (буква ещё не угадана), в результирующую строку добавляется символ '\u25A0'.
#
#     for letter in word:
#         Это цикл, который проходит по каждой букве (переменная letter) в слове word.
#
#     ''.join(...):
#         Эта функция объединяет все элементы, созданные генератором списка, в одну строку без разделителей.
#
# Соединяя все части вместе, эта строка создаёт новую строку, в которой:
#
#     Каждая угаданная буква отображается в её реальном виде.
#     Каждая неугаданная буква отображается символом '\u25A0'.
#
# Например, если word = "книга" и guessed_letters = {'к', 'и'}, то результат выполнения будет "к\u25A0и\u25A0\u25A0".

# all(letter in guessed_letters for letter in word)
#
# Эта строка использует встроенную функцию all() и генератор списка, чтобы проверить, были ли угаданы все буквы в слове word.
#
#     letter in guessed_letters for letter in word:
#         Это генератор списка (или выражение-генератор).
#         Он последовательно проверяет каждую букву letter в слове word.
#         Для каждой буквы проверяется, находится ли она в множестве guessed_letters.
#         Генератор возвращает True или False для каждой буквы: True, если буква угадана (то есть находится в guessed_letters), и False, если не угадана.
#
#     all(...):
#         Функция all() принимает итерируемый объект (в данном случае, результат генератора списка) и возвращает True, если все элементы итерируемого объекта истинны (в данном случае, если все буквы угаданы).
#         Если хотя бы один элемент является False, функция all() вернет False.
#
# Соединяя это вместе, строка all(letter in guessed_letters for letter in word) проверяет, находятся ли все буквы слова word в множестве guessed_letters.
#
# Пример:
#
#     Если word = "книга" и guessed_letters = {'к', 'и', 'г', 'а'}, то выражение будет эквивалентно all([True, True, True, True, True]), и результат будет True, так как все буквы угаданы.
#     Если word = "книга" и guessed_letters = {'к', 'и', 'г'}, то выражение будет эквивалентно all([True, True, True, False, False]), и результат будет False, так как не все буквы угаданы.