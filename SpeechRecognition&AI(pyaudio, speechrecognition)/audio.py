import pyaudio, wave, subprocess
import speech_recognition as sr # sounds record
from commands import Commander

running = True

def say(text):
    subprocess.call('say' + text, shell=True)


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )
    data_stream = wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()
play_audio("./audio/nice-work.wav")

r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print("Listening...")
    play_audio("./audio/nice-work.wav")
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
    
    play_audio("./audio/nice-work.wav")
    command = ""
    try:
        command = r.recognize_google(audio)
    except:
        print("Coludn't understand you. bro")

    print("Your command:")
    print(command)
    if command == ["quit", "exis", "bye", "goodbye"]:
        global running
        running = False
    cmd.discover(command)
    # say('you said: ' + command)

while running == True:
    initSpeech()