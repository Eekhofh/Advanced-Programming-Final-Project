PROGRAM DESCRIPTION
_______________________________________________________________________

The goal of the program(s) in this Github repository is to align the script and the subtitles of the movie 'Mission Impossible'. It labels every line of the script and adds character names and timestamps. The degree to which (in percentages) the script and the subtitles match is also displayed. The repository contains a web-based Graphical User Interface, which allows the user to easily make use of the program(s). For results, the user can choose between either a JSON or a CSV format. The way in which the programs work is described in their comments. 

_______________________________________________________________________

HOW TO USE
_______________________________________________________________________

Here is a short overview on how to use the program.

1) Load the web page by running app.py in the command-line. `sudo python3 app.py`
2) Upload a script .srt file and a script .txt file and submit both.
3) Select desired output (.csv or .json)
4) The program will now process the scripts.
5) You will now see a percentage of how much both files matched.
6) Download the desired output-file with the download-button.

Pytest:
1) Go into the unit_tests folder.
2) Run the pytest command.
* Some pycodestyle requirements were ignored, because of errors.

_______________________________________________________________________

DIVISION OF TASKS
_______________________________________________________________________

Rijck: Added the character name for each subtitle, based on the script.
Rijck: Added the timestamp to matching line of the script (if any).
Hessel: Labeled each line of the script with correct label.
Hessel: Summmarized differences between script/subtitles.
Louis: Made a user interface using Flask.
Joey: Output result to JSON and CSV format.
Joey: Created unit tests.

_______________________________________________________________________

TEAM
_______________________________________________________________________

N.R. Dijksterhuis - S2878739
Hessel Eekhof - S3398641
Joey Mallat - S4483081
Louis Speelman - S4364473
