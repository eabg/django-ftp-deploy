from fabric.api import local


def test():
    """All Tests"""
    local("django-admin.py test tests \
          --settings=tests.conf.conf --exe")


def testc():
    """All Tests with coverage"""
    local("django-admin.py test tests \
          --settings=tests.conf.confc --exe")


def testu(module=''):
    """Unit Tests"""
    if module:
        module = '.tests.unit_tests.%s' % module

    local("django-admin.py test tests%s \
          --exclude=integration_tests --exclude==external_tests \
          --settings=tests.conf.conf --exe" % module)


def testci():
    """Travis CI Tests"""
    local("django-admin.py test tests \
          --exclude=integration_tests --exclude==external_tests \
          --settings=tests.conf.travis --exe")

def testi(module=''):
    """Integration Tests"""
    if module:
        module = '.tests.integration_tests.%s' % module

    local("django-admin.py test tests%s \
          --exclude=external_tests --exclude=unit_tests  \
          --settings=tests.conf.conf --exe" % module)
