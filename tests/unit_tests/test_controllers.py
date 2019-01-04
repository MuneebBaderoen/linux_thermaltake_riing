from mock import patch

from linux_thermaltake_rgb.controllers import ThermaltakeController
from base_test_object import BaseTestObject


class ControllerTest(BaseTestObject):

    @patch('linux_thermaltake_rgb.drivers.ThermaltakeControllerDriver._initialize_device', autospec=True)
    def test_controller_factory(self, init_dev):
        for type_ in ('g3', 'iRGBPlus'):
            for case_variant in (str.lower, str.upper, str):
                self.assertIsInstance(ThermaltakeController.factory(case_variant(type_)),
                                      ThermaltakeController,
                                      '{} not recognized'.format(type_))
                self.assertTrue(init_dev.called, '{} did not initialize the driver'.format(type_))

