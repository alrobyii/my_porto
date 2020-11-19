from flask import Flask, render_template, url_for, request, redirect
import os
import csv
import sys
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database2.txt', "w") as database:
		email   = data['email']
		subject = data['subject']
		message = data['message']
		file    = database.write(f'\n{email},{subject},{message}')
		

# def write_to_csv(data):
# 	with open('database.csv', mode='a') as database2:
# 		email   = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		csv_writer    = csv_writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	print(data)
    	# write_to_csv(data)
    	# write_to_file(data)
    	# return '111111111111111111111'
    	return redirect('./thx.html')
    else:
    	return 'smth went wrong try again'