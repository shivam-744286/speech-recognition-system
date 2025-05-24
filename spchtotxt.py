import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now: ")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print(f"you said: {text}")
except sr.UnknownValueError:
    print("not audible / audio not clear")
except sr.RequestError as e:
    print(f"error making request: {e}")
