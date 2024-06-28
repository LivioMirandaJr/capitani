import asyncio
import json
import logging
from datetime import datetime

import msgspec
from confluent_kafka import Consumer

from common.aiohttp import SingletonAiohttp
from common.settings import settings
from models.product import Product, Pricing, Availability


async def main():
    await SingletonAiohttp.get_aiohttp_client()

    config = {
        'bootstrap.servers': settings.kafka_broker,
        'group.id': settings.kafka_group_id,
        'auto.offset.reset': settings.kafka_offset
    }

    consumer = Consumer(config)
    consumer.subscribe([settings.kafka_topic])

    while True:
        msg = consumer.poll(1.0)
        if not msg:
            logging.error("No message received within timeout")
            continue
        if msg.error():
            logging.error(f"Consumer error: {msg.error()}")
            continue
        serialized_msg = json.loads(msg.value().decode())
        product = Product(
            id=serialized_msg['productId'],
            name=serialized_msg['productName'],
            description=serialized_msg['productDescription'],
            pricing=Pricing(
                amount=serialized_msg['price'],
                currency=serialized_msg['currency']
            ),
            availability=Availability(
                quantity=serialized_msg['stockQuantity'],
                timestamp=datetime.now()
            ),
            category=serialized_msg['category']
        )
        await SingletonAiohttp.post(f"{settings.api_endpoint}/products", msgspec.json.encode(product))

        logging.error(f"product={product.name}")
        logging.info(f"product={product.name}")
        logging.error(f"product={product.pricing.amount}")
        logging.info(f"product={product.pricing.amount}")
        logging.error(f"message={msg.value().decode('utf-8')}")
        print("Received message: {}".format(msg.value().decode()))


asyncio.run(main())
