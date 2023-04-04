import visa

rm = visa.ResourceManager()
print(rm.list_resources())
"""
inst = rm.open_resource('USB0::0x0699::0x0368::C027902::INSTR')
inst.query('*IDN?')

inst.write('SAVE:IMAG:FILEF PNG')
inst.write('HARDCOPY START')
data = inst.read_raw()

file1 = open('70khz 0.0001uf.bmp', 'wb')
file1.write(data)
file1.close()

print("Image is ready")
"""