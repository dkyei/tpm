from flask import render_template, request

from manage import app, mongo, Individual_GIS, Individual_EC, Individual_NHIA, db


def add_citizens():
    citizen_1 = Individual_EC(
        username="yaw",
        location="abokobi",
        next_of_kin="Jim",
        age=27
    )
    citizen_2 = Individual_GIS(
        username="yaw",
        location="abokobi",
        next_of_kin="Jim",
        age=27
    )
    citizen_3 = Individual_NHIA(
        username="yaw",
        location="abokobi",
        next_of_kin="Jim",
        age=27
    )
    citizen_4 = {
        "username": "yaw",
        "location": "Abokobi",
        "next_of_kin": "Jim",
        "age": "25",
    }

    db.session.add(citizen_1, citizen_2, citizen_3)

    db.session.commit()
    mongo.db.individual_DVLA.insert(citizen_4)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []

    # add_citizens()
    if request.method == "POST":
        username = request.form['username']
        next_of_kin = request.form['next_of_kin']

        if username and next_of_kin:
            citizens_EC = Individual_EC.query.filter_by(username=username, next_of_kin=next_of_kin).all()
            citizens_GIS = Individual_GIS.query.filter_by(username=username, next_of_kin=next_of_kin).all()
            citizens_NHIA = Individual_NHIA.query.filter_by(username=username, next_of_kin=next_of_kin).all()

            citizens = mongo.db.individual_DVLA
            citizens_DVLA_1 = []
            for c in citizens.find():
                citizens_DVLA_1.append(
                    {'username': c['username'], 'location': c['location'], 'next_of_kin': c['next_of_kin'],
                     'age': c['age']})

            citizens_DVLA = []
            for citizen in citizens_DVLA_1:
                if citizen['username'] == username and citizen['next_of_kin'] == next_of_kin:
                    citizens_DVLA.append(
                        {'username': citizen['username'], 'location': citizen['locatoin'],
                         'next_of_kin': citizen['next_of_kin'],
                         'age': citizen['age']})

            return render_template('citizens.html', citizens_EC=citizens_EC, citizens_GIS=citizens_GIS,
                                   citizens_NHIA=citizens_NHIA, citizens_DVLA=citizens_DVLA)
        else:

            errors = {"File is not in JSON format"}

    return render_template('index.html', errors=errors)


@app.route('/citizens', methods=['GET', ])
def results():
    return render_template('citizens.html')


if __name__ == "__main__":
    app.run()
