from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from os import getcwd
from werkzeug.utils import secure_filename

bp = Blueprint('urlshort', __name__)


@bp.route('/')
def home():
    return render_template('home.html', slugs=session.keys())

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route("/your-url", methods=['GET', 'POST'])
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
            return redirect(url_for('urlshort.home'))

        if 'url' in request.form.keys():
            url = request.form['url']   #POST
            urls[slug] = {'url': url}
        else:
            f = request.files['file']
            full_name = slug + '-' + secure_filename(f.filename)
            f.save(os.path.join('static','uploads', full_name))
            urls[slug] = {'file': full_name}

        with open('urls.json', 'w') as urls_file:
            json.dump(urls, urls_file)
            session[slug] = True

        return render_template('your_url.html', slug=slug)
    else:
        # return render_template('home.html')
        # return redirect('/')    #Redirect to home
        return redirect(url_for('urlshort.home'))

@bp.route('/<string:slug>')
def redirect_to_url(slug):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)

            if slug in urls.keys():
                slug_info = urls[slug]
                if 'url' in slug_info.keys():
                    return redirect(slug_info['url'])
                else:
                    return redirect(url_for('static', filename='uploads/' + slug_info['file']))
            # else:
            #     flash('The short name has not exits.')
            #     return redirect(url_for('home'))
    return abort(404)

@bp.route('/api')
def session_api():
    return jsonify(list(session.keys()))

# Error 404
@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
