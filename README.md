COMPANY: CODTECH IT SOLUTIONS

NAME: SHIVAM KUMAR

Intern id: CT04DN1277

DOMAIN: Artificial Intelligence

DURATION: 4 weeks

MENTOR: NEELA SANTOSH

This project is done using Visual Studio Code (VS Code).  It's available for Windows, macOS, and Linux, and also has a web version. VS Code is a source code editor that combines developer tooling, a frictionless edit-build-debug cycle, and a rich ecosystem of extensions'



note: need a stable internet connection as it uses google's recognition system

This project is made using following steps:

We import the speech_recognition library and give it a shortcut name sr for convenience.

This creates an instance of the Recognizer class which helps convert speech to text.

This opens the microphone and assigns it to a variable named source. The program will listen to the user's speech from this microphone.

It prompts the user to speak and listens to the audio input until a pause is detected.

The recognize_google() method sends the audio to Google’s servers and gets back the transcribed text, which is printed to the console.

If the speech is unclear or can't be understood, it shows an appropriate message.

If there's a problem connecting to the Google API (like no internet), it prints the error.
