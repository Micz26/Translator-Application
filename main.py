import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

def main():
    print("Hello, welcome to the translator. Translator supports: ")
    print("1. Arabic\n2. German\n3. English\n4. Spanish\n5. French\n6. Hebrew\n7. Japanese\n8. Dutch\n9. Polish\n10. Portuguese\n11. Romanian\n12. Russian\n13. Turkish")
    user_lang = input('Type the number of your language: ')
    trans_lang = input("Type the number of a language you want to translate to or '0' to translate to all languages: ")
    word = input("Type the word you want to translate:")
    lang_dict = {
        "1" : "arabic",
        "2" : "german",
        "3" : "english",
        "4" : "spanish",
        "5" : "french",
        "6" : "hebrew",
        "7" : "japanese",
        "8" : "dutch",
        '9' : "polish",
        "10" : "portuguese",
        "11" : "romanian",
        "12" : "russian",
        "13" : "turkish"
    }
    filename = word + ".txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.close()
    if trans_lang == "0":
        for key, val in lang_dict.items():
            translation = f"{lang_dict[user_lang]}-{lang_dict[key]}"
            url = f'https://context.reverso.net/translation/{translation}/{word}'
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            translations = soup.find_all('span', {'class': 'display-term'})
            words = []
            for translation in translations:
                    words.append(translation.text.split()[0])
            print(f"{lang_dict[key]} translations:")
            print("\n".join(words))
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"{lang_dict[key]} translations:\n")
                file.write("\n".join(words))
            sections = soup.find_all('section', {'id': 'examples-content'})
            sentences = []
            for section in sections:
                examples = section.find_all('span', {'class': 'text'})
                for example in examples:
                    sentences.append(example.text.strip())
            print(f"{lang_dict[key]} examples:\n")
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"\n\n{lang_dict[key]} examples:\n")
            for i, sentence in enumerate(sentences):
                separator = '\n' * (1 + (i % 2))
                print(sentence + separator)
                with open(filename, "a") as file:
                    file.write(sentence + separator)
    else:
        translation = f"{lang_dict[user_lang]}-{lang_dict[trans_lang]}"
        url = f'https://context.reverso.net/translation/{translation}/{word}'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        translations = soup.find_all('span', {'class': 'display-term'})
        words = []
        with open(filename, "w", encoding="utf-8") as file:
            for translation in translations:
                words.append(translation.text.split()[0])
                file.write(translation.text.split()[0])
        print(*words, sep='\n')
        with open(filename, "a", encoding="utf-8") as file:
            file.write(*words)
        sections = soup.find_all('section', {'id': 'examples-content'})
        sentences = []
        for section in sections:
            examples = section.find_all('span', {'class': 'text'})
            for example in examples:
                sentences.append(example.text.strip())
        print(f"\n{lang_dict[trans_lang]} examples:")
        for i, sentence in enumerate(sentences):
            separator = '\n' * (1 + (i % 2))
            print(sentence, end=separator)
            with open(filename, "a", encoding="utf-8") as file:
                file.write(sentence)
    file.close()

if __name__ == "__main__":
    main()
