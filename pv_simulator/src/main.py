import json
import logging
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler

import pika
import pytz

import settings
from helper import load_data
from pv_simulator import PVSimulator

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

# define a logging handler with file rotation at 1GB
handler = RotatingFileHandler(settings.PV_LOG_FILE, maxBytes=1024 * 1024 * 1024, backupCount=200)
logger.addHandler(handler)

stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

data = load_data(
    pattern_path=settings.PV_PATTERN_PATH,
    min_val=settings.PV_SIMULATOR_MIN_VALUE,
    max_val=settings.PV_SIMULATOR_MAX_VALUE
)
simulator = PVSimulator(data)


def on_message(
        ch: pika.spec.Channel,
        method: pika.spec.Basic.Deliver,
        properties: pika.spec.BasicProperties,
        body: bytes
) -> None:
    # read message from broker
    meter_power = json.loads(body)['power']

    current_dt = datetime.now(tz=pytz.timezone(settings.TIME_ZONE))
    pv_power = simulator.draw_value_with_deviation(current_dt)
    sum_power = meter_power + pv_power
    logger.info(f'{current_dt.isoformat()} {meter_power} {pv_power} {sum_power}')


def main() -> None:
    params = pika.URLParameters(settings.RABBITMQ_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    exchange = settings.METER_EXCHANGE_NAME
    queue = settings.PV_SIMULATOR_QUEUE

    channel.exchange_declare(
        exchange=exchange,
        exchange_type='direct'
    )
    channel.queue_declare(queue=queue, exclusive=True)
    channel.queue_bind(
        exchange=exchange,
        queue=queue,
        routing_key=''
    )

    channel.basic_consume(queue=queue, on_message_callback=on_message, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    main()
