from collections import namedtuple

Accessory = namedtuple("Accessory", ("name", "number", "accesory_type"))

class Config:
    # Integra values
    usercode = "1234"
    host = "192.168.1.1"
    port = 7094
    encoding = "cp1250"

    accessories = [
        Accessory("Ruch Korytarz", 1, "MotionSensor"),
        Accessory("Stłuczenia Gabinet", 2, "ContactSensor"), #possibly wrong type
        Accessory("Dym Strych", 3, "SmokeSensor"),
    ]

