# URL Shortener (Using Flask)

This is flask based url and file shortener so from long url to short and memoriable urls in just 1 click and you can share them with anywhere.

> [Flask Essential Training](https://www.linkedin.com/learning/flask-essential-training/) course that i followed and created this.

## To-DOs

- [x] Basic functionality
- [ ] Responcive web design
- [x] URL Shortener
- [x] File Shortener
- [x] Pipfile scripts adding
- [ ] Replace json file with Database
- [ ] API Endpoints

## How to Deploy

- Clone this repo
- Install Python 3.7.x
- Install pipenv for virtual env management

```bash
pip install pipenv

cd /some/path/flask-url-shortener/

pipenv install

export FLASK_APP='urlshort'

# Using default flask server [use your own port and expose that using firewall for external access]
flask run --host=0.0.0.0 --port=9000

```

### gUnicorn wsgi server

```bash
pipenv install gunicorn

gunicorn "urlshort:create_app()" -b 0.0.0.0:9000
```

### Setup nginx for upfront request handler and add reverse proxy

```bash
sudo apt install nginx

sudo vi /etc/nginx/sites-enabled/default
```

**nginx** config for setup reverse proxy for gunicorn server
you can find more docs [here](https://gunicorn.org/#deployment)

```
server {
    listen 80;
    server_name example.org;
    access_log  /var/log/nginx/example.log;

    location / {
        proxy_pass http://127.0.0.1:9000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }
```

### Running as daemon process

```bash
# Run as daemon so we can easily close shell
gunicorn "urlshort:create_app()" -b 0.0.0.0:9000 --daemon
```

## Development Server

```bash
cd /some/path/flask-url-shortener/

pipenv install

pipenv run dev      # Development mode

pipenv run start    # Production mode

pipenv run test     # Testing using pytest
```

## Dependency

- [Python 3.7.x](https://www.python.org/)
- [pipenv](https://pypi.org/project/pipenv/)
- [Flaks](https://flask.palletsprojects.com/en/1.1.x/)
- [pytest](https://docs.pytest.org/en/stable/)
- [gunicorn](https://gunicorn.org/)
- [nginx](https://www.nginx.com/)

## Resource

- [Flask Essential Training Course](https://www.linkedin.com/learning/flask-essential-training)
- [URL Shortener System Design](https://medium.com/@narengowda/url-shortener-system-design-3db520939a1c)
- [8 Rules of Minimalist Web Design](https://www.oneims.com/8-rules-of-minimalist-web-design)
- [The Twelve-Factor App](https://12factor.net/)
