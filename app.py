from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Define the path to the data directory
data_dir = os.path.join(os.path.dirname(__file__), 'stat')

# Serve files from the data directory based on city name
@app.route('/stat/<city>_maxt.txt')
def serve_max_temperature(city):
    filename = f'{city}_maxt.txt'
    return send_from_directory(data_dir, filename)

# Serve files from the data directory based on city name for min temperature
@app.route('/stat/<city>_mint.txt')
def serve_min_temperature(city):
    filename = f'{city}_mint.txt'
    return send_from_directory(data_dir, filename)

# Serve files from the data directory based on city name for rainfall
@app.route('/stat/<city>_rainfall.txt')
def serve_rainfall(city):
    filename = f'{city}_rainfall.txt'
    return send_from_directory(data_dir, filename)
@app.route('/wcrglogo.png')
def logo():
       return send_from_directory('templates', 'wcrglogo.png')


# Define the directory path where images are stored
# img_dir = os.path.join(os.path.dirname(__file__), 'images')

# Route to serve images based on dynamic URL pattern
@app.route('/images/<year>_<month>_<parameter>_<domain>.png')
def images(year, month, parameter, domain):
    img_name = f'{year}_{month}_{parameter}_{domain}.png'
    return send_from_directory('static/images', img_name)




# Render the index.html template
@app.route('/')
def index():
    return render_template('index (2).html')

# Render the fetchb.html template when the view cities button is clicked

@app.route('/map.html')
def viewCities():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)
