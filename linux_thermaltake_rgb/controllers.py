from linux_thermaltake_rgb import drivers, LOGGER
from linux_thermaltake_rgb.classified_object import ClassifiedObject


class ThermaltakeController(ClassifiedObject):
    def __init__(self):
        self.devices = {}
        self.driver = None

    @classmethod
    def factory(cls, unit_type, unit_identifier=None):
        subclass_dict = {clazz.model: clazz for clazz in cls.inheritors()}
        try:
            # TODO: remove copy pasta
            if unit_identifier is not None:
                return subclass_dict.get(unit_type.lower())(unit=unit_identifier)
            else:
                return subclass_dict.get(unit_type.lower())()
        except KeyError as e:
            LOGGER.warn('%s not a valid controller type', e)

    def attach_device(self, port=None, dev=None):
        self.devices[port] = dev
        return self.devices[port]

    def save_profile(self):
        self.driver.save_profile()


class ThermaltakeG3Controller(ThermaltakeController):
    model = 'g3'

    def __init__(self, unit=1):
        super().__init__()
        self.unit = unit
        self.ports = 5
        self.driver = drivers.ThermaltakeG3ControllerDriver(unit)

