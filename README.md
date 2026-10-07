# 📊 Insta Audit

A beginner-friendly Python project that analyzes your Instagram followers and following data to find **who you follow but who doesn't follow you back**.

Insta Audit works completely **offline** using your Instagram data export. You don't need to enter your Instagram password or use any third-party Instagram service.

---

## ✨ Features

- 📥 Reads Instagram `followers` and `following` JSON files
- 👥 Counts total followers
- ➡️ Counts total following
- 🔍 Finds people who don't follow you back
- 🔤 Sorts usernames alphabetically
- 📄 Saves the results to `not_following_back.txt`
- 🔒 Works completely offline
- 🚫 No Instagram password required
- 📦 No external Python libraries required

---

## 📥 Getting Your Instagram Data

Before running Insta Audit, download your Instagram **Followers and following** data in **JSON** format.

1. **Open Instagram** and log in to the account you want to analyze.
2. Go to **Settings → Accounts Center**.
3. Open **Your information and permissions → Download your information**.
4. Select the Instagram account you want to analyze.
5. Choose the option to select **specific information**, then pick **Followers and following**.
6. Choose **JSON** as the format (required, because the script reads the data with Python's built-in `json` module).
7. Submit the request. When Instagram finishes preparing it, download the ZIP file and extract it.

> **Note:** Instagram's menu names change over time, so the exact steps may look slightly different in your version of the app.

---

## 📂 Preparing the Data

From the extracted ZIP, copy these two files into the same folder as `main.py`:

```text
followers_1.json
following.json
```

Your project should look like this:

```text
Insta Audit/
│
├── main.py
├── followers_1.json
├── following.json
├── not_following_back.txt   (created after running the script)
├── README.md
├── .gitignore
│
└── screenshots/
    ├── terminal_output.png
    └── result_file.png
```

> ⚠️ **Important:** Do not upload your Instagram JSON files to GitHub. They contain personal account information.

---

## ⚙️ How It Works

```text
Instagram Data Export
        ↓
followers_1.json + following.json
        ↓
Read JSON files
        ↓
Extract usernames into sets
        ↓
following - followers
        ↓
Sort usernames
        ↓
Create not_following_back.txt
```

### 1. Read the JSON files

The program loads both files using Python's built-in `json` module:

```python
import json
```

### 2. Extract usernames

Usernames are stored in Python **sets**, which makes comparison easy and removes duplicates:

```python
followers = {"user1", "user2", "user3"}
following = {"user1", "user2", "user3", "user4", "user5"}
```

### 3. Compare followers and following

The core logic is a single set difference:

```python
not_following_back = following - followers
```

With the example above, the result is `user4` and `user5`: you follow them, but they don't follow you back.

### 4. Sort the results

```python
sorted(not_following_back)
```

Sorting alphabetically makes the output easier to read.

### 5. Create the output file

Finally, the script writes `not_following_back.txt` with your follower count, following count, and the list of accounts that don't follow you back.

---

## ▶️ How to Run

Open the project folder in VS Code or a terminal and run:

```bash
python main.py
```

Example terminal output:

```text
Total followers: 139
Total following: 176
Not following you back: 39
Done! not_following_back.txt file ban gayi.
```

---

## 📄 Output File

The generated `not_following_back.txt` looks like this:

```text
Total followers: 139
Total following: 176

People who don't follow you back:

username_one
username_two
username_three
...
```

Usernames are sorted alphabetically.

---

## 🛠️ Requirements

- Python 3.6 or higher
- An Instagram data export in JSON format
- VS Code or any other code editor / terminal

**No external libraries are needed.** The project only uses Python's built-in `json` module.

---

## 🔒 Privacy

Insta Audit is designed to run locally on your computer.

- ❌ Your data is not uploaded anywhere
- ❌ Your data is not sent to any server
- ❌ Nothing is shared with third-party services
- ❌ No Instagram password is required
- ✅ Everything is processed locally

### Keep your data out of GitHub

Instagram JSON files and the generated results contain personal information. Add this to your `.gitignore`:

```text
followers_*.json
following.json
not_following_back.txt
```

Or, to ignore all JSON files:

```text
*.json
not_following_back.txt
```

> 💡 If you add screenshots to the repo, blur or crop the usernames first, since they belong to real people.

---

## 🧩 Troubleshooting

| Problem | Possible solution |
|---|---|
| `FileNotFoundError` | Make sure `followers_1.json` and `following.json` are in the same folder as `main.py`. |
| `KeyError: 'relationships_following'` | Your export may have a different JSON structure. Open `following.json` and check its structure. |
| Only some followers are counted | Instagram can split followers into `followers_1.json`, `followers_2.json`, etc. Include all of them. |
| Output looks incorrect | Make sure the data was downloaded in **JSON** format, not HTML. |
| Special characters look wrong | Open and write files using UTF-8 encoding. |

---

## 🚀 Future Improvements

- [ ] Automatically detect multiple `followers_*.json` files
- [ ] Find people who follow you but you don't follow back
- [ ] Export results to CSV
- [ ] Add a simple GUI
- [ ] Add command-line arguments
- [ ] Add account statistics
- [ ] Improve compatibility with different Instagram export structures

---

## 🎯 What I Learned

I built Insta Audit to apply basic programming concepts to a real-world problem. Along the way I practiced:

- File handling and writing files
- JSON parsing
- Sets and set difference
- Loops and functions
- Sorting
- Working with real-world exported data

The core idea is one line:

```python
following - followers
```

---

## 💡 Why I Built This

Instead of only practicing Python syntax with small exercises, I wanted to build something that solves a real problem, and keep it simple, offline, and privacy-friendly.

---

## 👨‍💻 Author

**Dilnoor**

Built as a Python learning project while practicing file handling, JSON parsing, sets, and working with real-world data.

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!
