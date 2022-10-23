#! /usr/bin/env python3

'''
File containing individual tests telling the locust users what to do.
'''

from locust import HttpUser, task

from schemas.comment_json import return_comment_schema, return_all_comments_schema
from helpers import validate_response, read_schema, setup_logger

class LocustTests(HttpUser):
    '''
    Class that holds all the locust tests for different API
    endpoints in https://jsonplaceholder.typicode.com
    '''
    @task(2)
    def users_endpoint(self):
        '''
        Locust test for /users endpoint
        :return:
        '''
        with self.client.get("/users", catch_response=True) as response:
            validate_response(response, read_schema("users"))

    @task(1)
    def specific_user_endpoint(self):
        '''
        Locust test for /users/1 endpoint
        :return:
        '''
        with self.client.get("/users/1", catch_response=True) as response:
            validate_response(response, read_schema("user"))

    @task(1)
    def specific_comment_endpoint(self):
        '''
        Locust test for /comments/1 endpoint
        :return:
        '''
        with self.client.get("/comments/1", catch_response=True) as response:
            validate_response(response, return_comment_schema())

    @task(2)
    def comments_endpoint(self):
        '''
        Locust test for /comments endpoint
        :return:
        '''
        with self.client.get("/comments", catch_response=True) as response:
            validate_response(response, return_all_comments_schema())

    def on_start(self):
        '''
        Gets run before locust tasks start executing. Currently just a placeholder.
        :return:
        '''
        logger = setup_logger()
        logger.info("On start place holder. Where users may login"
                    " or other init tasks before sending requests.")

    def on_stop(self):
        '''
        Gets run after locust tasks finish executing. Currently just a placeholder.
        :return:
        '''
        logger = setup_logger()
        logger.info("On stop placeholder. Where users may logout or"
                    " do other clean up tasks before stopping runs.")
