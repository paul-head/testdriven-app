import unittest
import coverage
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User


app = create_app()
cli = FlaskGroup(create_app=create_app)


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()


@cli.command()
def recreate_db():
    """ Recreate db """
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """ Runs the tests without code coverage """
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    if results.wasSuccessful():
        return 0
    return 1


@cli.command()
def seed_db():
    """ Seed database """
    db.session.add(User(username='pavel', email='pavel@pavel.ru', password='testpasswd'))
    db.session.add(User(username='testuser1', email='testuser1@testuser1.com', password='testpasswd'))
    db.session.commit()


@cli.command()
def cov():
    """ Run unit tests with coverage """
    tests = unittest.TestLoader().discover('project/tests')
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    if results.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


if __name__ == '__main__':
    cli()
