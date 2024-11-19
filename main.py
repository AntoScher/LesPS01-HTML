import requests
from bs4 import BeautifulSoup
from googletrans import Translator

"""translator = Translator()
translation = translator.translate('Hello, world!', dest='ru')
print(translation.text)"""

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except Exception as e:
        print("Произошла ошибка при получении данных с сайта:", e)
        return None

def word_game():
    translator = Translator()
    print("Игра начинается!")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            print("Произошла ошибка при получении данных с сайта.")
            break
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение
        word_translated = translator.translate(word, dest='ru').text
        word_definition_translated = translator.translate(word_definition, dest='ru').text

        print(f"Значение слова: {word_definition} [{word_definition_translated}]")

        user = input(f"Что это за слово? [{word_translated}] ")
        if user.lower() == word.lower():
            print("Ответ верный!")
        else:
            print(f"Ответ неверный, правильный ответ - {word} [{word_translated}]!")
        play_again = input("Хотите продолжить? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break



if __name__ == "__main__":
    word_game()
