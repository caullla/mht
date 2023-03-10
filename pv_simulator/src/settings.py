import os

RABBITMQ_URL = os.getenv('RABBITMQ_URL')

PV_SIMULATOR_MIN_VALUE = os.getenv('PV_SIMULATOR_MIN_VALUE', 0)
PV_SIMULATOR_MAX_VALUE = os.getenv('PV_SIMULATOR_MAX_VALUE', 0)

METER_EXCHANGE_NAME = os.getenv('METER_EXCHANGE_NAME', 'meter')

PV_SIMULATOR_QUEUE = os.getenv('PV_SIMULATOR_QUEUE', 'pv_simulator')

PV_PATTERN_PATH = os.getenv('PV_PATTERN_PATH', '/pv_patterns/regular.png')
PV_LOG_FILE = '/output/pv_simulator.log'

TIME_ZONE = os.getenv('TIME_ZONE', 'CET')
