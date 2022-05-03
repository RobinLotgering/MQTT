from pymodbus.constants import Defaults
from pymodbus.constants import Endian
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder

Defaults.Timeout = 25
Defaults.Retries = 5
client = ModbusClient('ipaddress.of.venus', port='502')
result = client.read_input_registers(840, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
voltage = decoder.decode_16bit_uint()
print("Battery voltage: {0:.2f}V".format(voltage / 10.0))