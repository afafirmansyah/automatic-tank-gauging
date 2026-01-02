#######################################################
Automatic Tank Gauging (ATG) System
#######################################################

This project implements an **Automatic Tank Gauging** system designed for industrial liquid level monitoring. It utilizes the **Modbus Protocol** to facilitate communication between field devices (PLC) and the **Haiwell SCADA** visualization platform.

*******************
System Architecture
*******************

The system follows a standard industrial automation hierarchy:
1. **Field Level:** Level sensors or transmitters.
2. **Control Level:** PLC (Programmable Logic Controller) programmed to read sensor data.
3. **Supervisory Level:** Haiwell SCADA for HMI visualization and data logging.
4. **Connectivity:** MQTT protocol integration for remote monitoring and IoT capabilities.

*******************
Key Features
*******************

- **Real-time Monitoring:** Live visualization of tank levels, volume, and temperature.
- **Modbus Communication:** Reliable data exchange using Modbus RTU/TCP.
- **Alarm System:** High-level and low-level alerts configured within the SCADA environment.
- **MQTT Integration:** Bridge industrial data to cloud platforms or mobile dashboards.
- **Historical Logging:** Data archiving for inventory trend analysis.

**************************
Technologies & Hardware
**************************

- **Software:** Haiwell Cloud SCADA, HaiwellHappy (PLC Programming).
- **Protocols:** Modbus RTU, Modbus TCP, MQTT.
- **Hardware:** Haiwell PLC / HMI (or compatible Modbus devices).

*******************
Project Structure
*******************

- ``/program`` : Contains the PLC logic files (e.g., .hwps).
- ``/scada`` : Haiwell SCADA project files and HMI screens.
- ``/docs`` : Wiring diagrams or communication maps.

*******************
How to Use
*******************

1. **Hardware Setup:** Ensure your PLC is wired to the sensors and connected via RS485 or Ethernet.
2. **PLC Logic:** Upload the program provided in the ``/program`` folder using HaiwellHappy.
3. **SCADA Configuration:** - Open the SCADA project in Haiwell Cloud Software.
   - Configure the IP/Com Port settings to match your hardware.
4. **Run:** Start the SCADA runtime to begin monitoring.

*******
License
*******

This project is licensed under the MIT License.

*********
Contact
*********

**Ahmad Fauzi Firmansyah**
- **GitHub:** `afafirmansyah <https://github.com/afafirmansyah>`_
- **LinkedIn:** `ahmad-fauzi-firmansyah <https://linkedin.com/in/ahmad-fauzi-firmansyah/>`_
