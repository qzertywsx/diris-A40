# diris_A40
A library for reading values ​​from Socomec Diris A40 via Modbus TCP

# Example

```python
from diris_A40 import Diris_A40

diris = Diris_A40('IP address')
if diris.check_connection():
	print(diris)
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
	print("\nTotal active power: {:.2f} kW".format(diris.getTotalPower()['P']))
	print("Total reactive power: {:.2f} kVAr".format(diris.getTotalPower()['Q']))
	print("Cosfi: {:.3f}".format(diris.getCosfi()['Cosfi tot']))
	diris.disconnect()
```
Result of executing the above code:
```
Diris A40 Addr: 192.168.70.217, Connected: True
Voltage:        {'U12': 15495.0, 'U23': 15511.05, 'U31': 15529.35, 'U1': 8914.2, 'U2': 8952.9, 'U3': 9000.15}
Current:        {'I1': 29.688, 'I2': 28.488, 'I3': 29.808, 'In': 0.0}
Power:          {'P': 582.99, 'Q': 529.95, 'S': 787.86}
Active power:   {'P1': 200.03, 'P2': 186.91, 'P3': 196.04}
Reactive power: {'Q1': 173.28, 'Q2': 173.53, 'Q3': 183.14}
Apparent power: {'S1': 264.65, 'S2': 255.05, 'S3': 268.28}
Energy:         {'E active': 392616, 'E reactive': 277124, 'E apparent': 547993, 'E active-': 36423, 'E reactive-': 23784}
Cosfi:          {'Cosfi tot': 0.739, 'Cosfi 1': 0.755, 'Cosfi 2': 0.732, 'Cosfi 3': 0.73}
Freq:           50.0
Hour:           {'H main': 105674, 'H energy': 105674}
THD:            {'THD U12': 0.026, 'THD U23': 0.027, 'THD U31': 0.028, 'THD U1': 0.027, 'THD U2': 0.026, 'THD U3': 0.028, 'THD I1': 0.194, 'THD I2': 0.194, 'THD I3': 0.194, 'THD In': 0.0}

Total active power: 582.99 kW
Total reactive power: 651.12 kVAr
Cosfi: 0.770
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
