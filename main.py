from flask import Flask, render_template, request, redirect, url_for

import house_controller, database, resident_controller

database.init_db()

app = Flask(__name__)


@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/setup')
def setup_home():
    return render_template('setup_home.html')

@app.route('/setup_house')
def setup_house():
    return render_template('setup_house.html')

@app.route('/setup_resident')
def setup_resident():
    return render_template('setup_resident.html')

@app.route('/setup/submit_house', methods=['GET', 'POST'])
def submit_house_data():
    if request.method == 'POST':
        #add code to take webform data and persist to DB
        name = request.form['name']
        address = request.form['address']
        house_controller.createNewHouse(name, address)
        return redirect(url_for('setup_resident.html'))
    return render_template('setup_house.html')

@app.route('/setup/submit_resident', methods=['get', 'post'])
def submit_resident_data():
    if request.method == 'post':
        name = request.form['name']
        email = request.form['email']
        user_pin = request.form['user_pin']
        phone = request.form['phone']
        ip = request.form['ip']
        mac = request.form['mac']
        resident_controller.createNewResident(name, email, user_pin, phone, ip, mac)
        return render_template('setup.resident.html')
    return render_template('setup_resident.html')


if __name__ == "__main__":
    app.run(debug=True)