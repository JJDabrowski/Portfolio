# Hello and welcome to RBF Reforged
RBF stands for Remove Big File (however hideous this name wouldn't be). This is a program that allows you to move the largest files in the directory of your choice for inspection and then remove them.

# Requirements
RBF was reforged using Python 3.10.1. You also need venv to start it. As for installing and creating venv, consult this tutorial: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ If it comes to other requirements, use:
python3 -m pip install -r requirements.txt
command on Unix systems.

# Launching the program
After launching venv, navigate to the directory of the version compatibile with your system. Then use:
flask --app RBF_R run