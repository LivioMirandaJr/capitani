import logging

from confluent_kafka import Producer as KafkaProducer

from settings import settings


class Producer:
    _p: KafkaProducer

    async def __aenter__(self):
        self._p = KafkaProducer({
            'bootstrap.servers': settings.kafka_broker,
        })
        self._p.poll(0)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._p.flush()

    @staticmethod
    def _delivery_report(err, msg):
        if err:
            logging.error(f"Producer error {err}, message={msg}")

    async def produce(self, data: any):
        self._p.produce(settings.kafka_topic, data, callback=self._delivery_report)
