from googletrans import Translator, LANGUAGES

translator = Translator()

NAME_TO_CODE = {name.lower(): code for code, name in LANGUAGES.items()}
CODE_TO_NAME = {code: name for code, name in LANGUAGES.items()}


def CodeLang(lang):
    lang_lower = lang.lower()
    if lang_lower in CODE_TO_NAME:
        return CODE_TO_NAME[lang_lower].capitalize()
    if lang_lower in NAME_TO_CODE:
        return NAME_TO_CODE[lang_lower]
    return f"Мову '{lang}' не знайдено."


def LangDetect(txt):
    detected = translator.detect(txt)
    return f"Detected(lang={detected.lang}, confidence={detected.confidence})"


def TransLate(text, lang):
    lang_lower = lang.lower()
    if lang_lower in CODE_TO_NAME:
        code = lang_lower
    elif lang_lower in NAME_TO_CODE:
        code = NAME_TO_CODE[lang_lower]
    else:
        return f"Мову '{lang}' не знайдено."
    result = translator.translate(text, dest=code)
    return result.text


print("Програма для перекладу тексту")
print("Введіть 'вихід' щоб завершити")
print()

while True:
    text = input("Введіть текст: ")
    if text.lower() == "вихід":
        print("До побачення!")
        break

    lang = input("На яку мову перекласти (наприклад: en або English): ")

    print(f"Мова оригіналу: {LangDetect(text)}")
    print(f"Переклад: {TransLate(text, lang)}")
    print()