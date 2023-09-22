import requests as req
from deep_translator import GoogleTranslator


def jok(lang):
    jk = req.get("https://api.codebazan.ir/jok")
    # return f'[ 😂 ] • joke : \n\n' \
    #        f'{jk.text}'
    translator = GoogleTranslator(target=lang)
    texts = ''
    if lang != 'fa':
        texts = translator.translate(jk.text)
    if lang == 'fa':
        texts = jk.text
    return f'[ 😂 ] • joke : \n\n' \
           f'{texts}'
