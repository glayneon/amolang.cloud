#!python

_targetHost = 'wowanggood.com'
_targetUser = _targetHost.split('.')[0]
_targetPort = 12272


try:
    import keyring
except ModuleNotFoundError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keyring'])
    import keyring
    import getpass
    _pass = getpass.getpass()
    print("Login Name : {} set the password...".format(getpass.getuser()))
    # creating keyring
    keyring.set_password(_targetHost, _targetUser, _pass)

try:
    from fabric import Connection, task
except ModuleNotFoundError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'fabric'])
    from fabric import Connection, task

@task
def make_update_all(ctx):
    with Connection(
        _targetHost,
        user = _targetUser,
        port = _targetPort,
        connect_kwargs={'password': keyring.get_password(_targetHost, _targetUser)}
    ) as c:
        c.run('uname -a')


if __name__ == '__main__':
    make_update_all()
