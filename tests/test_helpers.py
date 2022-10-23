#! /usr/bin/env python3

'''
Unittests for helpers.py
'''

import unittest
from unittest import mock
from helpers import read_schema, validate_response
from requests.models import Response

valid_test_schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "Arbitrary valid schema for unittest",
        "type": "object",
        "properties": {
            "id": {
                "type": "number"
            }
        }
    }


test_response = Response()
test_response._content = b'{"id": 1, "email": "Eliseo@gardner.biz"}'


class TestLocustFile(unittest.TestCase):
    '''
    Class for setting up and running tests on locustfile.py functions.
    '''
    def test_read_schema(self):
        '''
        Test to validate that read_schema function returns a JSON dictionary object.
        :return:
        '''
        result = read_schema("test")
        self.assertTrue(type(result) == dict)

    @mock.patch('jsonschema.validate', return_value="pass")
    def test_validate_response_success(self, mock_validate):
        validate_response(test_response, valid_test_schema)
        assert mock_validate.called is True
        assert mock_validate.call_count == 1
