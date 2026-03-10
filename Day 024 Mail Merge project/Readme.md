# Mail Merge Project (Day 24)

This project is part of the 100 Days of Code: Python Bootcamp by Dr. Angela Yu.

The goal of this project is to automatically generate personalized letters for multiple recipients using Python. Instead of manually writing the same letter multiple times, the program reads a list of names and inserts each name into a template letter.

## Features
- Reads a list of names from a text file
- Uses a template letter
- Replaces placeholders with actual names
- Generates personalized letters automatically
- Saves each generated letter as a new file

## Project Structure

Mail-Merge-Project
│
├── Input
│   ├── Letters
│   │   └── starting_letter.txt
│   │
│   └── Names
│       └── invited_names.txt
│
├── Output
│   └── ReadyToSend
│
└── main.py

## How It Works

1. The program reads names from invited_names.txt.
2. It opens the template letter starting_letter.txt.
3. The placeholder [name] inside the letter is replaced with each person's name.
4. A new personalized letter is created for every name.
5. The letters are saved in the Output/ReadyToSend folder.


## Concepts Used
- Python file handling
- Reading and writing text files
- String replacement
- Loops
- Basic automation

## Future Improvements
- Add CSV support for large contact lists
- Add automatic email sending
- Build a GUI version of the tool

This project was built while learning Python automation and file handling.

