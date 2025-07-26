from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import config
import new_site.utils as utils

app = Flask(__name__)

def main():
    """Main PyWebIO application function"""
    utils.main_menu()

# Add the PyWebIO view to Flask
app.add_url_rule('/', 'webio_view', webio_view(main), methods=['GET', 'POST', 'OPTIONS'])

# Optional: Add a health check endpoint
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'message': 'Personal Website is running'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
