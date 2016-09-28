from flask import Flask, render_template, request, redirect, url_for

import house_controller, database, resident_controller

database.init_db()

app = Flask(__name__)


# Setup routes - functions and routing related to the setup and configuration of the household

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/setup')
def setup_home():
    return render_template('setup_home.html')

@app.route('/setup_house')
def setup_house():
    house_in_db = database.getAllHouses()
    return render_template('setup_house.html', house=house_in_db)

@app.route('/setup_resident')
def setup_resident():
    residents = database.getAllResidents()
    return render_template('setup_resident.html', residents=residents)

@app.route('/setup/submit_house', methods=['GET', 'POST'])
def submit_house_data():
    if request.method == 'POST':
        #add code to take webform data and persist to DB
        name = request.form['name']
        address = request.form['address']
        house_controller.createNewHouse(name, address)
        return redirect(url_for('setup_resident'))
    return render_template('setup_house.html')

@app.route('/setup/submit_resident', methods=['GET', 'POST'])
def submit_resident_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user_pin = request.form['user_pin']
        phone = request.form['phone']
        ip = request.form['ip']
        mac = request.form['mac']
        resident_controller.createNewResident(name, email, user_pin, phone, ip, mac)
        return redirect(url_for('setup_resident'))
    return render_template('setup_resident.html')

@app.route('/remove_resident', methods=['POST'])
def remove_resident():
    name_to_remove = request.form['removeResident']
    database.deleteResident(name_to_remove)
    return redirect(url_for('setup_resident'))

@app.route('/test')
def testpage():
    return render_template('test.html')

@app.route('/animalfeeder')
def animalfeeder():
    pets_fed_today = database.getTodaysPetInfo()
    return render_template('animalfeeder.html', pets=pets_fed_today)

@app.route('/animals_fedam', methods=['POST'])
def animals_fedam():
    animalsam = True
    animalspm = False
    house_controller.animals_are_fed(animalsam, animalspm)
    return redirect(url_for('dashboard'))

@app.route('/animals_fedpm', methods=['POST'])
def animals_fedpm():
    animalsam = False
    animalspm = True
    house_controller.animals_are_fed(animalsam, animalspm)
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
