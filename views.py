#from app import app
import os
from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
#from __future__ import print_function
import time
import requests
import httplib, urllib, base64
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', name="",)

@app.route('/onClick', methods=['POST'])
def test():
	# headers = {'Content-Type': 'application/json','Ocp-Apim-Subscription-Key': 'a2219199d5834848a8e0546e2645a870'}
	# link = request.form['link']
	# params = urllib.urlencode({'visualFeatures': 'Tags'})
	# conn = httplib.HTTPSConnection('https://api.projectoxford.ai')
	# conn.request("POST", "/vision/v1.0/analyze?%s" % params, "{'url':'"+link+"'}", headers)
	# response = conn.getresponse()
	# data = response.read()
	# json_data = json.loads(data)
	# names = [r['name'] for r in json_data['tags']]
	# words_you_dont_want = ['flower', 'plant']
	# name = ''
	# for n in names:
	# 	if n not in words_you_dont_want:
	# 		name += "%s " % n.title()

	# if name == '':
	# 	name = names[0].title()
	# ftemp = ''
	# #print(data)
	# conn.close()
	# url = "https://api.darksky.net/forecast/209bb716d364854504482e794db7bad8/37.8267,-122.4233"
	# resp = requests.get(url)
	# data1 = resp.json()
	# prob = data1['daily']['data'][0]['precipProbability']
	# if prob > 0.75:
	# 	ans = "No"
	# else:
	# 	ans = "Yes"
	return render_template("index.html")

@app.route('/photo.jpg')
def returnPic():
	return send_file('photo.jpg')

@app.route('/onClick1', methods=['POST'])
def save_uploaded_file ():
	if request.method == 'POST':
		f = request.files['photo']
		f.save("photo.jpg")

	# headers = {'Content-Type': 'application/json','Ocp-Apim-Subscription-Key': 'a2219199d5834848a8e0546e2645a870'}
	# link = "https://aquaflora.herokuapp.com/photo.jpg"
	# params = urllib.urlencode({'visualFeatures': 'Tags'})
	# conn = httplib.HTTPSConnection('https://api.projectoxford.ai')
	# conn.request("POST", "/vision/v1.0/analyze?%s" % params, "{'url':'"+link+"'}", headers)
	# response = conn.getresponse()
	# data = response.read()
	# json_data = json.loads(data)
	# names = [r['name'] for r in json_data['tags']]
	# words_you_dont_want = ['flower', 'plant']
	# name = ''
	# for n in names:
	# 	if n not in words_you_dont_want:
	# 		name += "%s " % n.title()

	# if name == '':
	# 	name = names[0].title()
	# ftemp = ''
	# print(name)
	# conn.close()
	# url = "https://api.darksky.net/forecast/209bb716d364854504482e794db7bad8/37.8267,-122.4233"
	# resp = requests.get(url)
	# data1 = resp.json()
	# prob = data1['daily']['data'][0]['precipProbability']
	# if prob > 0.75:
	# 	ans = "No"
	# else:
	# 	ans = "Yes"
	return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
