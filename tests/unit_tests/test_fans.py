from mock import patch

from base_test_object import BaseTestObject
from linux_thermaltake_rgb.fan_manager import FanModel, TempTargetModel, CurveModel

TempTargetModel._get_temp = (lambda self: 50)
CurveModel._get_temp = (lambda self: 50)


class FanTest(BaseTestObject):

    @patch('linux_thermaltake_rgb.drivers.ThermaltakeControllerDriver._initialize_device', autospec=True)
    def test_fan_factory(self, init_dev):

        for clazz in FanModel.inheritors():
            if clazz.model is None:
                continue

            fan = FanModel.factory({'model': clazz.model,
                                    'points': [[50, 50]],  # curve
                                    'speed': 50,  # locked_speed
                                    'target': 50,  # temp_target
                                    'multiplier': 10
                                    })
            fan.main()
            self.assertIsInstance(fan, FanModel)
