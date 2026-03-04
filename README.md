# CLI Password Generator

## version 1.0.0

A simple command-line password generator that creates secure random passwords using Python’s `secrets` module.

## Features

- Generates cryptographically secure passwords.
- Enforces password length between **20 and 40** characters.
- Optional exclusion of ambiguous characters (`O`, `0`, `o`, `I`, `l`, `1`, `|`).
- Optional copy-to-clipboard support via `pyperclip`.

## Requirements

- Python 3.10+ (3.14 works).
- Dependencies from `requirements.txt`.

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

Run the application:

```bash
python3 app.py
```

You’ll be prompted to:

1. Enter password length (must be between 20 and 40).
2. Choose whether to avoid ambiguous characters.
3. Optionally copy the generated password to your clipboard.

### Example session

```text
How many characteres do you want in your new password? 20
Avoid ambiguous characters (O/0, l/1)? [y/N]: y
hy6J)whzASFNLb@!CL52
Copy password to clipboard? [y/N]: y
Password copied to clipboard.
```

## Project Structure

```text
.
├── app.py
├── test_app.py
├── requirements.txt
└── README.md
```

## Running Tests

This project uses Python's built-in `unittest` framework.

Run all tests:

```bash
python3 -m unittest -v
```

Current tests validate:

- Error when password length input is not numeric.
- Error message + `None` return when length is outside `20-40`.
- Successful password generation with valid length.
- Exclusion of ambiguous characters when requested.
- Alphabet filtering behavior in `build_alphabet(...)`.

## Notes

- If clipboard copy fails, the password is still displayed in the terminal.
- The generator uses `secrets.choice(...)`, which is appropriate for security-sensitive randomness.
