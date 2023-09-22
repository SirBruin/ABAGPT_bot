from deep_translator import GoogleTranslator


def translation(text, first_language, target_language):
    translator = GoogleTranslator(source=first_language, target=target_language)
    translate = translator.translate(text)
    return translate
