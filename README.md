# Personal Website - Hack Club SoM 2025

![Python](https://img.shields.io/badge/python-v3.12+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v2.0+-green.svg)
![PyWebIO](https://img.shields.io/badge/pywebio-v1.8+-orange.svg)
![License](https://img.shields.io/badge/license-Educational-lightgrey.svg)

A personal website built with Python, Flask, and PyWebIO for Hack Club's Summer of Making 2025. The site includes user authentication, AI quote generation, statistics tracking, and internet speed testing.

**Live Demo:** [https://sandersonfan.pythonanywhere.com](https://sandersonfan.pythonanywhere.com)  
*Note: Demo version has limited functionality*

## What it does

This is a multi-feature web application I built to learn PyWebIO and explore web development with Python. Users can sign up, log in, and access several tools:

- **User Authentication** - Secure registration and login system with password hashing
- **AI Quote Generator** - Generates quotes using Hack Club's AI API with various prompt styles
- **SoM Countdown** - Real-time countdown to the end of Summer of Making 2025
- **Statistics Dashboard** - Tracks user activity and site usage
- **Speed Test** - Tests internet connection speed with progress indicators

The interface uses PyWebIO's tabbed navigation and includes the minty theme for a clean look.

## Tech Stack

- **Backend:** Python 3.12, Flask
- **Frontend:** PyWebIO
- **Database:** TinyDB (JSON-based)
- **Security:** bcrypt for password hashing
- **External APIs:** Hack Club AI API
- **Testing:** speedtest-cli library

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r new_site/requirements.txt`
3. Run: `python new_site/run.py`
4. Visit: `http://localhost:8080`

## Project Structure

```
PersonalWebsite/
├── README.md
└── new_site/
    ├── app.py              # Main Flask app
    ├── main.py             # Alternative entry point
    ├── run.py              # Runner script
    ├── utils.py            # Dashboard and UI logic
    ├── auth.py             # Authentication system
    ├── AI.py               # Quote generation
    ├── wifi_utils.py       # Speed test functionality
    ├── requirements.txt    # Dependencies
    ├── users.json          # User database
    └── stats.json          # Statistics database
```

## Development Notes

I used AI assistance while learning the PyWebIO library, which was new to me. The project helped me understand Python web development beyond just Flask routes - PyWebIO lets you build entire web interfaces using Python functions instead of HTML/CSS/JavaScript.

The authentication system stores user data in JSON files using TinyDB, which works well for a personal project. The AI quote generator connects to Hack Club's API and uses different prompt templates to generate varied responses.

Built for Hack Club's Summer of Making 2025 as a way to explore modern Python web development and AI integration.

## Requirements

```
pywebio>=1.8.0
pywebio[flask]
flask>=2.0.0
tinydb>=4.8.0
bcrypt>=4.0.0
requests>=2.28.0
speedtest>=2.1.3
```
