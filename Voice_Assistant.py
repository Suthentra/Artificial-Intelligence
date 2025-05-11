from flask import Flask, render_template, jsonify, request
import speech_recognition as sr
from gtts import gTTS
import winsound
from pydub import AudioSegment
import pyautogui
import webbrowser
import os

app = Flask(__name__)

tasks = []
listeningToTask = False

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    winsound.PlaySound("response.wav", winsound.SND_FILENAME)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listen', methods=['POST'])
def listen():
    command = listen_for_command()
    if command:
        return jsonify({'response': command})
    else:
        return jsonify({'response': "Sorry, I could not understand that."})

@app.route('/respond', methods=['POST'])
def respond_to_command():
    command = request.form['command']
    triggerKeyword = "bologna"

    global tasks
    global listeningToTask

    if triggerKeyword in command:
        if listeningToTask:
            tasks.append(command)
            listeningToTask = False
            response_text = "Adding " + command + " to your task list. You have " + str(len(tasks)) + " tasks currently."
        elif "add a task" in command:
            listeningToTask = True
            response_text = "Sure, what is the task?"
        elif "list tasks" in command:
            response_text = "Your tasks are: " + ', '.join(tasks)
        elif "take a screenshot" in command:
            pyautogui.screenshot("screenshot.png")
            response_text = "I took a screenshot for you."
        elif "open chrome" in command:
            webbrowser.open("http://www.youtube.com")
            response_text = "Opening Chrome."
        elif "exit" in command:
            response_text = "Goodbye!"
            return jsonify({'response': response_text})
        else:
            response_text = "Sorry, I didn't understand that command."
    else:
        response_text = "Please trigger the assistant with the keyword."

    respond(response_text)
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
