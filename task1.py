from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

if __name__ == "__main__":
    input_text = input("Enter text to translate: ")
    target_language = input("Enter target language (e.g., 'en' for English, 'fr' for French): ")
    
    translated_text = translate_text(input_text, target_language)
    print("Translated text:", translated_text)
