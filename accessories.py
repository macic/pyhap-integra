# -*- coding: UTF-8 -*-
from random import randint
from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_SENSOR

from integrapy.integra import Integra
from config import Config

integra = Integra(user_code=Config.usercode, host=Config.host, port=Config.port, encoding=Config.encoding)


class ContactSensor(Accessory):
    """Contact Sensor simplest configuration"""

    category = CATEGORY_SENSOR

    def __init__(self, integra_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.integra_no = integra_no

        service = self.add_preload_service('ContactSensor')
        self.sensor_char = service.configure_char('ContactSensorState')

    @Accessory.run_at_interval(randint(10, 20))
    async def run(self):
        if self.integra_no in await integra.get_violated_zones():
            self.sensor_char.set_value(1)
        else:
            self.sensor_char.set_value(0)


class MotionSensor(Accessory):
    """Motion Sensor simplest configuration"""

    category = CATEGORY_SENSOR

    def __init__(self, integra_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.integra_no = integra_no

        service = self.add_preload_service('MotionSensor')
        self.sensor_char = service.configure_char('MotionDetected')

    @Accessory.run_at_interval(randint(1, 2))
    async def run(self):
        if self.integra_no in await integra.get_violated_zones():
            self.sensor_char.set_value(1)
        else:
            self.sensor_char.set_value(0)


class LeakSensor(Accessory):
    """Leak Sensor simplest configuration"""

    category = CATEGORY_SENSOR

    def __init__(self, integra_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.integra_no = integra_no

        service = self.add_preload_service('LeakSensor')
        self.sensor_char = service.configure_char('LeakDetected')

    @Accessory.run_at_interval(randint(1, 3))
    async def run(self):
        if self.integra_no in await integra.get_violated_zones():
            self.sensor_char.set_value(1)
        else:
            self.sensor_char.set_value(0)


class SmokeSensor(Accessory):
    """Leak Sensor simplest configuration"""

    category = CATEGORY_SENSOR

    def __init__(self, integra_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.integra_no = integra_no

        service = self.add_preload_service('SmokeSensor')
        self.sensor_char = service.configure_char('SmokeDetected')

    @Accessory.run_at_interval(randint(1, 3))
    async def run(self):
        if self.integra_no in await integra.get_violated_zones():
            self.sensor_char.set_value(1)
        else:
            self.sensor_char.set_value(0)

class CarbonDioxideSensor(Accessory):
    """Leak Sensor simplest configuration"""

    category = CATEGORY_SENSOR

    def __init__(self, integra_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.integra_no = integra_no

        service = self.add_preload_service('CarbonDioxideSensor')
        self.sensor_char = service.configure_char('CarbonDioxideDetected')

    @Accessory.run_at_interval(randint(1, 3))
    async def run(self):
        if self.integra_no in await integra.get_violated_zones():
            self.sensor_char.set_value(1)
        else:
            self.sensor_char.set_value(0)
