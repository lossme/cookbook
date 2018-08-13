import os
from flask_script import Manager

from mysite import create_app


here = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(here, 'conf/config.py')

app = create_app(config_file)
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
