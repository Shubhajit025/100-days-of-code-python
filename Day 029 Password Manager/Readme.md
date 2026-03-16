# Day 029: Password Manager

A simple yet powerful **desktop Password Manager** built with Python and Tkinter — Day 29 of my 100 Days of Code challenge!

---

## About The Project

Password Manager is a GUI-based password manager that lets you store, generate, and manage your website credentials — all saved locally on your machine.

---

## Features

- **Random Password Generator** — generates strong passwords with a mix of letters, numbers, and symbols
- **Auto Copy to Clipboard** — generated password is instantly copied using `pyperclip`
- **Save Credentials** — stores website, email/username, and password to a local `data.txt` file
- **Confirmation Dialog** — asks before saving so you never store anything by accident
- **Input Validation** — alerts you if any field is left empty
- **Clean GUI** — built with Tkinter, featuring with a logo


---

## What I Learned

- How to build a **multi-widget Tkinter GUI** using grid layout
- Using **Canvas** to display images inside a Tkinter window
- Writing and appending data to a **local `.txt` file** in Python
- Using **`pyperclip`** to copy text to the system clipboard programmatically and also learned about `.join()` method to join many strings
- Implementing **`messagebox`** for both info alerts and OK/Cancel confirmations
- Generating **secure random passwords** by combining shuffled character lists
- Pre-filling Entry fields with **`.insert()`** for a better UX
