from fabric.api import local


def test():
    """All Tests"""
    local("django-admin.py test tests \
          --settings=tests.conf.conf --exe")


def testc():
    """All Tests with coverage"""
    local("django-admin.py test tests \
          --settings=tests.conf.conf_coverage --exe")


def testu(module=''):
    """Unit Tests"""
    if module:
        module = '.unit_tests.%s' % module

    local("django-admin.py test tests%s \
          --exclude='integration_tests|external_tests' \
          --settings=tests.conf.conf --exe" % module)


def testi(module=''):
    """Integration Tests"""
    if module:
        module = '.integration_tests.%s' % module

    local("django-admin.py test tests%s \
          --exclude='unit_tests' --settings=tests.conf.conf --exe" % module)


def testci():
    """Travis CI Tests"""
    local("django-admin.py test tests \
          --exclude='external_tests' \
          --settings=tests.conf.conf_travis --exe")
