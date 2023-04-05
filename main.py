import baker
import logging
import signal
from pyhap.accessory import Bridge
from pyhap.accessory_driver import AccessoryDriver
from integrapy.integra import Integra
from integrapy.constants import ZONE
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


@baker.command
def server_start():
    # Start the accessory on port 51826
    driver = AccessoryDriver(port=51826)

    # Add whole bridge
    driver.add_accessory(accessory=get_bridge(Config.accessories, driver))

    # We want SIGTERM (terminate) to be handled by the driver itself,
    # so that it can gracefully stop the accessory, server and advertising.
    signal.signal(signal.SIGTERM, driver.signal_handler)

    # Start it!
    driver.start()


@baker.command
def list_integra(no=128):
    # helper method to list mapping between integra based port (for simplicity numbers) and their names
    integra = Integra(user_code=Config.usercode, host=Config.host, port=Config.port, encoding=Config.encoding)
    last = int(no)
    for i in range(1, last + 1):
        try:
            print("ZONE " + str(i) + " " + integra.get_name(ZONE, i).name)
        except Exception: # no more things mapped
            break


if __name__ == "__main__":
    baker.run()
