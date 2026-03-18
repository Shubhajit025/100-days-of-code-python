## Day 30 - Password Manager Modified with Json

> **100 Days of Code – Day 30**
> A fully functional desktop Password Manager built with Python and Tkinter.

---

## What I Built

A **GUI-based Password Manager** called **Password Manager** that lets you:

- Generate strong random passwords
- Save credentials (website, email, password) to a local JSON file
- Search and retrieve saved credentials instantly
- Auto-copy generated passwords to clipboard

---

## What I Learned

### File Handling with JSON
- Reading from a JSON file using `json.load()`
- Writing/updating data with `json.dump()` and `indent=4` for readability
- Handling `FileNotFoundError` with `try/except/else` blocks
- **Update pattern** — load existing data → update with new entry → write back:
```python
  data.update(new_data)
```
- Using `.title()` on website names for consistent key formatting

### Search Functionality
- Looking up saved passwords by website name from the JSON store
- Handling `KeyError` when a website isn't found
- Displaying results with `messagebox.showinfo()`

### Modules Used
| Module | Purpose |
|--------|---------|
| `tkinter` | GUI framework |
| `random` | Password generation |
| `pyperclip` | Clipboard copy |
| `json` | Persistent data storage |

---

## Project Structure
```
day30-password-manager/
│
├── main.py         # Main application logic
├── data.json       # Saved credentials (auto-created)
└── logo.png        # App logo
```

---

## Sample `data.json`
```json (*Note: This email or password is just for testing and randomly generated, not even exsist from my side.)
{
    "Facebook": {
        "email": "indie@gmail.com",
        "password": "L#Nq42J!Em6!Ub"
    }
}
```
