from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        return render_template('your_url.html', slug=slug, url=url)
    else:
        # return render_template('home.html')
        # return redirect('/')    #Redirect to home
        return redirect(url_for('home'))