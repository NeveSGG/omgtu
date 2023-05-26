from flask import Flask, render_template, make_response, request
import csv
from io import StringIO

def save_to_csv(data):
    # Create a StringIO object to hold the CSV data
    output = StringIO()

    # Write the data to the output buffer in CSV format
    writer = csv.writer(output)
    writer.writerow(['Name', 'Email', 'Age', 'Gender', 'Language', 'Editor'])
    writer.writerow([data['name'], data['email'], data['age'], data['gender'], data['language'], data['editor']])

    # Return the value of the output buffer
    return output.getvalue()


dataState = ''

app = Flask(__name__)


@app.route('/', methods=['GET'])
def survey():
    return render_template('survey.html')


@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'age': request.form['age'],
        'gender': request.form['gender'] if ('gender' in request.form) else '',
        'language': request.form['language'],
        'editor': request.form['editor']
    }

    # Save the data to CSV format
    global dataState
    dataState = save_to_csv(data)

    # Code for saving data to database goes here

    return render_template('confirmation.html')


@app.route('/download')
def download():
    # Get the data from the database and save it to a CSV file
    csv_data = dataState
    output = make_response(csv_data)
    output.headers["Content-Disposition"] = "attachment; filename=results.csv"
    output.headers["Content-type"] = "text/csv"
    return output


if __name__ == '__main__':
    app.run(debug=True)


