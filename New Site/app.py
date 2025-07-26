from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import config
import utils

app = Flask(__name__)

@config.config(theme="minty")
def main():
    """Main PyWebIO application function"""
    utils.main_menu()

# Add the PyWebIO view to Flask
app.add_url_rule('/', 'webio_view', webio_view(main), methods=['GET', 'POST', 'OPTIONS'])

# Optional: Add a health check endpoint
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'message': 'Personal Website is running'}, 200

# Optional: Add API endpoints if needed in the future
@app.route('/api/stats')
def get_stats():
    """API endpoint to get stats data"""
    import tinydb
    stats = tinydb.TinyDB('stats.json')
    return {'stats': stats.all()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
