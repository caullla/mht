import json
import logging
import sys
import time

import numpy as np
import pika

import settings

logger = logging.getLogger('meter')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def main() -> None:
    params = pika.URLParameters(settings.RABBITMQ_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    logger.info('connected to rabbit mq')

    exchange = settings.METER_EXCHANGE_NAME

    channel.exchange_declare(
        exchange=exchange,
        exchange_type='direct'
    )

    while True:
        power = round(np.random.uniform(settings.METER_MIN_VALUE, settings.METER_MAX_VALUE), 2)
        channel.basic_publish(
            exchange=exchange,
            routing_key='',
            body=json.dumps({
                'power': power
            }).encode()
        )
        logger.info(f'send: {power}')
        time.sleep(settings.METER_INTERVAL_SECONDS)


if __name__ == '__main__':
    main()
