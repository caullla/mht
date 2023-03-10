Produces random value about power consumption in range between min and max and send it to rabbitMQ.

### Environment Variables

| Name                   | Required | Description                                                | Default                        |
|:-----------------------|----------|------------------------------------------------------------|--------------------------------|
| RABBITMQ_URL           | True     | Full url to rabbitMQ instance                              | amqp://guest:guest@broker:5672 |
| METER_EXCHANGE_NAME    | True     | name of rabbitMQ exchange where `meter` will push messages | meter                          |
| METER_MIN_VALUE        | True     |                                                            | 0                              |
| METER_MAX_VALUE        | True     |                                                            | 9000                           |
| METER_INTERVAL_SECONDS | True     | how often meter will generate power consumption message    |                                |
