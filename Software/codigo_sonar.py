import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from flask import Flask, render_template
import sys


app = Flask(__name__)
os.environ["PATH"] += ":/usr/local/bin/"

@app.route("/")
def home():

	# os.system("sh test.sh")

	driver = webdriver.Chrome()
	driver.get("http://localhost:9000/measures/search/1?asc=false&cols%5B%5D=metric%3Aalert_status&cols%5B%5D=name&cols%5B%5D=version&cols%5B%5D=metric%3Ancloc&cols%5B%5D=date&cols%5B%5D=metric%3Ablocker_violations&cols%5B%5D=metric%3Acritical_violations&cols%5B%5D=metric%3Amajor_violations&cols%5B%5D=metric%3Aminor_violations&cols%5B%5D=metric%3Acomplexity&cols%5B%5D=metric%3Aduplicated_lines&cols%5B%5D=metric%3Acomment_lines&display=list&pageSize=100&qualifiers=TRK&sort=metric%3Ablocker_violations&id=1")
	time.sleep(3)
	soup = BeautifulSoup(driver.page_source, "html.parser")
	driver.close()

	data = {
		'ncloc'						: soup.select_one("#m_ncloc").string,
		'complexity'				: soup.select_one("#m_complexity").string,
		'comment_lines'				: soup.select_one("#m_comment_lines").string,
		'duplicated_lines'			: soup.select_one("#m_duplicated_lines").string,
		'blocker_violations'		: soup.select_one("#m_blocker_violations").string,
		'critical_violations'		: soup.select_one("#m_critical_violations").string,
		'major_violations'			: soup.select_one("#m_major_violations").string,
		'minor_violations'			: soup.select_one("#m_minor_violations") .string 
	}
	return render_template('index.html', **data)

@app.route("/graph1/<ncloc>")
def graph1(ncloc):
	return render_template('graph1.html', ncloc=ncloc)

@app.route("/graph2/<duplicated_lines>")
def graph2(duplicated_lines):
	return render_template('graph2.html', duplicated_lines = duplicated_lines)

@app.route("/graph3/<complexity>")
def graph3(complexity):
	return render_template('graph3.html', complexity=complexity)

@app.route("/graph4/<blocker_violations>/<critical_violations>/<major_violations>/<minor_violations>")
def graph4(blocker_violations,critical_violations,major_violations,minor_violations):
	return render_template('graph4.html', blocker_violations=blocker_violations,critical_violations=critical_violations,major_violations=major_violations,minor_violations=minor_violations)

if __name__ == "__main__":
    app.run(debug=True)
