from googletrans import Translator

def translate_to_sinhala(text):
    translator = Translator()
    try:
        translated = translator.translate(text, src="en", dest="si")
        return translated.text
    except Exception as e:
        return f"Translation error: {str(e)}"
