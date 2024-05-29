from pyModbusTCP.client import ModbusClient
from pyModbusTCP.utils import get_2comp, word_list_to_long

class Diris_A40:
	def __init__(self, ip, debug=False):
		self.ip = ip
		self.debug = debug
		self.client = ModbusClient(host=self.ip, port=502, timeout=3, unit_id=5, debug=self.debug)

	def __str__(self):
		return "Diris A40 Addr: " + self.ip + ", Connected: " + str(self.client.is_open)

	def check_connection(self):
		self.client.open()
		return self.client.is_open
	
	def disconnect(self):
		self.client.close()
	
	def __getint32(self,data):
		temp = word_list_to_long(data)[0]
		temp = get_2comp(temp, val_size=32)
		return temp
	
	def __dataToVoltage(self,data):
		return self.__getint32(data)/100
	
	def __dataToCurrent(self,data):
		return self.__getint32(data)/1000
	
	def __dataToCosfi(self,data):
		return self.__getint32(data)/1000
	
	def __dataToPower(self,data):
		return self.__getint32(data)/100
	
	def __dataToEnergy(self,data):
		return self.__getint32(data)
	
	def __dataToFrequency(self,data):
		return self.__getint32(data)/100
		
	def __dataToHarminic(self,data):
		return data[0]/1000
	
	def getVoltage(self):
		try:
			U12 = self.__dataToVoltage(self.client.read_holding_registers(0xc552, 2))
			U23 = self.__dataToVoltage(self.client.read_holding_registers(0xc554, 2))
			U31 = self.__dataToVoltage(self.client.read_holding_registers(0xc556, 2))
			U1  = self.__dataToVoltage(self.client.read_holding_registers(0xc558, 2))
			U2  = self.__dataToVoltage(self.client.read_holding_registers(0xc55a, 2))
			U3  = self.__dataToVoltage(self.client.read_holding_registers(0xc55c, 2))
			return {"U12": U12, "U23": U23, "U31": U31, "U1": U1, "U2": U2, "U3": U3}
		except:
			return False
	
	def getCurrent(self):
		try:
			I1 = self.__dataToCurrent(self.client.read_holding_registers(0xc560, 2))
			I2 = self.__dataToCurrent(self.client.read_holding_registers(0xc562, 2))
			I3 = self.__dataToCurrent(self.client.read_holding_registers(0xc564, 2))
			In = self.__dataToCurrent(self.client.read_holding_registers(0xc566, 2))
			return {"I1": I1, "I2": I2, "I3": I3, "In": In}
		except:
			return False
	
	def getTotalPower(self):
		try:
			P = self.__dataToPower(self.client.read_holding_registers(0xc568, 2))
			Q = self.__dataToPower(self.client.read_holding_registers(0xc56a, 2))
			S = self.__dataToPower(self.client.read_holding_registers(0xc56c, 2))
			return {"P": P, "Q": Q, "S": S}
		except:
			return False
	
	def getActivePower(self):
		try:
			P1 = self.__dataToPower(self.client.read_holding_registers(0xc570, 2))
			P2 = self.__dataToPower(self.client.read_holding_registers(0xc572, 2))
			P3 = self.__dataToPower(self.client.read_holding_registers(0xc574, 2))
			return {"P1": P1, "P2": P2, "P3": P3}
		except:
			return False
	
	def getReactivePower(self):
		try:
			Q1 = self.__dataToPower(self.client.read_holding_registers(0xc576, 2))
			Q2 = self.__dataToPower(self.client.read_holding_registers(0xc578, 2))
			Q3 = self.__dataToPower(self.client.read_holding_registers(0xc57a, 2))
			return {"Q1": Q1, "Q2": Q2, "Q3": Q3}
		except:
			return False
	
	def getApparentPower(self):
		try:
			S1 = self.__dataToPower(self.client.read_holding_registers(0xc57c, 2))
			S2 = self.__dataToPower(self.client.read_holding_registers(0xc57e, 2))
			S3 = self.__dataToPower(self.client.read_holding_registers(0xc580, 2))
			return {"S1": S1, "S2": S2, "S3": S3}
		except:
			return False
	
	def getCosfi(self):
		try:
			Cosfi_Tot = self.__dataToCosfi(self.client.read_holding_registers(0xc56e, 2))
			Cosfi_1   = self.__dataToCosfi(self.client.read_holding_registers(0xc582, 2))
			Cosfi_2   = self.__dataToCosfi(self.client.read_holding_registers(0xc584, 2))
			Cosfi_3   = self.__dataToCosfi(self.client.read_holding_registers(0xc586, 2))
			return {"Cosfi tot": Cosfi_Tot, "Cosfi 1": Cosfi_1, "Cosfi 2": Cosfi_2, "Cosfi 3": Cosfi_3}
		except:
			return False
	
	def getEnergy(self):
		try:
			E_Active        = self.__dataToEnergy(self.client.read_holding_registers(0xc65c, 2))
			E_Reactive      = self.__dataToEnergy(self.client.read_holding_registers(0xc65e, 2))
			E_Apparent      = self.__dataToEnergy(self.client.read_holding_registers(0xc660, 2))
			E_ActiveMinus   = self.__dataToEnergy(self.client.read_holding_registers(0xc662, 2))
			E_ReactiveMinus = self.__dataToEnergy(self.client.read_holding_registers(0xc664, 2))
			return {"E active": E_Active, "E reactive": E_Reactive, "E apparent": E_Apparent, "E active-": E_ActiveMinus, "E reactive-": E_ReactiveMinus}
		except:
			return False
	
	def getHour(self):
		try:
			H_Main   = self.__dataToEnergy(self.client.read_holding_registers(0xc550, 2))
			H_Energy = self.__dataToEnergy(self.client.read_holding_registers(0xc650, 2))
			return {"H main": H_Main, "H energy": H_Energy}
		except:
			return False
	
	def getFrequency(self):
		try:
			return self.__dataToFrequency(self.client.read_holding_registers(0xc55e, 2))
		except:
			return False

	def getTHD(self):
		try:
			THD_U12 = self.__dataToHarminic(self.client.read_holding_registers(0xc950, 1))
			THD_U23 = self.__dataToHarminic(self.client.read_holding_registers(0xc951, 1))
			THD_U31 = self.__dataToHarminic(self.client.read_holding_registers(0xc952, 1))
			THD_U1  = self.__dataToHarminic(self.client.read_holding_registers(0xc953, 1))
			THD_U2  = self.__dataToHarminic(self.client.read_holding_registers(0xc954, 1))
			THD_U3  = self.__dataToHarminic(self.client.read_holding_registers(0xc955, 1))
			THD_I1  = self.__dataToHarminic(self.client.read_holding_registers(0xc956, 1))
			THD_I2  = self.__dataToHarminic(self.client.read_holding_registers(0xc957, 1))
			THD_I3  = self.__dataToHarminic(self.client.read_holding_registers(0xc958, 1))
			THD_In  = self.__dataToHarminic(self.client.read_holding_registers(0xc959, 1))
			return {"THD U12": THD_U12, "THD U23": THD_U23, "THD U31": THD_U31, "THD U1": THD_U1, "THD U2": THD_U2, "THD U3": THD_U3, "THD I1": THD_I1, "THD I2": THD_I2, "THD I3": THD_I3, "THD In": THD_In}
		except:
			return False
