#!/usr/bin/env python3
"""
Simple runner script for the Personal Website Flask app
Usage: python run.py
"""

from new_site.main import app

if __name__ == '__main__':
    print("Starting Personal Website Flask App...")
    print("Access your app at: http://localhost:8080")
    print("Health check available at: http://localhost:8080/health")
    print("API stats endpoint: http://localhost:8080/api/stats")
    app.run(host='0.0.0.0', port=8080, debug=True)
