from googletrans import Translator

with open('../data/langlist.txt') as f:
    langs = f.read().strip().split('\n')

typ = "personality"

with open('../data/' + typ + '.txt') as f:
    data = f.read().strip().split('\n')


translator = Translator()

for lang in langs:
    print(lang)
    with open('../data/' + typ + '/' + lang + '.txt', 'w', encoding="utf-8") as f:
        translations = translator.translate(data, dest=lang)
        for translation in translations:
            f.write(translation.text + '\n')
