import os, platform, socket, modules.repo as repo, modules.utils as utils
from tokenize import Name
from flask_prometheus_metrics import register_metrics
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple


from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return get_gallery()

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


@app.route('/gallery')
def get_gallery():
    response = repo.getImages()
    return render_template("gallery.html", 
            db_connected = response[0],
            image_names = response[1], 
            node = platform.node()
            )


############## Metrics ##############
# Provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.0.0", app_config="staging")

def create_dispatcher() -> DispatcherMiddleware:
    # App factory for dispatcher middleware managing multiple WSGI apps
    return DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})
######################################


if __name__ == "__main__":
    run_simple(
        "localhost",
        9000,
        create_dispatcher()
    )

