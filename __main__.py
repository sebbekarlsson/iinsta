import os
from iinsta.app import app
from iinsta.config import config
import flask_assets


STATIC_DIR = 'iinsta/static'


def run():
    env = flask_assets.Environment(app)

    env.load_path = [
        os.path.join(os.path.dirname(__file__), '{STATIC_DIR}/js'.format(
            STATIC_DIR=STATIC_DIR
        ))
    ]

    env.register(
        'js_all',
        flask_assets.Bundle(
            'wpost.js',
            'wget.js',
            'utils.js',
            'Article.js',
            'Account.js',
            'Search.js',
            'app.js',
            filters=['jsmin'],
            output='js/packed.js'
        )
    )

    app.run(
        debug=config['debug'] if 'debug' in config else False,
        threaded=config['threaded'] if 'threaded' in config else False
    )


if __name__ == '__main__':
    run()
