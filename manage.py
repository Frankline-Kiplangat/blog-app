from app import app
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


# Creating app instance

manager = Manager(app)
manager.add_command('server', Server)




@manager.command
def test():
    """Run unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    pass


if __name__ == '__main__':
    manager.run()
