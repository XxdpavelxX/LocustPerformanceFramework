#! /usr/bin/env python3

'''
Unittests for comment_json.py
'''

import unittest
from schemas.comment_json import return_comment_schema, return_all_comments_schema

class TestCommentJson(unittest.TestCase):
    '''
    Class for setting up and running tests on comment_json.py functions.
    '''
    def test_return_comment_schema(self):
        '''
        Test to validate that return_comment_schema function returns a dictionary.
        :return:
        '''
        result = return_comment_schema()
        self.assertTrue(type(result) == dict)
        self.assertIn("properties", result)
        self.assertIn("title", result)
        self.assertEqual(result["type"], "object")
        self.assertTrue(type(result["properties"]) == dict)

    def test_return_all_comments_schema(self):
        '''
        Test to validate that return_comment_schema function returns a dictionary.
        :return:
        '''
        result = return_all_comments_schema()
        self.assertTrue(type(result) == dict)
        self.assertIn("items", result)
        self.assertEqual(result["type"], "array")
        self.assertIn("title", result)
