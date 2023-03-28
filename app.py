from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('emails.db', check_same_thread=False)
c = conn.cursor()

# Create the emails table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS emails
             (email text)''')


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/submit', methods=['POST'])
# def submit():
#     email = request.form['email']
#     c.execute("INSERT INTO emails VALUES (?)", (email,))
#     conn.commit()
#     return redirect('/')


@app.route('/submit', methods=['POST'])
def calculate_price():
    distance_weight = float(request.form['distance_weight'])
    time_weight = float(request.form['time_weight'])
    route_weight = float(request.form['route_weight'])
    holiday_weight = float(request.form['holiday_weight'])
    weather_weight = float(request.form['weather_weight'])
    oil_price_weight = float(request.form['oil_price_weight'])

    distance = float(request.form['distance'])
    time = float(request.form['time'])
    route = float(request.form['route'])
    holiday = float(request.form['holiday'])
    weather = float(request.form['weather'])
    oil_price = float(request.form['oil_price'])

    adjusted_price = (distance_weight * distance +
                      time_weight * time +
                      route_weight * route +
                      holiday_weight * holiday +
                      weather_weight * weather +
                      oil_price_weight * oil_price) / 100

    return render_template('index.html', price=adjusted_price)


if __name__ == '__main__':
    app.run()
