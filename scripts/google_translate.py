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
            translated_text = word['translatedText']
            first_brack = translated_text.find('[')
            second_brack = translated_text.find(']')
            if(first_brack == second_brack):
                continue
            translated_text = translated_text.replace(translated_text[first_brack+1:second_brack],"MASK")
            f.write(translated_text+'\n')

