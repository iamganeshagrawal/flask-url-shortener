from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from os import getcwd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'h55dasdash3hacas68789cxaj'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    print(getcwd())
    return "This is a url shortener"

@app.route("/your-url", methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        # slug = request.args['slug'] # GET 
        # url = request.args['url']   #GET
        slug = request.form['slug'] # POST 

        # Storing data into json
        urls = {}
        
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        
        if slug in urls.keys():
            flash('The short name has already been taken. Please select another one')
            return redirect(url_for('home'))

        if 'url' in request.form.keys():
            url = request.form['url']   #POST
            urls[slug] = {'url': url}
        else:
            f = request.files['file']
            full_name = slug + '-' + secure_filename(f.filename)
            f.save(os.path.join('uploads', full_name))
            urls[slug] = {'file': full_name}

        with open('urls.json', 'w') as urls_file:
            json.dump(urls, urls_file)

        return render_template('your_url.html', slug=slug)
    else:
        # return render_template('home.html')
        # return redirect('/')    #Redirect to home
        return redirect(url_for('home'))

@app.route('/<string:slug>')
def redirect_to_url(slug):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)

            if slug in urls.keys():
                slug_info = urls[slug]
                if 'url' in slug_info.keys():
                    return redirect(slug_info['url'])
            else:
                flash('The short name has not exits.')
                return redirect(url_for('home'))