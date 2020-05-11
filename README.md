# What is Music Genre Recommender?
Music Genre Recommender is an expert system that recommends music genre. It is written in Python3 using PySide2 (the Qt5 python bindings) for GUI.
It takes you through a set of questions and based on your answers it suggest a music genre.
## Below are some screens of the GUI
[![MainWindow](./images/MainWindow.jpg "MainWindow")]
[![Questions](./images/Questions.jpg "Questions")]
[![Result](./images/Result.jpg "Result")]

# How to run?
## Create an environment and install requirements: 
``python3 -m venv /path/to/new/virtual/environment``

Activate environment then install requirements.

``pip install -r requirements.txt``

### 1. Use PyInstaller to create an executable file (sh/exe):
``pyinstaller Main.py``

Then go to /build/Main and run the Main.sh/Main.exe

### 2. Run Main.py from terminal/cmd by:
``python3 Main.py``