from braubuddy.envcontroller import IEnvController
from braubuddy.envcontroller import PercentageError

import relayctl
import usb

class RelayHeaterController(IEnvController):
    """
    A dummy EnvController. Use for testing.
    """

    def __init__(self):
        self._heater_percent = 0
        self._cooler_percent = 0
        print ("new relay")

    def _relayset(self, bool):
        devices = relayctl.connect()
        usb.util.dispose_resources(devices[0])
        relayctl.enable(devices[0])
        if bool:
            relayctl.switchon(devices[0], 1)
            relayctl.getstatus(devices[0], 1)
        else:
            relayctl.switchoff(devices[0], 1)
            relayctl.getstatus(devices[0], 1)
        relayctl.disable(devices[0])
        if devices[0].is_kernel_driver_active(0):
            devices[0].detach_kernel_driver(0)

    def set_heater_level(self, percent):
        if percent not in list(range(0, 101)):
            msg = '{0} is not in range 0-100'.format(percent)
            raise PercentageError(msg)
        print("heater set to {0}".format(percent))
        self._relayset(percent)
        self._heater_percent = percent

    def set_cooler_level(self, percent):

        if percent not in list(range(0, 101)):
            msg = '{0} is not in range 0-100'.format(percent)
            raise PercentageError(msg)
        self._cooler_percent = percent

    def get_power_levels(self):

        return (self._heater_percent, self._cooler_percent)

class DummyEnvController(IEnvController):
    """
    A dummy EnvController. Use for testing.
    """

    def __init__(self):

        self._heater_percent = 0
        self._cooler_percent = 0

    def set_heater_level(self, percent):

        if percent not in list(range(0, 101)):
            msg = '{0} is not in range 0-100'.format(percent)
            raise PercentageError(msg)
        print("heater set to {0}".format(percent))
        self._heater_percent = percent

    def set_cooler_level(self, percent):

        if percent not in list(range(0, 101)):
            msg = '{0} is not in range 0-100'.format(percent)
            raise PercentageError(msg)
        self._cooler_percent = percent

    def get_power_levels(self):

        return (self._heater_percent, self._cooler_percent)
