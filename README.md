# 🌟 Personal Website

[![Version](https://img.shields.io/badge/version-v0.9-blue.svg)](https://github.com/yourusername/PersonalWebsite)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/flask-2.0+-red.svg)](https://flask.palletsprojects.com/)
[![PyWebIO](https://img.shields.io/badge/pywebio-1.8+-orange.svg)](https://pywebio.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> A modern, interactive personal website built with Flask and PyWebIO, featuring user authentication, AI-powered content generation, and real-time analytics.

## ✨ Features

- 🔐 **Secure Authentication** - User registration and login system with bcrypt password hashing
- 🤖 **AI-Powered Quotes** - Dynamic quote generation using AI APIs with multiple styles and themes
- 📊 **Real-time Analytics** - Built-in statistics tracking and dashboard
- 🎨 **Modern UI** - Clean, responsive interface powered by PyWebIO
- 🗄️ **Lightweight Database** - TinyDB for simple, file-based data storage
- 🚀 **Easy Deployment** - Flask-based architecture ready for production

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/PersonalWebsite.git
   cd PersonalWebsite
   ```

2. **Install dependencies**
   ```bash
   pip install -r new_site/requirements.txt
   ```

3. **Run the application**
   ```bash
   python new_site/run.py
   ```

4. **Access your website**
   
   Open your browser and navigate to `http://localhost:8080`

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Flask | Web framework and API endpoints |
| **Frontend** | PyWebIO | Interactive web interface |
| **Database** | TinyDB | Lightweight JSON-based storage |
| **Authentication** | bcrypt | Secure password hashing |
| **AI Integration** | Custom API | Dynamic content generation |
| **Styling** | Minty Theme | Bootstrap-based UI theme |

## 📁 Project Structure

```
PersonalWebsite/
├── new_site/
│   ├── AI.py              # AI quote generation system
│   ├── app.py             # Flask application setup
│   ├── auth.py            # User authentication logic
│   ├── main.py            # Main application entry point
│   ├── run.py             # Simple runner script
│   ├── utils.py           # Utility functions and dashboard
│   ├── requirements.txt   # Python dependencies
│   ├── stats.json         # Statistics database
│   └── users.json         # User database
└── README.md
```

## 🔧 Configuration

### Environment Setup

The application uses sensible defaults but can be customized:

- **Host**: `0.0.0.0` (accessible from any IP)
- **Port**: `8080`
- **Debug Mode**: Enabled in development
- **Theme**: Minty (Bootstrap-based)

### Database Files

- `users.json` - Stores user accounts and authentication data
- `stats.json` - Tracks application usage statistics

## 📱 Usage

### For Users

1. **Sign Up**: Create a new account with username and password
2. **Login**: Access your personal dashboard
3. **Dashboard**: View statistics and interact with AI features
4. **AI Quotes**: Generate motivational and inspirational quotes

### For Developers

```python
# Import the main app
from new_site.main import app

# Run in development mode
app.run(debug=True)

# Access API endpoints
# GET /health - Health check
# GET /api/stats - Statistics data
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET/POST | Main application interface |
| `/health` | GET | Health check endpoint |
| `/api/stats` | GET | Retrieve application statistics |

## 🛡️ Security Features

- ✅ Password hashing with bcrypt
- ✅ Session management
- ✅ Input validation and sanitization
- ✅ Secure database operations
- ✅ Protection against common web vulnerabilities

## 📊 Statistics & Analytics

The application tracks:
- User login attempts and successes
- Feature usage patterns
- System performance metrics
- Custom application events

## 🚢 Deployment

### Development
```bash
python new_site/run.py
```

### Production
```bash
# Using Gunicorn (recommended)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 new_site.main:app

# Using Docker (if Dockerfile exists)
docker build -t personal-website .
docker run -p 8080:8080 personal-website
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Roadmap

- [ ] **v1.0** - OAuth integration (Google, GitHub)
- [ ] **v1.1** - Advanced AI features and chat functionality
- [ ] **v1.2** - Mobile app companion
- [ ] **v1.3** - Multi-language support
- [ ] **v1.4** - Advanced analytics dashboard
- [ ] **v1.5** - Plugin system for extensibility

## 🐛 Known Issues

- AI quote generation requires external API connectivity
- TinyDB is suitable for development; consider PostgreSQL for production
- Session persistence across server restarts needs improvement

## ⚙️ Requirements

```txt
pywebio>=1.8.0
pywebio[flask]
flask>=2.0.0
tinydb>=4.8.0
bcrypt>=4.0.0
requests>=2.28.0
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Website: [your-website.com](https://your-website.com)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [PyWebIO](https://pywebio.readthedocs.io/) for the amazing web interface framework
- [Flask](https://flask.palletsprojects.com/) for the robust web framework
- [TinyDB](https://tinydb.readthedocs.io/) for the lightweight database solution
- The open-source community for inspiration and contributions

---

<div align="center">

**[⭐ Star this repo](https://github.com/yourusername/PersonalWebsite)** if you found it helpful!

Made with ❤️ and Python

</div>
