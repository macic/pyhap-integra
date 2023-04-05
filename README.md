HAP-Python (https://github.com/ikalchev/HAP-python) accessories implementation for Satel Integra device controls based on framing and initial bytes array implementation by https://github.com/mkorz/IntegraPy. 


Not intended for commercial use.

##Usage

Please make sure your integra ETHM-1 module has enabled Integration setting (port 7094) - that can be achieved through DLOADX.

**Start with listing items** you can spin up as HomeKit accessories:

`python main.py list_integra` 

**Amend** `config.py` providing Integra details and mapping items to available accessory types. List of accessories implemented can be found in `accessories.py`

To **run the server** and create a HomeKit bridge with all your accessories from config:

`python main.py server_start`
