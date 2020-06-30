from google.cloud import translate_v2 as translate
import six

translate_client = translate.Client()

with open('../data/langlist.txt') as f:
    langs = f.read().strip().split('\n')
    
typ = "female_probes"
with open('../data/' + typ + '.txt') as f:
    text = f.read().strip().split('\n')

if isinstance(text, six.binary_type):
    text = text.decode('utf-8')


for lang in langs:
    print(lang)
    with open('../data/' + typ + '/' + lang + '.txt', 'w', encoding="utf-8") as f:
        result = translate_client.translate(
            text, target_language=lang)

        for word in result:
            f.write(word['translatedText']+'\n')

