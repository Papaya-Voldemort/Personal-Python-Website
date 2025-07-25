# Personal Website

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Python 3.12](https://img.shields.io/badge/tested%20on-python%203.12-brightgreen.svg)
![Version](https://img.shields.io/badge/version-0.2-orange.svg)
![License](https://img.shields.io/badge/license-Personal%20Use-red.svg)

A Python web application built with PyWebIO featuring user authentication, theme customization, and dashboard functionality.

## Version

**Current Version:** 0.2

## Features

- 🔐 User authentication (login/signup)
- 🎨 Live theme switching with Bootswatch themes
- 📊 User dashboard
- ⏰ Countdown timer functionality
- 💾 User data persistence with TinyDB
- 🌐 Web-based interface

## Requirements

- Python 3.8+ (tested on Python 3.12)
- PyWebIO
- TinyDB

## Installation

1. Clone or download the project
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or manually install:
   ```bash
   pip install pywebio tinydb
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Open your browser and navigate to `http://localhost:8080`
3. Create an account or login
4. Explore the dashboard features

## File Structure

```
PersonalWebsite/
├── main.py              # Main application entry point
├── helpers.py           # Helper functions for authentication and dashboard
├── database-managment.py # Database management utilities
├── test.py             # Test file
├── users.json          # User data storage
└── __pycache__/        # Python cache files
```

## Available Themes

- Default (Bootstrap)
- Dark (Darkly)
- Minty
- Yeti
- Sketchy
- Sandstone

## Known Issues

### Version 0.2 Known Bugs

- **Theme Switch Return Issue**: After changing themes in user settings, the application doesn't properly return to the dashboard and remove the theme switch text. This is tracked as a TODO in `helpers.py` line 109.

## Configuration

The application runs on port 8080 by default. You can modify this in `main.py`:

```python
start_server(app, port=8080, cdn=True)
```

## Contributing

Feel free to submit issues and pull requests to improve the application.

## License

This project is for personal use and learning purposes.
