import sys

if sys.version_info < (3, 0):
    from django_nose import NoseTestSuiteRunner
    from django_coverage.coverage_runner import CoverageRunner

    class NoseCoverageTestRunner(CoverageRunner, NoseTestSuiteRunner):

        """Custom test runner that uses nose and coverage"""
        pass
