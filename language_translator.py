import nltk
from googletrans import Translator
nltk.download("punkt")

translator = Translator()

while True:

    print("                        Select the language to be Translated")
    print("")
    print("--------------------------")

    print("1. Tamil")
    print("2. Telugu")
    print("3. Hindi")
    print("4. Malayalam")
    print("5. Kannada")
    print("6. Exit from the loop")

    print("--------------------------")
    
    your_choice=int(input("enter your choice : "))

    if your_choice>=1 and your_choice<=5:
        input_text = input("enter the text : ")
        detected_lang = translator.detect(input_text).lang

        if your_choice == 1:
            translated = translator.translate(input_text,dest="ta")
        elif your_choice == 2:
            translated = translator.translate(input_text,dest="te")
        elif your_choice == 3:
            translated = translator.translate(input_text,dest="hi")
        elif your_choice == 4:
            translated = translator.translate(input_text,dest="ml")
        else:
            translated = translator.translate(input_text, dest="kn")


        print("original text({}):{}".format(detected_lang,input_text))

        print("translated text ({}):{}".format(translated.dest,translated.text))

    elif your_choice == 6:
        print("Exiting the loop")
        break

    else:
        print("choose from 1-4 options")