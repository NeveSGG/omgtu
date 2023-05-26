from flask import Flask, render_template, make_response, request
import csv
from io import StringIO
import unittest


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


class TestFlaskProject(unittest.TestCase):
    def test_survey(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertNotIn(bytes("ЫЫЫЫыыыыы", 'utf-8'), response.data)
            self.assertIn(bytes("Форма анкеты", 'utf-8'), response.data)

    def test_submit(self):
        with app.test_client() as client:
            response = client.post('/submit', data={
                'name': 'John Doe',
                'email': 'john@example.com',
                'age': '25',
                'gender': 'Male',
                'language': 'English',
                'editor': 'Atom'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(bytes("Спасибо за прохождение анкеты", 'utf-8'), response.data)

    def test_download(self):
        with app.test_client() as client:
            response = client.get('/download')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'text/csv')
            self.assertEqual(response.headers['Content-Disposition'], 'attachment; filename=results.csv')


if __name__ == '__main__':
    unittest.main()


