# API Challenge
[Deployment](https://capitals-api.herokuapp.com/)

## Requirements

This challenge is to produce a web service using Java or Python.This web service should be a
restful API that performs a search with the following requirements:
* The request should accept a search string as input.
* The data to be searched should be in a MongoDB database.
* The response should be formatted in JSON.
* The API needs to return appropriate response codes (i.e. 200, 404, etc)
* The API should handle at least one scalability concern. Describe which scalability concerns you picked, and why.
* The API should handle at least one security concern. Describe which security concern you picked, and why.

We will pay attention to good programming best practices, your ability to write reusable code, as
well as your testing strategy.

Assumptions
* You don’t need to worry about ordering by search relevancy. Any match may be returned in no particular order.

Deliverables
* Code accessible in a github repository.
* Code deployed on a server in the cloud, so that the API may be invoked.
* A simple, hosted, front-end to invoke the search API

## Solutions

#### Security
By implementing [Flask Limiter](https://flask-limiter.readthedocs.io/en/stable/), requests from the api are limited to 500 per day. Do to the simplicity of the app, 
I am not expecting more requests than that, but limits are easily adjustable. 

#### Scalability
Along with security, Flask Limiter also helps with scalabilty. I have implemented a trie as the search algorithm to be more 
efficient when a higher rate of requests come in and more data is stored. This trie returns the closest match to the user input.
