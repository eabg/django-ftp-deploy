import settings

from fabric.api import local


def test():
    """All Tests"""
    local("python ../manage.py test ftp_deploy \
          --settings=%s.conf --exe", settings.PROJECT_NAME)


def testc():
    """All Tests with coverage"""
    local("python ../manage.py test ftp_deploy \
          --settings=%s.confc --exe", settings.PROJECT_NAME)


def testu(module=''):
    """Unit Tests"""
    if module:
        module = '.tests.unit_tests.%s' % module

    local("python ../manage.py test ftp_deploy%s \
          --exclude=integration_tests --exclude==external_tests \
          --settings=%s.conf.conf --exe" % (module, settings.PROJECT_NAME))


def testi(module=''):
    """Integration Tests"""
    if module:
        module = '.tests.integration_tests.%s' % module

    local("python ../manage.py test ftp_deploy%s \
          --exclude=external_tests --exclude=unit_tests  \
          --settings=%s.conf.conf --exe" % (module, settings.PROJECT_NAME))
