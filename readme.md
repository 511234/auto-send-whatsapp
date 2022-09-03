## Background

My gooooood🐷 friend wants to programmatically send Whatsapp to a bunch of people. He tried VBA but faced many constraints. I turn to Python for breakthrough. :D 🐷🍄

## Description

Using Python, read contact info from Google Sheet and send custom Whatsapp messages to recipients through Whatsapp Web.

## Pre-requisites:

1. Login Whatsapp onto your default browser
2. Prepare a Google Sheet with privacy set as public and have a column for `phone` / `Phone` / `電話`. Please also include a custom message column called `message` / `Message` / `訊息`
3. Check FAQ if you are using Mac OS

## Steps to use:

1. Install python if you haven't

```
Windows:
https://www.python.org/downloads/release/python-3106/
Mac:
https://www.python.org/downloads/macos/
Linux:
https://www.python.org/downloads/source/
```

2. Open a github account and set up personal access token.

3. Open terminal. Run
```
git clone git@github.com:511234/auto-send-whatsapp.git
```

4. Run 
```
cd auto-send-whatsapp/python
```

5. Install python virtual env if you haven't (Only need to do once for each computer)

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3 install --upgrade pip

pip3 install virtualenv
```

6. Create a virtual environment

```
python3.10 -m venv venv
```

7. Enter the virtual environment

```
source venv/bin/activate
```

8. Install dependencies

```
pip3 install flask keyboard pyvirtualdisplay pyautogui pandas Xlib
```

9. Run the program

```
python3 -m flask run --port=28311
```

10. Go to website `localhost:28311`
Type in Google Sheet name and Google Sheet link. Hit submit.

## FAQ

Message is shown on Whatsapp Web but pyautogui `click` and `typewrite` are not working.

> It's about mac setting. Go to `System Preferences` > `Security and Privacy` > `Privacy` > `Accessibility` > Enable `Visual Studio Code`, your other IDE or your terminal

Intellisense not working

> Ctrl + shift + p >> Python: Select Interpreter

---

### 🦔 Github workflow

- Add v\* tag to publish a release
- `pip freeze > requirements.txt` to export existing packages

---

### 🦔 Deploy to server?

https://github.com/asweigart/pyautogui/issues/632  
https://www.pythonanywhere.com/forums/topic/28076/

`docker-compose up --build` > Can access `localhost:28311` but not opening Web and controlling GUI

---

### 🦔 Changing VS Code Python Interpreter

```
Command + ,

Python: Venv Path
Path to folder with a list of Virtual Environments (e.g. ~/.pyenv, ~/Envs, ~/.virtualenvs).

~/python/venv, ~/python/env
```

Then

```
Command + Shift + P
Python: Select Interpreter
./python/venv/bin/python
```
