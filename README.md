### Solution
Contains of two images `meter` and `pv_simulator`. Please check corresponding readme files for details.
[METER_README.md](meter%2FREADME.md) [PV_README.md](pv_simulator%2FREADME.md)
`pv_patterns` contains pv patters in black/white pngs. Which can be replaced in order to adjust pv generation patter.

### Running
Best way to run the solution is to start two containers in separate terminals

```
docker-compose up pv_simulator
```
```
docker-compose up meter
```
Output files by default will be created in `./output` folder, see [docker-compose.yml](docker-compose.yml) for details  

