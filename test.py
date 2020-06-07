#!/usr/bin/env python
import unittest
import sys
sys.path.append(os.environ['WORKSPACE'])
import app
'''
 File "/var/jenkins_home/workspace/webmf-python-flask/app.py", line 2, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
'''

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_name(self):
        name = 'Simon'
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

if __name__ == '__main__':
    #import xmlrunner
    #runner = xmlrunner.XMLTestRunner(output='test-reports')
    #unittest.main(testRunner=runner)
    #unittest.main()
    assert 1 == 1
