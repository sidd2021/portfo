from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_info>')
def page_info(page_info):
    return render_template(page_info)


def store_data_csv(data):
    with open('database.csv',mode='a') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


def store_data(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        database.write(f'{email},{subject},{message}\n')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        store_data_csv(data)
        return redirect("/thankyou.html")
    else:
        print("something went wrong")


# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# $env:FLASK_APP="server"
# $env:FLASK_ENV="development"
# flask run