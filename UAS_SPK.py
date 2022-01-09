from googletrans import Translator
sentence=str(input('say...='))
translator=Translator()
translated_sentence=translator.translate(sentence,src='en',dest='ja')
print(translated_sentence)