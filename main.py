import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
from pydub import AudioSegment


engine = pyttsx3.init()
voices = engine.getProperty('voices')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.adjust_for_ambient_noise(source)
        voice = r.listen(source)
        try:
            # command = listener.recognize_google(voice)
            if language == 'en':
                engine.setProperty('voice', voices[1].id)
                command = r.recognize_google(voice, language='en-US')
            elif language == 'id':
                engine.setProperty('lang', 'id')
                command = r.recognize_google(voice, language='id-ID')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
        except sr.UnknownValueError:
            command = ''
        return command


def run_alexa():
    global language
    language = 'en'  # default language
    while True:
        command = take_command()
        print(command)
        if 'ubah bahasa ke bahasa inggris' in command:
            talk('Language changed to English')
            language = 'en'
        elif 'change language to bahasa indonesia' in command:
            talk('Bahasa diubah menjadi Bahasa Indonesia')
            language = 'id'
        elif 'stop' in command or 'exit' in command or 'berhenti' in command:
            talk('Goodbye!')
            exit()
        elif language == 'en':
            if 'are you listening' in command:
                talk('Yes, I am listening to you')
            elif 'hello' in command or 'hi' in command:
                talk('Hello, How may I help you?')
            elif 'how are you' in command:
                talk('I am good today. How are you')
            elif 'who are you' in command:
                talk('I am a voice assistant created by Nafa')
            elif 'what is this program created for' in command:
                talk(
                    'This program is created for fulfilling Multimedia Syste practice midterm exam by Mr. Insan')
            elif 'play' in command:
                song = command.replace('play', '')
                talk('playing' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%H:%M')
                print(time)
                talk('Current time is ' + time)
            elif 'who' in command:
                person = command.replace('who', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'compress' in command:
                talk('Please insert an audio mp3 file!')
                # Input file audio
                file_input = input("Enter the audio file name: ")
                file_size_input = os.path.getsize(file_input)

                # Mengubah nama file output
                file_output = os.path.splitext(
                    file_input)[0] + "_compressed.mp3"

                # Load file audio
                sound = AudioSegment.from_file(file_input)

                # Mengubah bitrate
                sound.export(file_output, format="mp3", bitrate="64k")
                file_size_output = os.path.getsize(file_output)

                # Menampilkan ukuran file awal
                print(f"The original size: {file_size_input} bytes")
                talk('The original size of the file is ' +
                     str(file_size_input) + ' bytes')

                # Menampilkan ukuran file yang telah dikompresi
                print(
                    f"The compressed size: {file_size_output} bytes")
                talk('The compressed size of the file is ' +
                     str(file_size_output) + ' bytes')
            elif 'thank you' in command:
                talk(
                    'It was my pleasure to assist you.')
            else:
                talk('Please say the command again.')
        elif language == 'id':
            if 'dengar' in command:
                talk('Ya, saya sedang mendengarkan')
            elif 'halo' in command or 'hai' in command:
                talk('Halo, Ada yang bisa saya bantu?')
            elif 'apa kabar' in command:
                talk('Baik. Bagaimana denganmu')
            elif 'kamu siapa' in command:
                talk('Saya adalah asisten suara yang dibuat oleh Nafa')
            elif 'program ini dibuat untuk' in command:
                talk(
                    'Program ini dibuat untuk memenuhi ujian tengah semester praktikum sistem multimedia oleh Pak Insan')
            elif 'mainkan' in command:
                song = command.replace('mainkan', '')
                talk(song + 'dimainkan')
                pywhatkit.playonyt(song)
            elif 'jam' in command:
                time = datetime.datetime.now().strftime('%H:%M')
                print(time)
                talk('Sekarang jam ' + time)
            elif 'siapa' in command:
                person = command.replace('siapa', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'kompres' in command:
                talk('Tolong sisipkan audio mp3!')
                # Input file audio
                file_input = input("Masukkan nama file audio: ")
                file_size_input = os.path.getsize(file_input)

                # Mengubah nama file output
                file_output = os.path.splitext(
                    file_input)[0] + "_compressed.mp3"

                # Load file audio
                sound = AudioSegment.from_file(file_input)

                # Mengubah bitrate
                sound.export(file_output, format="mp3", bitrate="64k")
                file_size_output = os.path.getsize(file_output)

                # Menampilkan ukuran file awal
                print(f"Ukuran file awal: {file_size_input} bytes")
                talk('Ukuran file awal adalah ' +
                     str(file_size_input) + ' byte')

                # Menampilkan ukuran file yang telah dikompresi
                print(
                    f"Ukuran file setelah dikompresi: {file_size_output} bytes")
                talk('Ukuran file setelah dikompresi adalah ' +
                     str(file_size_output) + ' byte')
            elif 'terima kasih' in command:
                talk(
                    'Dengan senang hati saya membantu Anda.')
            else:
                talk('Tolong ulangi perintahnya.')


run_alexa()
