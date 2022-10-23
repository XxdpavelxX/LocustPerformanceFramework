#! /usr/bin/env python3

'''
We can also write our json schema inside Python files and functions.
'''

def return_comment_schema():
    '''
    Returns a dictionary object representing the json response from the /comments/<number> endpoint
    :return: {dictionary object}
    '''
    data = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "Comment1 response schema. Endpoint: /comments/<number>",
        "type": "object",
        "properties": {
            "postId": {
                "type": "number"
            },
            "id": {
                "type": "number"
            },
            "name": {
                "type": "string"
            },
            "email": {
                "type": "string",
                "format": "email"
            },
            "body": {
                "type": "string"
            }
        },
    }
    return data

def return_all_comments_schema():
    '''
    Returns a dictionary object representing the json response from the /comments endpoint
    :return: {dictionary object}
    '''
    data = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "Multiple comments response schema. Endpoint: /comments",
        "type": "array",
        "items": return_comment_schema()
    }
    return data
