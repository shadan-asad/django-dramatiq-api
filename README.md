## Django Web Application with Asynchronous Processing (Dramatiq, Redis, PostgreSQL, Heroku)
### Developed and deployed a Django microservice on Heroku that fetches and displays cat facts via a REST API.
### Integrated PostgreSQL for data storage and Redis for caching and task queue management using Dramatiq for asynchronous task execution.
### Employed a worker-based architecture with gunicorn and Dramatiq to manage asynchronous tasks, effectively decoupling data processing from user requests.

## Live Links for the APIs
#### GET catfact-7270ffcda952.herokuapp.com/api/health_check
#### POST catfact-7270ffcda952.herokuapp.com/api/fetch_fact
#### GET catfact-7270ffcda952.herokuapp.com/api/get_fact
