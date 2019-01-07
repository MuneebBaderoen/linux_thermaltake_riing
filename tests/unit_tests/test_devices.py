from mock import patch

from linux_thermaltake_rgb.controllers import ThermaltakeController
from linux_thermaltake_rgb.devices import ThermaltakeDevice
from base_test_object import BaseTestObject


class DeviceTest(BaseTestObject):

    @patch('linux_thermaltake_rgb.drivers.ThermaltakeControllerDriver._initialize_device', autospec=True)
    def test_device_factory(self, init_dev):
        controller = ThermaltakeController.factory('g3')
        for i, clazz in enumerate(ThermaltakeDevice.inheritors()):
            if clazz.model is None:
                continue

            dev = ThermaltakeDevice.factory(clazz.model, controller, 1)
            controller.attach_device(i, dev)
            self.assertIsInstance(ThermaltakeDevice.factory(clazz.model, controller, 1), clazz)
            self.assertTrue(init_dev.called)
