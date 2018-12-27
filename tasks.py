
from invoke import task

@task
def tests(c):
    c.run('py.test -vvx tests', pty=True)


@task
def release(c):
    c.run('mkdir dist')
    c.run('python setup.py sdist bdist_wheel')
    c.run('python -m twine upload dist/*')
