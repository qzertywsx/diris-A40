# diris_A40
A library for reading values ​​from Socomec Diris A40 via Modbus TCP

# Example

```
from diris_A40 import Diris_A40

diris = Diris_A40('IP address')
print("Voltage:       ", diris.getVoltage())
print("Current:       ", diris.getCurrent())
print("Power:         ", diris.getTotalPower())
print("Active power:  ", diris.getActivePower())
print("Reactive power:", diris.getReactivePower())
print("Apparent power:", diris.getApparentPower())
print("Energy:        ", diris.getEnergy())
print("Cosfi:         ", diris.getCosfi())
print("Freq:          ", diris.getFrequency())
print("Hour:          ", diris.getHour())
print("Total active power: {:.2f} kW".format(diris.getTotalPower()['P']))
print("Total reactive power: {:.2f} kVAr".format(diris.getTotalPower()['Q']))
print("Cosfi: {:.3f}".format(diris.getCosfi()['Cosfi tot']))
diris.disconnect()
```
Result of executing the above code:
```
Voltage:        {'U12': 404.76, 'U23': 405.04, 'U31': 404.71, 'U1': 233.55, 'U2': 233.79, 'U3': 233.86}
Current:        {'I1': 94.016, 'I2': 87.712, 'I3': 86.224, 'In': 0.0}
Power:          {'P': 46.72, 'Q': 41.71, 'S': 62.63}
Active power:   {'P1': 16.41, 'P2': 15.39, 'P3': 14.92}
Reactive power: {'Q1': 14.59, 'Q2': 13.55, 'Q3': 13.56}
Apparent power: {'S1': 21.96, 'S2': 20.51, 'S3': 20.16}
Energy:         {'E active': 7476757, 'E reactive': 4688014, 'E apparent': 9580525, 'E active-': 25, 'E reactive-': 146047}
Cosfi:          {'Cosfi tot': 0.745, 'Cosfi 1': 0.747, 'Cosfi 2': 0.75, 'Cosfi 3': 0.739}
Freq:           50.01
Hour:           {'H main': 9091042, 'H energy': 9091042}
Total active power: 46.72 kW
Total reactive power: 41.71 kVAr
Cosfi: 0.745
```
