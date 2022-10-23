### To run
Simply enter the command **locust** in your terminal then navigate to the assigned port on your machine.
By default this is: http://localhost:8089/

Locust can also be run headless without the UI by utilizing Locust's CLI

For example you can run it like this: \
`locust --headless --users 10 --spawn-rate 1 -H http://your-server.com` \
(The above command will spawn 10 users, 1 user every second) 

For more information on running locust headless see these sources: 
1) https://docs.locust.io/en/stable/quickstart.html#direct-command-line-usage-headless 
2) https://docs.locust.io/en/stable/running-without-web-ui.html

### Documentation:
- Sample API used: https://jsonplaceholder.typicode.com
- JSON Schema Reference Doc: https://json-schema.org/understanding-json-schema/reference/index.html
- Locust Documentation: https://docs.locust.io/en/stable/quickstart.html

### Testing:
Unittests can be run via: \
`python -m unittest discover tests` \
or \
`python -m pytest`

Code syntax testing: \
`pylint *`