import logging
import signal
from pyhap.accessory import Bridge
from pyhap.accessory_driver import AccessoryDriver

import accessories
from config import Config

logging.basicConfig(level=logging.INFO, format="[%(module)s] %(message)s)")


def get_bridge(accesories_list, driver):
    """Iterates over list of accessories and adds them to the bridge."""
    bridge = Bridge(driver, 'HAP Bridge')

    for accessory in accesories_list:
        accessory_class_ = getattr(accessories, accessory.accesory_type)
        accessory_instance = accessory_class_(integra_no=accessory.number, display_name=accessory.name, driver=driver)
        bridge.add_accessory(accessory_instance)

    return bridge


# Start the accessory on port 51826
driver = AccessoryDriver(port=51826)

driver.add_accessory(accessory=get_bridge(Config.accessories, driver))

# We want SIGTERM (terminate) to be handled by the driver itself,
# so that it can gracefully stop the accessory, server and advertising.
signal.signal(signal.SIGTERM, driver.signal_handler)

# Start it!
driver.start()
