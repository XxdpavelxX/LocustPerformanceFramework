#! /usr/bin/env python3

'''
This is where helper functions that assist in the execution of locust tests are written
'''

import json
import logging

import jsonschema

def setup_logger():
    '''
    Creates a Logger that writes log output to both console and logs/locust_records.log
    :return: {logging object}
    '''
    logger = logging.getLogger("LocustLogger")
    logger.setLevel(logging.ERROR)
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # Setting up a logger that writes to locust_records.py
    filename = "logs/locust_records.log"
    file_log_handler = logging.FileHandler(filename)
    file_log_handler.setLevel(logging.ERROR)
    file_log_handler.setFormatter(log_format)
    logger.addHandler(file_log_handler)
    # Setting up a logger that writes to console
    console_log_handler = logging.StreamHandler()
    console_log_handler.setLevel(logging.ERROR)
    console_log_handler.setFormatter(log_format)
    logger.addHandler(console_log_handler)
    return logger

def read_schema(file_name):
    '''
    Loads the passed json schema file containing the expected API response and returns it as json.
    :param file_name: {string object}: Name of the json schema file to load.
    :return: {json object}: JSON object representing the expected response from passed schema file.
    '''
    file_data = open(f'schemas/{file_name}.json')
    data = json.load(file_data)
    return data

def validate_response(response, schema):
    '''
    Compares the passed API response content vs the expected content from the passed schema.
    Tells locust to log a failure if there is a mismatch between the response and schema or
    to raise an error if the schema provided is invalid.
    :param response: {CLASS object}: The API response received from an endpoint.
    :param schema: {JSON object}: JSON object representing the expected API response.
    :return:
    '''
    logger = setup_logger()
    try:
        jsonschema.validate(response.json(), schema)
    except jsonschema.SchemaError as schema_error:
        logger.error(f'There is an error with the schema. Make sure'
                     f' the provided schema is valid. \n {schema_error}')
        raise schema_error
    except jsonschema.ValidationError as validation_error:
        logger.error("---------")
        logger.error(validation_error)
        logger.error("---------")
        logger.error(validation_error.absolute_path)
        logger.error("---------")
        logger.error(validation_error.absolute_schema_path)
        response.failure("The provided schema does not match JSON response content")
