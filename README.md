# Python Face Detection 🔍

Face Detection written in Python with OpenCV 2024 💻
Initial method is the classic haarcascades to detect faces. Tested against three types of images (real, AI generated, cartoon).
![app_image](app_image.png)

Output:
Some detection in a real image, completely unable to detect anything in the AI generated image or the cartoon image.

## Requirements 📜

- Python 3.11++
- OpenCV

Optional:

- Bash terminal
- Visual Studio Code

## Setup 🔧

When running this codebase, it was originally coded on a Windows 11 machine with Python 3.12.4 using Visual Studio Code.

You can check your version with: `python --version`

You will want to setup a Python environment in VSC. To do this:

- Ctrl + Shift + P
- Find `Python: Create Environment...`
- Choose `.venv`
- Select interpreter (in this case Python 3.12.4)

If you have any terminals open in Visual Studio Code, you will want to relaunch them to allow the virtual environment to take effect.

## Install dependencies

```
pip install opencv-python
```

## How to Run 🏃

- Open a terminal and cd to the directory that contains app.py
- Run `python app.py`
- Done!

Alternatively:

- Open the `app.py` file in VSC
- Click on the Play button to the top right
- Let VSC work its magic and done!
