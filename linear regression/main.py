import pickle
import time
import tkinter
import numpy as np
from pyModbusTCP.client import ModbusClient
from typing import Text

# TCP auto connect on first modbus request
c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)

while True:
    regs = c.read_holding_registers(0)
    if regs:
        data_in = [regs]
        convert_in_to_array = np.asarray(data_in)
        print(convert_in_to_array)
        data_load = pickle.load(open('finalized_model.sav', 'rb'))
        prediction = data_load.predict(convert_in_to_array)
        print(prediction)
        data_out = int(np.asscalar(prediction))
        print(data_out)
        c.write_multiple_registers(10, [data_out])
        time.sleep(5)
    else:
        print("read error")
        time.sleep(5)
