Consume `meter` data from rabbitMQ.
Using png mask generate pv values. Any image size or ration.
Height will be scaled to fit min and max value proportionally.
Width will be scaled to fix 24 hours proportionally.

##### example pattern:

![regular.png](..%2Fpv_patterns%2Fregular.png)

### Environment Variables

| Name                   | Required | Description                                                | Default                        |
|:-----------------------|----------|------------------------------------------------------------|--------------------------------|
| RABBITMQ_URL           | True     | Full url to rabbitMQ instance                              | amqp://guest:guest@broker:5672 |
| PV_SIMULATOR_MIN_VALUE | True     |                                                            | 0                              |
| PV_SIMULATOR_MAX_VALUE | True     |                                                            | 3500                           |
| PV_PATTERN_PATH        | True     | path to png image representing PV power production pattern | /pv_patterns/regular.png       |
| METER_EXCHANGE_NAME    | True     | name of rabbitMQ exchange where `meter` will push messages | 9000                           |
| PV_SIMULATOR_QUEUE     | True     | name of rabbitMQ queue to consume `meter` data             |                                |
| TIME_ZONE              | True     | timezone to be used when logging data                      | CET                            |
