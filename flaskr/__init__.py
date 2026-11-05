import os
import sys
from pathlib import Path
from flask import Flask, render_template, request, send_from_directory

# 1. Add the root directory (Cache-me-if-you-can) to Python's search path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# 2. Now Python can successfully find visualize_route in the root folder
from .visualize_route import generate_route_map
from config import DATA_DIR

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'coolroute.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # --- ROUTES FOR COOLROUTE ---
    @app.route('/')
    def index():
        return render_template('index.html', map_generated=False)

    @app.route('/generate-route', methods=['POST'])
    def generate_route():
        try:
            start_lat = float(request.form['start_lat'])
            start_lon = float(request.form['start_lon'])
            end_lat = float(request.form['end_lat'])
            end_lon = float(request.form['end_lon'])

            
            # Run your ML/OSMnx spatial pipeline
            generate_route_map(start_lat, start_lon, end_lat, end_lon)
            
            return render_template('index.html', map_generated=True)
        except Exception as e:
            return f"<h3>Error generating route: {e}</h3><p><a href='/'>Go Back</a></p>"

    @app.route('/map')
    def static_map():
        return send_from_directory(str(DATA_DIR), "route_comparison.html")

    return app