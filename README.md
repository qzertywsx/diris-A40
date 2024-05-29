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
print("THD:           ", diris.getTHD())
print("Total active power: {:.2f} kW".format(diris.getTotalPower()['P']))
print("Total reactive power: {:.2f} kVAr".format(diris.getTotalPower()['Q']))
print("Cosfi: {:.3f}".format(diris.getCosfi()['Cosfi tot']))
diris.disconnect()
```
Result of executing the above code:
```
Voltage:        {'U12': 15298.95, 'U23': 15306.3, 'U31': 15387.3, 'U1': 8821.05, 'U2': 8829.45, 'U3': 8903.55}
Current:        {'I1': 6.462, 'I2': 7.47, 'I3': 7.164, 'In': 0.0}
Power:          {'P': -168.88, 'Q': -79.11, 'S': 186.49}
Active power:   {'P1': -50.55, 'P2': -58.79, 'P3': -59.54}
Reactive power: {'Q1': -26.33, 'Q2': -29.9, 'Q3': -22.88}
Apparent power: {'S1': 57.0, 'S2': 65.96, 'S3': 63.78}
Energy:         {'E active': 391940, 'E reactive': 276292, 'E apparent': 546852, 'E active-': 36390, 'E reactive-': 23773}
Cosfi:          {'Cosfi tot': 0.905, 'Cosfi 1': 0.886, 'Cosfi 2': 0.891, 'Cosfi 3': 0.933}
Freq:           50.02
Hour:           {'H main': 105514, 'H energy': 105514}
THD:            {'THD U12': 0.027, 'THD U23': 0.031, 'THD U31': 0.031, 'THD U1': 0.029, 'THD U2': 0.028, 'THD U3': 0.033, 'THD I1': 0.291, 'THD I2': 0.213, 'THD I3': 0.244, 'THD In': 0.0}
Total active power: -168.88 kW
Total reactive power: -78.16 kVAr
Cosfi: 0.912
```
The unit of measurement are:
```
Voltage:        Volt
Current:        A
Power:          kW, kVAr, kVA
Active power:   kW
Reactive power: kVAr
Apparent power: kVA
Energy:         kWh, kVARh, kVAh
Cosfi:          Unitless
Freq:           Herz
Hour:           Hour
THD:            Unitless
```
