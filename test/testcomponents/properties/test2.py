import unittest
from PageObModel.test.testcomponents.properties import parenttest as pt

def setup_module():
    print(__name__, ': setup_module() ~~~~~~~~~~~~~~~~~~~~~~')

def teardown_module():
    print(__name__, ': teardown_module() ~~~~~~~~~~~~~~~~~~~')

class TestClass2(pt.BaseTest):

    @classmethod
    def setup_class(cls):
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def teardown_class(cls):
        print(__name__, ': TestClass.teardown_class() -------')

    def setup(self):
        print(__name__, ': TestClass.setup()  - - - - - - - -')

    def teardown(self):
        print(__name__, ': TestClass.teardown() - - - - - - -')

    def test_method_1(self):
        print(__name__, ': TestClass.test_method_1()')

    def test_method_2(self):
        print(__name__, ': TestClass.test_method_2()')
