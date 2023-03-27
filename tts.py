from gtts import gTTS

if __name__ == "__main__":


    word = ''
    word = input(word)
    language = 'en'
    myobj = gTTS(text=word, lang=language, slow=True)

    myobj.save(f'./computer_voice_input/{word}.wav')





    