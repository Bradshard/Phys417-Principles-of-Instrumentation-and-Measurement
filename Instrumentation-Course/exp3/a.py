import pyvisa as visa
import numpy as np
import pylab
from struct import unpack
rm = visa.ResourceManager()
print(rm.list_resources())


inst = rm.open_resource('USB0::0x0699::0x0368::C027902::INSTR')
print(inst.query("*IDN?"))
 
inst.write('Data:SOU CH1')
inst.write('DATA:WIDTH 1')
inst.write('DATA:ENC RPB')
"""
inst.write('Data:SOU CH2')
inst.write('DATA:WIDTH 2')
inst.write('DATA:ENC RPB')
"""
ymult = float(inst.query('WFMPRE:YMULT?'))
yzero = float(inst.query('WFMPRE:YZERO?'))
yoff = float(inst.query('WFMPRE:YOFF?'))
xincr = float(inst.query('WFMPRE:XINCR?'))
 
inst.write('CURVE?')
data= inst.read_raw()
headerlen = 2+int(data[1])
header = data[:headerlen]
ADC_wave = data[headerlen:-1]
ADC_wave=np.array(unpack('%sB' % len(ADC_wave),ADC_wave))
Volts = (ADC_wave - yoff)* ymult + yzero
Time = np.arange(0, xincr* len(Volts),xincr)
pylab.plot(Time,Volts)
pylab.show()
