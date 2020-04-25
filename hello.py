from flask import Flask, render_template, url_for,request,redirect
import csv
app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:username>')
def work(username):
    return render_template(username)



def write_to_data(data):
	with open('database.txt',mode = 'a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n email= {email},subject = {subject},message = {message}')

def write_to_csv(data):
	with open('database.csv',mode = 'a',newline='') as database1:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database1, delimiter = ',',quotechar = '"',quoting=csv.QUOTE_MINIMAL)
		
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect('thank-you.html')
    else:
    	return 'something went wrong'
   	
#@app.route('/favicon.ico')
#def favicon():
    #return send_from_directory(os.path.join(app.root_path, 'static'),
                               #'favicon.ico', mimetype='image/vnd.microsoft.icon')    