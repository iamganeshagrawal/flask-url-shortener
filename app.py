from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)
app.secret_key = 'h55dasdash3hacas68789cxaj'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "This is a url shortener"

@app.route("/your-url", methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        # slug = request.args['slug'] # GET 
        # url = request.args['url']   #GET
        slug = request.form['slug'] # POST 
        url = request.form['url']   #POST

        # Storing data into json
        urls = {}
        
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        
        if slug in urls.keys():
            flash('The short name has already been taken. Please select another one')
            return redirect(url_for('home'))

        urls[slug] = {'url': url}
        with open('urls.json', 'w') as urls_file:
            json.dump(urls, urls_file)

        return render_template('your_url.html', slug=slug, url=url)
    else:
        # return render_template('home.html')
        # return redirect('/')    #Redirect to home
        return redirect(url_for('home'))