from fabric.api import local


def test():
    """All Tests"""
    local("django-admin.py test ftp_deploy \
          --settings=ftp_deploy.tests.conf.conf --exe")


def testc():
    """All Tests with coverage"""
    local("django-admin.py test ftp_deploy \
          --settings=ftp_deploy.tests.conf.confc --exe")


def testu(module=''):
    """Unit Tests"""
    if module:
        module = '.tests.unit_tests.%s' % module

    local("django-admin.py test ftp_deploy%s \
          --exclude=integration_tests --exclude==external_tests \
          --settings=ftp_deploy.tests.conf.conf --exe" % module)


def testi(module=''):
    """Integration Tests"""
    if module:
        module = '.tests.integration_tests.%s' % module

    local("django-admin.py test ftp_deploy%s \
          --exclude=external_tests --exclude=unit_tests  \
          --settings=ftp_deploy.tests.conf.conf --exe" % module)
