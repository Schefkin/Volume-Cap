# Volume Cap

Table of Contents
1. [Download](#1-download)
2. [Introduction](#2-introduction)
3. [Features](#3-features)
4. [Note](#4-note) 

<hr style="height:4px; background-color:#3d444d; border:none;" />

🏡 Website : maybe I'll make it later

## 1. Download

### Step 1: Install the app
[Download for Windows](https://github.com/Schefkin/Volume-Cap/releases/download/v1.0.0/Volume_Cap.exe)

Choose any desired location.


### Step 2: Add app to Startup
Press `Win + R`, type `shell:startup`, and hit Enter.
Place a shortcut to EXE in that folder.

### Step 3: Add app to Start Menu
Go to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs`. Place an anothor shortcut to EXE in programs folder. You're done!🎉

<hr style="height:4px; background-color:#3d444d; border:none;" />

## 2. Introduction
Volume Cap is a lightweight desktop application that helps protect your ears by limiting the maximum volume output of your PC. 

Designed for users who want to maintain safe listening levels, Volume Cap runs quietly in the background and ensures your system volume never exceeds a healthy threshold.

### How to open the UI?
Search the shortcut name in the Windows search bar (the shortcut is added to the Start Menu, so it’s searchable). 

![Image couldn't load](imgs/Screenshot%202025-03-20%20010959.png)

Right after the first download app is not yet launched, so you need to launch it and then do it one more time for the UI to appear.

![Image couldn't load](imgs/Screenshot%202025-03-20%20011025.png)

After closing UI using X button the app continues to run in the background.

The app can be found from Task Manager under background processes.

<hr style="height:4px; background-color:#3d444d; border:none;" />

## 3. Features
- Set a maximum volume limit for your PC
- Lightweight(5-7MB or ~0.2% of 8gb ram usage)
- Easy to configure with a simple UI
- Auto-start on boot
- Runs silently in the background
- Works with all audio devices and system outputs
- Windows 10/11 supported

<hr style="height:4px; background-color:#3d444d; border:none;" />

## 4. Note
My antivirus said my own software was acting "suspicious", whatever that means (probably because the app creates a .txt file to store the volume cap value between computer sessions; or because it changes system settings-the volume nob; or it looks for the current audio device in use; or because it is a python script running in the background, thus an antivirus might automatically flag it as "suspicious"; whatever the reason, the release version is safe even if antivirus might tell you otherwise). 

If you don't trust the release, you can clone the code and compile it yourself using tools like `PyInstaller`, form  there continue like you would normally with steps 2 and 3.

<hr style="height:4px; background-color:#3d444d; border:none;" />