#from app import app
import os
from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
#from __future__ import print_function
import time
import requests
import httplib, urllib, base64
import json
import geocoder

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', name="Please enter link above.",)

@app.route('/onClick', methods=['POST'])
def test():
	address = request.form['address']
	link = request.form['link']
	if address == "" or link == "":
		return render_template("index.html", name="Please enter link above")

	headers = {'Content-Type': 'application/json','Ocp-Apim-Subscription-Key': 'a2219199d5834848a8e0546e2645a870'}
	
	print(link)
	params = urllib.urlencode({'visualFeatures': 'Tags'})
	conn = httplib.HTTPSConnection('api.projectoxford.ai')
	conn.request("POST", "/vision/v1.0/analyze?%s" % params, "{'url':'"+link+"'}", headers)
	response = conn.getresponse()
	data = response.read()
	json_data = json.loads(data)

	names = [r['name'] for r in json_data['tags']]
	words_you_dont_want = ['flower', 'plant', 'indoor', 'tree', 'outdoor', 'snack food', 'food', 'crazy', 'water', 'several']
	name = ''
	for n in names:
		if n not in words_you_dont_want:
			name += "%s " % n.title()
	if name == '':
		name = names[0].title()
	ftemp = ''
	#print(data)
	conn.close()
	formatSt = ""
	
	g = geocoder.google("address")
	ll = g.latlng
	formatSt = str(ll[0]) + "," + str(ll[1])

	url = "https://api.darksky.net/forecast/209bb716d364854504482e794db7bad8/"+formatSt+""
	resp = requests.get(url)
	data1 = resp.json()
	prob = data1['daily']['data'][0]['precipProbability']
	humidity = data1['daily']['data'][0]['humidity']
	temperature = data1['daily']['data'][0]['temperatureMax']
	wind = data1['daily']['data'][0]['windSpeed']
	if prob > 0.75 and humidity < 0.50 and temperature < 50 and wind < 5:
		ans = "No need to water your plants this week."
	elif prob > 0.75 and humidity > 0.50 and temperature < 50 and wind < 5:
		ans = "Water your plants a little this week."
	elif prob > 0.75 and humidity > 0.50 and temperature > 78 and wind < 5:
		ans = "Water your plants a lot this week."
	elif prob > 0.75 and humidity > 0.50 and temperature > 78 and wind > 9:
		ans = "Water your plants a lot this week!"
	elif prob < 0.75 and humidity > 0.50 and temperature > 78 and wind > 9:
		ans = "Water your plants a lot this week."
	elif prob < 0.75 and humidity < 0.50 and temperature > 78 and wind > 9:
		ans = "Water your plants a little this week."
	elif prob < 0.75 and humidity < 0.50 and temperature < 50 and wind > 9:
		ans = "No need to water your plants this week."
	elif prob < 0.75 and humidity < 0.50 and temperature < 50 and wind < 5:
		ans = "No need to water your plants this week."
	else:
		ans = "Water your plants this week."
	return render_template("index.html", link=link, name=name, location=address, prob=prob, water=ans, humidity=humidity, temperature=temperature, wind=wind)

@app.errorhandler(500)
def refresh(e):
	return render_template("index.html", name="Please enter link above"), 500
# @app.route('/photo.jpg')
# def returnPic():
# 	return send_file('photo.jpg')

# @app.route('/onClick1', methods=['POST'])
# def save_uploaded_file ():
# 	if request.method == 'POST':
# 		f = request.files['photo']
# 		f.save("photo.jpg")

# 	# headers = {'Content-Type': 'application/json','Ocp-Apim-Subscription-Key': 'a2219199d5834848a8e0546e2645a870'}
# 	link = "https://aquaflora.herokuapp.com/photo.jpg"
# 	print(link)
# 	params = urllib.urlencode({'visualFeatures': 'Tags'})
# 	conn = httplib.HTTPSConnection('https://api.projectoxford.ai')
# 	conn.request("POST", "/vision/v1.0/analyze?%s" % params, "{'url':'"+link+"'}", headers)
# 	response = conn.getresponse()
# 	data = response.read()
# 	json_data = json.loads(data)
# 	names = [r['name'] for r in json_data['tags']]
# 	words_you_dont_want = ['flower', 'plant']
# 	name = ''
# 	for n in names:
# 		if n not in words_you_dont_want:
# 			name += "%s " % n.title()

# 	if name == '':
# 		name = names[0].title()
# 	ftemp = ''
# 	print(name)
# 	conn.close()
# 	url = "https://api.darksky.net/forecast/209bb716d364854504482e794db7bad8/37.8267,-122.4233"
# 	resp = requests.get(url)
# 	data1 = resp.json()
# 	prob = data1['daily']['data'][0]['precipProbability']
# 	if prob > 0.75:
# 		ans = "No"
# 	else:
# 		ans = "Yes"
# 	return render_template("index.html")

#app.run()
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
