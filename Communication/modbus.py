from pymodbus.client.sync import ModbusTcpClient
import time

MODBUS_PORT = 502

class ClientModbus(ModbusTcpClient):
	def __init__(self, addr, port = MODBUS_PORT):
		ModbusTcpClient.__init__(self, addr, port)

	def read(self, addr):
		rq = self.read_coils(addr, 5)
		return rq.bits

	def write(self, addr, data):
		rq = self.write_coil(addr, data, unit=0x6)

client = ClientModbus("192.168.10.2")
