import requests
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from .models import CatFact

redis_broker = RedisBroker(url="redis://localhost:6379")
dramatiq.set_broker(redis_broker)

@dramatiq.actor
def fetch_cat_fact():
    response = requests.get('https://cat-fact.herokuapp.com/facts')
    if response.status_code == 200:
        facts = response.json()
        first_fact = facts[0]['text']
        CatFact.objects.create(fact=first_fact)
