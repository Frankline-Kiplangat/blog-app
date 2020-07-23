from app import app
from flask_script import Manager, Server
from  flask_migrate import Migrate, MigrateCommand

# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)
manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run()