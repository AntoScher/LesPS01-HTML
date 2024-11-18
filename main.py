import requests
from bs4 import BeautifulSoup



def get_english_words():
    url="https://randomword.com/"
    try:
        response=requests.get(url)
        soup=BeautifulSoup(response.content, "html.parser")
        english_words=soup.find("div",id="random_word").text.strip()
        word_definition=soup.find("div",id="random_word_definition").text.strip()

        return{
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка при получении данных с сайта.")
       # return None

def word_game():
    print("Игра начинается!")
    while True:
        word_dict=get_english_words()
        word=word_dict.get("english_words")
        word_definition=word_dict.get("word_definition")
        print(f"Значение слова: {word_definition}")

        user=input("Что это за слово?")
        if user==word:
            print("Ответ верный!")
        else:
            print("Ответ неверный, правльный ответ -{word}!")
        play_again=input("хотите продолжить? y/n:")
        if play_again.lower()!="y":
            print("Спасибо за игру!")
            break
        #if word_dict is None:
        #    print("Произошла ошибка при получении данных с сайта.")
        #else:
        #break
    word_game()
        