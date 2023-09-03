# Random India Facts WhatsApp Sender

## Overview

While my partner was on a week-long business trip to India, I decided to write a script that sends him random facts about India. I created a Python script that sends automated WhatsApp messages. 
To accomplish this, I utilized the pywhatkit library and Windows Task Scheduler to automate the task.

## Prerequisites

- Python 3.11.3
- Windows operating system (for Task Scheduler)

## Start

```
pip install -r requirements.txt
```
Create a `secrets_.py` file with the `PHONE_NUMBER` variable containing the recipient's phone number you want to message.

Create a `filename_here.bat` file with the following:

```
@echo off
"path to your venv script\python.exe" "path to your app.py file"
pause
```

This `.bat` file we will use for our Task sheduler

## Set-up Task sheduler
Open Task sheduler

Create a new task.

![image](https://github.com/Anissa3005/automate_text/assets/114712265/5c670025-7677-4f47-8a07-181dd34d839b)

Create new action

![image](https://github.com/Anissa3005/automate_text/assets/114712265/6d01763a-d6e8-4800-b396-d342fc74a735)

Add the Python Executable File to the Program Script

![image](https://github.com/Anissa3005/automate_text/assets/114712265/1c3e4985-a0e4-436c-a298-f00b18e17501)

Add the path to your `filename.bat` in argument

![image](https://github.com/Anissa3005/automate_text/assets/114712265/774590ec-7101-4ffd-b110-70f8a6ea7076)

All that is left is adding a trigger, when do you want to run the script

![image](https://github.com/Anissa3005/automate_text/assets/114712265/2ce0b2c2-63be-4090-b8ea-af0d76f55a99)


🎉🎉🎉 Now you can automate messages with random facts about India. 🎉🎉🎉


