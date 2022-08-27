## Background

My gooooood🐷 friend wants to programmatically send Whatsapp to a bunch of people. He tried VBA but faced many constraints. I turn to Python for some breakthrough. :D

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

2. Download zip version of this directory and unzip, or if you have a Github account, use `git clone git@github.com:511234/auto-send-whatsapp.git`

3. Open the project directory. You should be in `.../auto-send-whatsapp`

4. Open terminal on your machine. Go inside /python directory by inputting the following command.

```
cd python
```

5. Install python virtual env if you haven't

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

pip3 install virtualenv
```

6. Create a virtual environment
```
python3 -m venv env
```

7. Enter the virtual environment
```
source env/bin/activate
```

8. Install dependencies
```
pip3 install pyautogui
pip3 install keyboard
pip3 install python-dotenv
```

9. Clone a `.env` from `.env.sample`
```
cp .env.sample .env
```

10. Change environment variables according to your need
```
CUSTOM_GOOGLE_SHEET_ID=8We12J0DX4S1kcSW1p6lS
CUSTOM_GOOGLE_SHEET_NAME=工作表 1
```

11. Run the program
```
python3 main.py
```

## FAQ

Message is shown on Whatsapp Web but pyautogui `click` and `typewrite` are not working.

> It's about mac setting. Go to `System Preferences` > `Security and Privacy` > `Privacy` > `Accessibility` > Enable `Visual Studio Code`, your other IDE or your terminal
