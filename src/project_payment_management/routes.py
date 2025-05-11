import project_payment_management.structures.projects as psp
import project_payment_management.data.samples as pds

from flask import render_template, url_for
from project_payment_management import app

samples = {
    "projects": {"P1": "Test 1", "P2": "Test 2", "P3": "Test 3"},
    "contracts": [
        {"key": "C1", "name": "Con 1", "project": "P1"},
        {"key": "C2", "name": "Con 2", "project": "P2"},
        {"key": "C3", "name": "Con 3", "project": "P3"},
        ]
} 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/projects')
@app.route('/projects/index')
def projects():
    user = dict()
    user["username"] = "User 1"
    # contracts = samples["contracts"]
    user_projects: list[psp.Project] = []
    for i in pds.make_projects():
        user_projects.append(i)
    return render_template('projects.html', title='Projects', user=user, projects=user_projects)

