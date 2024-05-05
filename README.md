## Django Web Application with Asynchronous Processing (Dramatiq, Redis, PostgreSQL, Heroku)
### Developed and deployed a Django microservice on Heroku that fetches and displays cat facts via a REST API.
### Integrated PostgreSQL for data storage and Redis as a broker and task queue management using Dramatiq for asynchronous task execution.
### Employed a worker-based architecture with gunicorn and Dramatiq to manage asynchronous tasks, effectively decoupling data processing from user requests.

## Live Links for the APIs
#### GET https://catfact-7270ffcda952.herokuapp.com/api/health_check
#### POST https://catfact-7270ffcda952.herokuapp.com/api/fetch_fact
#### GET https://catfact-7270ffcda952.herokuapp.com/api/get_fact

## Flow
##### /fetch_fact: It queues an async task to fetch data from https://cat-fact.herokuapp.com/facts endpoint and it returns {‘success’: True} response if the “message queueing” is successful
##### /get_fact: returns the fact which was processed after hitting the above API.


