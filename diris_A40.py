from pyModbusTCP.client import ModbusClient
from pyModbusTCP.utils import get_2comp, word_list_to_long

class Diris_A40:
	def __init__(self, ip, debug=False):
		self.ip = ip
		self.debug = debug
		self.client = ModbusClient(host=self.ip, port=502, timeout=3, unit_id=5, debug=self.debug)
	
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
	
	def getVoltage(self):
		U12 = self.__dataToVoltage(self.client.read_holding_registers(0xc552, 2))
		U23 = self.__dataToVoltage(self.client.read_holding_registers(0xc554, 2))
		U31 = self.__dataToVoltage(self.client.read_holding_registers(0xc556, 2))
		U1  = self.__dataToVoltage(self.client.read_holding_registers(0xc558, 2))
		U2  = self.__dataToVoltage(self.client.read_holding_registers(0xc55a, 2))
		U3  = self.__dataToVoltage(self.client.read_holding_registers(0xc55c, 2))
		return {"U12": U12, "U23": U23, "U31": U31, "U1": U1, "U2": U2, "U3": U3}
	
	def getCurrent(self):
		I1 = self.__dataToCurrent(self.client.read_holding_registers(0xc560, 2))
		I2 = self.__dataToCurrent(self.client.read_holding_registers(0xc562, 2))
		I3 = self.__dataToCurrent(self.client.read_holding_registers(0xc564, 2))
		In = self.__dataToCurrent(self.client.read_holding_registers(0xc566, 2))
		return {"I1": I1, "I2": I2, "I3": I3, "In": In}
	
	def getTotalPower(self):
		P = self.__dataToPower(self.client.read_holding_registers(0xc568, 2))
		Q = self.__dataToPower(self.client.read_holding_registers(0xc56a, 2))
		S = self.__dataToPower(self.client.read_holding_registers(0xc56c, 2))
		return {"P": P, "Q": Q, "S": S}
	
	def getActivePower(self):
		P1 = self.__dataToPower(self.client.read_holding_registers(0xc570, 2))
		P2 = self.__dataToPower(self.client.read_holding_registers(0xc572, 2))
		P3 = self.__dataToPower(self.client.read_holding_registers(0xc574, 2))
		return {"P1": P1, "P2": P2, "P3": P3}
	
	def getReactivePower(self):
		Q1 = self.__dataToPower(self.client.read_holding_registers(0xc576, 2))
		Q2 = self.__dataToPower(self.client.read_holding_registers(0xc578, 2))
		Q3 = self.__dataToPower(self.client.read_holding_registers(0xc57a, 2))
		return {"Q1": Q1, "Q2": Q2, "Q3": Q3}
	
	def getApparentPower(self):
		S1 = self.__dataToPower(self.client.read_holding_registers(0xc57c, 2))
		S2 = self.__dataToPower(self.client.read_holding_registers(0xc57e, 2))
		S3 = self.__dataToPower(self.client.read_holding_registers(0xc580, 2))
		return {"S1": S1, "S2": S2, "S3": S3}
	
	def getCosfi(self):
		Cosfi_Tot = self.__dataToCosfi(self.client.read_holding_registers(0xc56e, 2))
		Cosfi_1   = self.__dataToCosfi(self.client.read_holding_registers(0xc582, 2))
		Cosfi_2   = self.__dataToCosfi(self.client.read_holding_registers(0xc584, 2))
		Cosfi_3   = self.__dataToCosfi(self.client.read_holding_registers(0xc586, 2))
		return {"Cosfi tot": Cosfi_Tot, "Cosfi 1": Cosfi_1, "Cosfi 2": Cosfi_2, "Cosfi 3": Cosfi_3}
	
	def getEnergy(self):
		E_Active        = self.__dataToEnergy(self.client.read_holding_registers(0xc65c, 2))
		E_Reactive      = self.__dataToEnergy(self.client.read_holding_registers(0xc65e, 2))
		E_Apparent      = self.__dataToEnergy(self.client.read_holding_registers(0xc660, 2))
		E_ActiveMinus   = self.__dataToEnergy(self.client.read_holding_registers(0xc662, 2))
		E_ReactiveMinus = self.__dataToEnergy(self.client.read_holding_registers(0xc664, 2))
		return {"E active": E_Active, "E reactive": E_Reactive, "E apparent": E_Apparent, "E active-": E_ActiveMinus, "E reactive-": E_ReactiveMinus}
	
	def getHour(self):
		H_Main   = self.__dataToEnergy(self.client.read_holding_registers(0xc550, 2))
		H_Energy = self.__dataToEnergy(self.client.read_holding_registers(0xc650, 2))
		return {"H main": H_Main, "H energy": H_Energy}
	
	def getFrequency(self):
		return self.__dataToFrequency(self.client.read_holding_registers(0xc55e, 2))
