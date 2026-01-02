#######################################################
Automatic Tank Gauging (ATG) System
#######################################################

This project implements an **Automatic Tank Gauging** system designed for industrial liquid level monitoring. It utilizes the **Modbus Protocol** to facilitate communication between field devices (PLC) and the **Haiwell SCADA** visualization platform.

*******************
Key Features
*******************

- **Real-time Monitoring:** Live visualization of tank levels, volume, and temperature status.
- **Modbus Communication:** Reliable data exchange using Modbus RTU/TCP protocols.
- **MQTT Integration:** Seamless data bridging to cloud platforms for remote IoT monitoring.
- **Alarm System:** Automated alerts for high-level and low-level inventory thresholds.

**************************
Technical Specifications
**************************

- **Software:** Haiwell Cloud SCADA & HaiwellHappy (PLC Programming)
- **Protocols:** Modbus RTU, Modbus TCP, and MQTT
- **Hardware:** Haiwell PLC / HMI (or compatible Modbus-enabled devices)
- **Application:** Industrial Inventory and Fuel Tank Monitoring

*******************
Installation Guide
*******************

1. **Clone the Project**
   .. code-block:: bash

      git clone https://github.com/afafirmansyah/automatic-tank-gauging.git

2. **Hardware Setup**
   - Connect your sensors to the PLC analog/digital input modules.
   - Ensure the RS485 or Ethernet communication cable is properly wired between the PLC and the SCADA PC/HMI.

3. **PLC Configuration**
   - Open the project file in the ``/program`` folder using **HaiwellHappy**.
   - Compile and download the logic to your PLC hardware.

4. **SCADA Configuration**
   - Open the SCADA project using **Haiwell Cloud Software**.
   - Update the Communication Settings (IP Address or COM Port) to match your hardware configuration.

5. **Launch**
   - Run the SCADA project to start the real-time monitoring dashboard.

*******
License
*******

This project is licensed under the MIT License - see the `license.txt` file for details.

*********
Contact
*********

**Ahmad Fauzi Firmansyah**
- **GitHub:** `afafirmansyah <https://github.com/afafirmansyah>`_
- **LinkedIn:** `ahmad-fauzi-firmansyah <https://linkedin.com/in/ahmad-fauzi-firmansyah/>`_
