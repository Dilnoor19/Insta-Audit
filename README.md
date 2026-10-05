# Instagram Not Following Back Checker

A small Python script that reads your Instagram data export and tells you **who you follow but who doesn't follow you back**. It works fully offline on your own exported files, so you never have to enter your Instagram password or use any third-party app.

## Features

- Reads your Instagram `followers` and `following` JSON files
- Counts total followers and total following
- Finds accounts that don't follow you back
- Saves the result as a sorted (A-Z) list in `not_following_back.txt`

## How It Works

1. Loads both JSON files using Python's built-in `json` module.
2. Stores usernames in two `set`s (fast comparison, no duplicates).
3. Uses set difference: `following - followers` gives everyone you follow who doesn't follow you.
4. Sorts the result alphabetically and writes it to a text file.

## Requirements

- Python 3.6 or higher
- No external libraries needed (only the built-in `json` module)

## Getting Your Instagram Data

1. Open Instagram → **Settings** → **Accounts Center**.
2. Go to **Your information and permissions** → **Download your information**.
3. Choose **Followers and following** as the data to export.
4. Select the format **JSON** and submit the request.
5. Once Instagram emails you the download link, extract the ZIP file.
6. Copy these two files next to the script:
   - `followers_1.json`
   - `following.json`

> Note: Instagram's menu names and export layout can change over time, so the steps above may look slightly different for you.

## Project Structure

```
.
├── script.py               # main script (use your own file name)
├── followers_1.json        # from your Instagram export
├── following.json          # from your Instagram export
└── not_following_back.txt  # generated output
```

## Usage

```bash
python script.py
```

Sample terminal output:

```
Total followers: 320
Total following: 410
Not following you back: 95
Done! not_following_back.txt file ban gayi.
```

## Output File

`not_following_back.txt` looks like this:

```
Total followers: 320
Total following: 410

People who don't follow you back:

username_one
username_two
username_three
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `FileNotFoundError` | Make sure both JSON files are in the same folder as the script, or update the file paths at the top of the script. |
| `KeyError: 'relationships_following'` | Your export may use a different structure. Open `following.json` and check the top-level key name. |
| Followers are split into multiple files (`followers_2.json`, etc.) | Large accounts get several files. Load each one and add the usernames to the same `followers` set. |
| Emojis or special characters look broken | The script already uses `encoding="utf-8"`. Open the output file in an editor that supports UTF-8. |

## Privacy

Everything runs locally on your computer. Your data is never uploaded anywhere. Don't commit your JSON export files to a public GitHub repo, since they contain personal account information. Add them to `.gitignore`:

```
followers_1.json
following.json
not_following_back.txt
```

## Possible Improvements

- Support multiple follower files automatically (`followers_*.json`)
- Also list "fans" (people who follow you but you don't follow back)
- Export results to CSV
- Simple GUI or command-line arguments for file paths

## Author

Made by Dilnoor as a beginner-friendly Python project to practice file handling, JSON parsing and sets.
