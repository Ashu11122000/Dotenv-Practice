# DOTENV overview
DOTENV (using the python-dotenv package) lets store sensitive data in a .env file and load it into python app as environment variables.

# Why DOTENV is important?
1. Security
   * Keeps secrets (API keys, passwords) out of source code
   * Prevents accidental leaks on GitHub

2. Clean Code
   * No hardcoded values
   * Code becomes reuseable and flexible

3. Environment Management
   * Have different configurations like .env for development and .env.production for production.
# Dotenv Practice (Python)
This task demonstrates how to securely manage environment variables in Python using the python-dotenv package.

---

## Objective
The goal of this assignment is to:
 * Install and use `python-dotenv`
 * Store sensitive data in a `.env` file
 * Load environment variables securely in Python
 * Prevent secrets from being pushed to GitHub using `.gitignore`

---

## Project Structure

dotenv-practice/
│
├── test.py            # Main Python script
├── .env               # Environment variables (ignored in Git)
├── .gitignore         # Ignore sensitive files
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation


## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Ashu11122000/Dotenv-Practice.git
cd Dotenv-Practice
```

---

### 2. Create virtual environment
```bash
python -m venv venv
```

Activate it:
```bash
.\venv\Scripts\activate
```

---

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Environment Variables
Create a `.env` file in the root directory:
```
API_KEY=your_api_key_here
SECRET_PASSWORD=your_password_here
```
 * This file is ignored using `.gitignore` to keep secrets safe.

---

## Running the Project
```bash
python test.py
```

### ✅ Expected Output

```
API KEY: your_api_key_here
PASSWORD: your_password_here
```

---

## Code Explanation
What actually happens:
 * .env file → read by`load_dotenv()` → Loads variables from `.env` file
 * Values → loaded into OS environment
 * `os.getenv()` → Accesses environment variables (fetches environment variables)
 * Keeps sensitive data outside source code

---

## .gitignore

The following files are ignored:
```
.env
venv/
__pycache__/
```
This ensures:
 * No secrets are uploaded
 * Virtual environment is not tracked

---

## Key Learnings
 * Secure handling of API keys and passwords
 * Separation of configuration from code
 * Best practices for real-world Python projects

---

## Future Improvements
 * Use `pydantic-settings` for advanced configuration
 * Integrate with FastAPI
 * Add environment-specific configs (dev, prod)

