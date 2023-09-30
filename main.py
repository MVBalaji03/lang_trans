import nltk
from googletrans import Translator
nltk.download("punkt")
translator=Translator()
print("1.CONVERTION TO TAMIL")
print("2.CONVERSION TO TELUGU")
print("CONVERSION TO HINDI")
print("COVERSION TO MALAYALAM")
your_choice=int(input("enter your choice"))
if your_choice==1:
    input_text=input("enter the text :")
    detected_lang=translator.detect(input_text).lang
    translator=translator.translator(input_text,dest="ta")
elif your_choice==2:
    input_text = input("enter the text :")
    detected_lang = translator.detect(input_text).lang
    translator = translator.translator(input_text, dest="te")
elif your_choice==3:
    input_text = input("enter the text :")
    detected_lang = translator.detect(input_text).lang
    translator = translator.translator(input_text, dest="hi")
elif your_choice==4:
    input_text = input("enter the text :")
    detected_lang = translator.detect(input_text).lang
    translator = translator.translator(input_text, dest="ma")
else:
    print("choose from 1-4 options")
print("original text({}):{}".format(detected_lang,input_text))
print("translated text (your_choice):{}".format(translated.text))
