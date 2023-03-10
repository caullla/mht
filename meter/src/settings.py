import os

RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://guest:guest@broker:5672')

METER_MIN_VALUE = os.getenv('METER_MIN_VALUE', 0)
METER_MAX_VALUE = os.getenv('METER_MAX_VALUE', 9000)

METER_INTERVAL_SECONDS = os.getenv('METER_INTERVAL_SECONDS', 1)
METER_EXCHANGE_NAME = os.getenv('METER_EXCHANGE_NAME', 'meter')




