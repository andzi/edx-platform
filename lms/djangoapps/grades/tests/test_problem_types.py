"""
Test that persistent grading works for different block types
"""
from path import Path

import ddt
from django.test import TestCase

from student.tests.factories import CourseEnrollmentFactory, UserFactory
from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from xmodule.modulestore.tests.factories import CourseFactory


TEST_DATA_DIR = Path(__file__).dirname() / 'data'  # pylint: disable=invalid-name


@ddt.ddt
class TestGradingProblemTypes(TestCase):
    """
    Test that grading works for different problem types
    """

    @ddt.data(
        'capa.xml',
        'openassessment.xml',
    )
    def test_save_grades_by_block_type(self, problem_file):
        course_key = 'x'
        import_course_from_xml(
            self.store,
            'test_user',
            TEST_DATA_DIR,
            source_dirs=[problem_file],
            static_content_store=None,
            target_id=course_key,
            raise_on_failure=True,
            create_if_not_present=True,
        )


