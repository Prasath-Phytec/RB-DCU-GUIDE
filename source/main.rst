==================
RB-DCU i.MX 6ULL
==================



RB-DCU i.MX 6ULL Board Top View
===============================

.. raw:: latex

   \vspace{7em}
   

.. figure:: ../images/image/top.jpeg
   :alt: RB-DCU i.MX 6ULLL Top View
   :width: 800px
   :align: center
   
.. raw:: html

   <div style="text-align:center; margin-top:10px; font-style: italic; font-weight: bold;">
     Figure 1
   </div>

   
.. raw:: latex

   \vspace{7em}

RB-DCU i.MX 6ULL Board Bottom View
===================================


.. figure:: ../images/image/bottom.jpeg
   :alt: RB-DCU i.MX 6ULLL Bottom View
   :width: 800px
   :align: center

   **Figure 2**


RB-DCU i.MX 6ULL Board Hardware Details
=======================================

.. raw:: latex

   \vspace{7em}

.. csv-table::
   :header: "Req", "Hardware", "Part No", "Interface", "Connector", "Remarks"
   :widths: 6, 20, 18, 18, 10, 40

   "HWR1", "Boot Mode", "", "Mode-0 & Mode-1", "P1", "(2+3) Internal Boot, (1+2) Serial Boot"
   "HWR2", "Power Session", "", "Circuit --DC 5V", "P2", ""
   "HWR3", "External RTC", "RV-4162-C7", "I2C2", "P3", "(2+3) External RTC"
   "HWR4", "Internal RTC", "", "SOM RTC", "P3", "(1+2) Internal RTC"
   "HWR5", "User LED", "RGB LED", "GPIO", "D4, D7", "GPIO02_11(), GPIO02_12()"
   "HWR6", "User Switch", "", "GPIO", "SW1", "GPIO02_08()"
   "HWR7", "Reset Switch", "", "GPIO", "SW2", "SOM Reset available; Additional GPIO01_13() (DNM)"
   "HWR8", "Power ON Indication", "", "Panel LED", "D3", "Board Power ON Indication"
   "HWR9", "Mini PCIe", "", "USB1", "P8", "Contains eSIM(DNM), SIM, USB-1, SOM Reset, GPIO Reset GPIO01_04"
   "HWR10", "Micro SIM Socket", "", "DATA & CLK signals", "J4", ""
   "HWR11", "eSIM", "", "DATA & CLK signals", "U16", "Chip not mounted"
   "HWR12", "WiFi Module", "LILY-W131", "USB2", "U18", "GPIO5_0 Power Seq, GPIO1_18 Radio Ctrl, Wakeup, Power Enable GPIO"
   "HWR13", "Ethernet", "", "Ethernet PHY", "J3", ""
   "HWR14", "RS232", "", "UART2", "P4", ""
   "HWR15", "RS485", "", "UART6", "P4", ""
   "HWR16", "Optical UART", "", "UART7", "D31, D30", ""
   "HWR17", "RF Connector 1", "", "UART4", "P9", ""
   "HWR18", "RF Connector 1 GPIOs", "", "GPIO", "P9", ""
   "HWR19", "RF Connector 2", "", "UART3", "P12", ""
   "HWR20", "RF Connector 2 GPIOs", "", "GPIO", "P12", ""
   "HWR21", "TPM", "SLB_9672XU2.0_UQFN_32P", "SPI2, GPIO", "U24", "Disable I2C and test SPI functionality"
   "HWR22", "TPM", "SLB_9672XU2.0_UQFN_32P", "I2C2, GPIO", "U24", "Disable SPI and test I2C functionality"
   "HWR23", "Accelerometer, Gyroscope (3-Axis)", "LSM6DSLTR", "I2C1, GPIO", "U23", ""
   "HWR24", "Tamper Pins", "", "GPIO", "", ""
   "HWR25", "SPI-LCD Header", "", "SPI1", "P10", ""
   "HWR26", "Digital Input Header", "", "GPIO", "P5", ""
   "HWR27", "Micro SD Card", "", "SDIO", "J2", ""
   "HWR28", "TTL Debug Port", "Debug_Port", "UART1", "J1", ""
   "HWR29", "Bluetooth", "BGM220PC22HNA2", "UART5, Watchdog", "U14", ""
   "HWR30", "Bluetooth Power Switch", "TPS22965NDSGR", "GPIO5_3_BLE_PWR_EN", "U15", ""
   "HWR31", "Li-ion Battery Charger", "", "GPIO1_3_ADC1_IN3", "P7", ""
   "HWR32", "Boot Mode Configuration Selection", "61300211121", "eMMC, SD Card", "J9", ""

.. raw:: latex

   \vspace{7em}

RB-DCU i.MX 6ULL Board Block Diagram
=======================================


.. raw:: latex

   \vspace{7em}


.. raw:: html

   <div style="text-align: center; margin-bottom: 5px; margin-left: 90px; margin-top: 40px;">
     <img src="_static/dcu_block.jpeg" alt="RB-DCU i.MX 6ULL Block Diagram" style="width: 900px;" />
   </div>

.. raw:: html

   <div style="margin-top: 10px; text-align: center; font-style: italic; font-weight: bold;">
     Figure 3
   </div>


Power Supply Connections
========================

Power Supply Connector (P2)
----------------------------

Power management for RB-DCU i.MX 6ULL-1P1 is come up with either USB or
DC 5V.



.. figure:: ../images/image/powersupply.jpeg
   :alt: Power Supply Connector
   :width: 250px
   :align: center

   **Figure 4: Power Supply Connector (P2)**

.. raw:: html

   <br>


+-------------------+--------------------+---------------+--------------+----------------------+
| Connector Pin No  | SOM Signal         | Signal Level  | Signal Type  | Description          |
+===================+====================+===============+==============+======================+
| 1                 | VCC5V_MAIN         | 5V            | PWR          | +5V power supply     |
+-------------------+--------------------+---------------+--------------+----------------------+
| 2                 | GND                | N/A           | N/A          | Ground               |
+-------------------+--------------------+---------------+--------------+----------------------+
| 3                 | SHIELD             | N/A           | N/A          | Shield               |
+-------------------+--------------------+---------------+--------------+----------------------+

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 4: Pin Assignment of P2
   </div>

.. raw:: html

   <br>

.. note::
   By default, the board uses the 5 V DC adapter as its primary power source.


Power Supply LED (D3)
---------------------
The LED D3 indicates the presence of the 3.3 V supply voltage generated from
the 5V input voltage.


.. figure:: ../images/image/po_led.jpeg
   :alt: Power Supply LED
   :width: 300px
   :align: center

   **Figure 5: Power Supply LED (D3)**

.. tip::
   After applying power, D3 should light up almost immediately—if it doesn’t, check that your 5 V adapter is delivering the correct voltage and that the barrel jack is firmly seated.




TTL Debug Port (J1)
======================
This port usually provides a **serial communication interface** that follows the
**UART1 (Universal Asynchronous Receiver-Transmitter)** protocol with TTL
voltage levels.


.. figure:: ../images/image/debug.jpeg
   :alt: TTL Debug Port (J1)
   :width: 300px
   :align: center

   **Figure 6: TTL Debug Port (J1)**

.. raw:: html

   <br>



+--------------------+-------------------+----------------------+--------------+--------------+--------------------------------------+
| Connector Pin No   | Connector Signal  | SOM Signal           | Signal Level | Signal Type  | Description                          |
+====================+===================+======================+==============+==============+======================================+
| 1                  | TX                | X_UART1_RX_DBG       | 3.3V         | IN           | Debug UART receive (from SOM)        |
+--------------------+-------------------+----------------------+--------------+--------------+--------------------------------------+
| 2                  | RX                | X_UART1_TX_DBG       | 3.3V         | OUT          | Debug UART transmit (from SOM)       |
+--------------------+-------------------+----------------------+--------------+--------------+--------------------------------------+
| 3                  | GND               | GND                  | NA           | NA           | Ground reference                     |
+--------------------+-------------------+----------------------+--------------+--------------+--------------------------------------+

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 6: Pin Assignment of J1
   </div>

.. raw:: html

   <br>
.. note::
   The TTL debug port (J1) uses 3.3 V logic levels (TX, RX, GND). Do **not** connect it directly to RS-232 interfaces—use a USB-to-TTL serial adapter or level shifter to prevent damage.


Boot Mode Configuration Selection (J9)
======================================

The RB-DCU i.MX 6ULL-1P1 has two defined boot sequences which can be
selected by configuring jumper J9.

.. warning::
   If J9 is left open (eMMC boot) and no valid image is present on the on-board flash, the board will hang during startup. Always confirm your boot media contains a valid bootloader.

.. figure:: ../images/image/bootmode.jpeg
   :alt: Boot Mode Selection Jumper J9
   :width: 300px
   :align: center

   **Figure 7: Boot Mode Selection Jumper (J9)**

.. raw:: html

   <br>

+-----------------------------+------------------+
| Boot mode                   | Description      |
+=============================+==================+
| Boot mode 1(with jumper)    | MMC boot         |
+-----------------------------+------------------+
| Boot mode 2(without jumper) | EMMC boot        |
+-----------------------------+------------------+

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 7: Pin Assignment of J9
   </div>

.. raw:: html

   <br>
.. note::
   Jumper J9 selects between SD-card (MMC) boot and on-board eMMC boot. Ensure the board is **powered off** before changing the jumper position to avoid unintended writes or boot failures.


System Reset Button (SW2)
============================

The RB-DCU i.MX 6ULL-1P1 is equipped with a system reset button at SW2.
Pressing this button will toggle the **X_nRESET_IN**,causing the module to
reset.Additionally,the reset signal **X_nRESET_OUT(X_RESET#)** is generated on
the module to also reset the peripherals on the carrier board.

.. warning::
   Pressing SW2 abruptly restarts the CPU and peripherals without a clean shutdown—unsaved data in volatile memory or on attached storage may be lost. Use it sparingly and only when necessary.
.. raw:: html

   <br>
.. figure:: ../images/image/reset.jpeg
   :alt: System Reset Button S2
   :width: 300px
   :align: center

   **Figure 8: System Reset Button (SW2)**

.. raw:: html

   <br>

.. csv-table::
   :header: "Connector Pin No","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 15, 25, 15, 15, 30

   "1","X_nRESET_IN","3.3V","IN","System reset input (active low)"
   "2","GND","N/A","N/A","Ground reference"


.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 8: Pin Assignment of SW2
   </div>

Li-ion Battery Charger (P7)
============================

External Li-ion battery (3.7V) is used to boot the board.

.. warning::
   Li-ion batteries can be hazardous if over-discharged or short-circuited. Always use a proper Li-ion charging circuit and respect the battery’s current and temperature limits to avoid fire or damage.


.. raw:: html

   <br>

.. figure:: ../images/image/liion.jpeg
   :alt: Li-ion Battery Charger
   :width: 300px
   :align: center

   **Figure 9: Li-ion Battery Charger (P7)**

.. raw:: html

   <br>

.. note::
   Connector P7 lets you attach a 3.7 V Li-ion battery for backup or standalone operation—ensure the battery voltage does not exceed 4.2 V when fully charged.

.. raw:: html

   <br>

+--------------------+-------------------+----------------------+--------------+--------------+----------------------------------------------+
| Connector Pin No   | Connector Signal  | SOM Signal           | Signal Level | Signal Type  | Description                                  |
+====================+===================+======================+==============+==============+==============================================+
| 1                  | VBAT+             | VBAT_OUT             | 3.7–4.2V     | PWR          | Battery positive terminal                    |
+--------------------+-------------------+----------------------+--------------+--------------+----------------------------------------------+
| 2                  | BAT_TS            | BAT_TS               | 3.3V         | IN           | Battery temperature sense (to ADC)           |
+--------------------+-------------------+----------------------+--------------+--------------+----------------------------------------------+
| 3                  | GND               | GND                  | NA           | NA           | Ground reference                             |
+--------------------+-------------------+----------------------+--------------+--------------+----------------------------------------------+

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 9: Pin Assignment of P7
   </div>

.. raw:: html

   <br>

.. tip::
   To monitor battery health, measure the voltage on the **BAT_TS** pin (Pin-2). You can read this via an ADC channel on the SOM to implement low-battery shutdown or alert notifications in your application.
   


RTC (P11)
=========

The RB-DCU i.MX 6ULL-1P1 features an external RTC at P11 in addition to the
internal RTC.They are used for real-time or time-driven applications. The 2-pole
pin header P11 can be used to connect an external battery to keep time up to
date. Internal RTC is not mounted in board.


.. figure:: ../images/image/rtc.jpeg
   :alt: RTC
   :width: 300px
   :align: center

   **Figure 10: RTC (P11)**

.. raw:: html

   <br>


+-------------------+----------------+---------------+--------------+--------------------------------------+
| Connector Pin No  | SOM Signal     | Signal Level  | Signal Type  | Description                          |
+===================+================+===============+==============+======================================+
| 1                 | GND            | N/A           | N/A          | Ground reference                     |
+-------------------+----------------+---------------+--------------+--------------------------------------+
| 2                 | VCC_3V3        | 3.0–3.3V      | PWR          | RTC backup battery input             |
+-------------------+----------------+---------------+--------------+--------------------------------------+

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 10.1: Pin Assignment of P11
   </div>

.. raw:: html

   <br><br>


+-------------------+----------------+---------------+--------------+--------------------------------------+
| Connector Pin No  | SOM Signal     | Signal Level  | Signal Type  | Description                          |
+===================+================+===============+==============+======================================+
| 1                 | INT_RTC        | 3.3V          | PWR          | Internal RTC supply                  |
+-------------------+----------------+---------------+--------------+--------------------------------------+
| 2                 | RTC_BACKUP     | 3.0–3.3V      | PWR          | RTC supply node                      |
+-------------------+----------------+---------------+--------------+--------------------------------------+
| 3                 | EXT_RTC        | 3.0–3.3V      | PWR          | External battery input (P11)         |
+-------------------+----------------+---------------+--------------+--------------------------------------+

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 10.2: Pin Assignment of P3
   </div>


User LED (D4)
=================

The RB-DCU i.MX 6ULL-1P1 is populated with one user LEDs to indicate the
status of the user led, as well as the power supply voltage. View of the
RB-DCU i.MX 6ULL-1P1 (top) shows the location of the LED.

.. figure:: ../images/image/d4.jpeg
   :alt: D4
   :width: 300px
   :align: center

   **Figure 11: (D4)**

.. raw:: html

   <br><br>

+------+--------+-------------------------------+---------------+--------------+--------------------------------------+
| LED  | Colour | SOM Signal                    | Signal Level  | Signal Type  | Description                          |
+======+========+===============================+===============+==============+======================================+
| D4   | Green  | X_GPIO2_IO11_USER_LED         | 3.3V          | OUT          | User LED (active low control)        |
+------+--------+-------------------------------+---------------+--------------+--------------------------------------+


.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 11: Pin Assignment of D4
   </div>


User Switch (SW1)
=====================

The RB-DCU i.MX 6ULL-1P1 is populated with Single user Switch to check the
INPUT operation of the board.**X_GPIO2_IO8_INT_SW** is used for switch.


.. figure:: ../images/image/user_switch.jpeg
   :alt: Switch1
   :width: 300px
   :align: center

   **Figure 12: Switch1 (SW1)**


.. csv-table::
   :header: "SOM Signal","Signal Level","Signal Type","Description"
   :widths: 30, 15, 15, 40

   "X_GPIO2_IO8_INT_SW","3.3V","IN","User switch input (active low)"

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 12: Pin Assignment of SW1
   </div>


Mini PCIe (P8)
==================

**USB-OTG interface** signals are routed through the **Mini PCIe connector (P8)**,
which allows devices connected via mPCIe to communicate using the USB
protocol. The SIM/UIM card signals of a connected mPCIe module can be made
available at expansion connector J4.

.. warning::
   Many mPCIe cards expect a full 5 V supply on the slot’s VCC pin—do **not** insert a USB-only module without confirming the board’s power capabilities, as overcurrent can cause brown-outs or damage the board.
   
.. raw:: html

   <br>

.. figure:: ../images/image/mini.jpeg
   :alt: Mini PCIe Connector
   :width: 300px
   :align: center

   **Figure 13: Mini PCIe Connector (P8)**


.. raw:: html

   <br>

.. csv-table::
   :header: "Connector Pin No","Connector Signal","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 20, 30, 12, 12, 30

   "2","+3.3V","VCC_3V3_GSM","3.3V","PWR","Mini PCIe power supply"
   "4","GND","GND","NA","NA","Ground reference"
   "6","SIM_VCC","SIM_VCC","1.8/3.0V","PWR","SIM card power"
   "8","SIM_RST","SIM_RST","1.8/3.0V","OUT","SIM reset"
   "10","SIM_CLK","SIM_CLK","1.8/3.0V","OUT","SIM clock"
   "12","SIM_IO","SIM_IO","1.8/3.0V","I/O","SIM data"
   "20","USB_D+","X_USB_OTG_P","3.3V","I/O","USB data positive"
   "22","USB_D-","X_USB_OTG_N","3.3V","I/O","USB data negative"
   "24","PERST#","X_GPIO1_4_mPCIe_RST","3.3V","OUT","PCIe reset (active low)"
   "42","LED_WWAN#","WLAN_EN_LED","3.3V","OUT","WWAN status LED"
   "44","LED_WLAN#","WLAN_EN_LED","3.3V","OUT","WLAN status LED"
   "52","+3.3V","VCC_3V3_GSM","3.3V","PWR","Mini PCIe power supply"


.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 13: Pin Assignment of P8
   </div>

   
Micro SIM Socket (J4)
=========================

A Micro SIM Socket(J4) is provided to enable cellular connectivity through a
mobile network and a smooth extraction function by Push-in/ Push-out of
card.


.. warning::

   Do **not** insert or remove the SIM card while the board is powered on. Doing so may cause hardware damage or corrupt modem communication.

.. raw:: html

   <br>

.. figure:: ../images/image/sim.jpeg
   :alt: micro SIM socket
   :width: 200px
   :align: center

   **Figure 14: Micro SIM Socket (J4)**



.. csv-table::
   :header: "Connector Pin No","Signal","Signal Level","Signal Type","Description"
   :widths: 15, 25, 15, 15, 30

   "C1","SIM_VCC","1.8/3.0V","PWR","SIM card power supply"
   "C2","SIM_RST","1.8/3.0V","OUT","SIM reset signal"
   "C3","SIM_CLK","1.8/3.0V","OUT","SIM clock signal"
   "C4","Not used","N/A","N/A","Not connected"
   "C5","GND","N/A","N/A","Ground reference"
   "C6","SIM_VPP","1.8/3.0V","PWR","SIM programming voltage"
   "C7","TP32","N/A","TP","Test point connection"
   "S1","GND","N/A","N/A","Ground"
   "S2","GND","N/A","N/A","Ground"
   "S3","GND","N/A","N/A","Ground"
   "S4","GND","N/A","N/A","Ground"
   "CD","SIM_VCC","1.8/3.0V","PWR","Card detect / SIM power"


.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 14: Pin Assignment of J4
   </div>

.. raw:: html

   <br>

.. note::

   This socket is designed for **Micro SIM** cards only. Using a Nano or full-size SIM with adapters may damage the socket.
   


eSIM (U16)
=============

eSIM offers significant advantages over traditional SIMs, particularly in terms
of flexibility, scalability, and ease of management, especially for IoT and
embedded systems that rely on cellular connectivity.eSIM is not mounted.


.. figure:: ../images/image/esim.jpeg
   :alt: eSIM (U16)
   :width: 300px
   :align: center

   **Figure 15: eSIM (U16)**

.. note::

   eSIM (Embedded SIM) is a programmable SIM card embedded directly into the device, eliminating the need for a physical SIM card slot. It allows remote provisioning and management of mobile network profiles.

.. raw:: html

   <br>

.. tip::

   eSIM is ideal for **remote or hard-to-access deployments**, where replacing a physical SIM card would be difficult.

.. raw:: html

   <br>

.. csv-table::
   :header: "Connector Pin No","Connector Signal","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 22, 30, 12, 12, 30

   "1","VCC","SIM_eSIM_VDD","1.8/3.0V","PWR","eSIM power supply"
   "2","RST","eSIM_RST","1.8/3.0V","OUT","eSIM reset signal"
   "3","CLK","eSIM_CLK","1.8/3.0V","OUT","eSIM clock signal"
   "5","DATA","eSIM_DATA","1.8/3.0V","I/O","eSIM data line"
   "6","GND","GND","NA","NA","Ground reference"


.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 15: Pin Assignment of U16
   </div>

.. raw:: html

   <br>

.. note::

   The eSIM (U16) module is **not pre-mounted** on the board. If eSIM functionality is required, you must mount a compatible eSIM module manually.

   
Wi-Fi Module (U18)
======================

The LILY-W1 series ultra-compact Wi-Fi front end modules include an
integrated MAC/baseband processor and RF front end components. The
modules connect to a host via USB interface. They provide simultaneous
operation as a station and a micro access point for up to 8 clients.

.. figure:: ../images/image/wifi.jpeg
   :alt: WIFI Module (U18)
   :width: 200px
   :align: center

   **Figure 16: Wi-Fi Module (U18)**




.. csv-table::
   :header: "Connector Pin No","Connector Signal","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 22, 30, 12, 12, 30

   "1","SDIO_D1","SDIO_D1","3.3V","I/O","SDIO data line 1"
   "2","SDIO_D0","SDIO_D0","3.3V","I/O","SDIO data line 0"
   "3","SDIO_CLK","SDIO_CLK","3.3V","OUT","SDIO clock"
   "4","SDIO_CMD","SDIO_CMD","3.3V","I/O","SDIO command"
   "8","VCC","VCC_3V3_WIFI_MOD","3.3V","PWR","WiFi module power"
   "9","VCC","VCC_3V3_WIFI_MOD","3.3V","PWR","WiFi module power"
   "10","GND","GND","NA","NA","Ground reference"
   "11","GND","GND","NA","NA","Ground reference"
   "12","ANT","RF_ANT","RF","RF","Antenna connection (50Ω)"
   "13","GND","GND","NA","NA","Ground reference"
   "14","PDn","WIFI_PDn","3.3V","IN","Power down control (active low)"
   "18","WAKE","X_GPIO_WIFI_WAKE","3.3V","IN","Wake-up signal from host"
   "19","HOST_WAKE","X_HOST_WAKE_UP_3V3IO","3.3V","OUT","Wake-up signal to host"
   "21","USB_D+","X_USB_OTG2_P","3.3V","I/O","USB data positive"
   "22","USB_D-","X_USB_OTG2_N","3.3V","I/O","USB data negative"



.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 16: Pin Assignment of U18
   </div>

   
   
Ethernet Connectivity (J3)
===========================

The Ethernet interfaces of the RB-DCU i.MX 6ULL-1P1 are accessible at RJ45
connector(J3). Ethernet is directly brought out from the SOM's Ethernet
interface ENET1.Ethernet interface is configured as 10/100Base-T networks.
The LEDs for LINK (green) and SPEED (yellow) indications are integrated into
the connector.



.. figure:: ../images/image/ethernet.jpeg
   :alt: Ethernet Interfaces at Connector (J3)
   :width: 200px
   :align: center

   **Figure 17: Ethernet Interfaces at Connector (J3)**

.. csv-table::
   :header: "Connector Pin No","Connector Signal","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 25, 30, 12, 12, 30

   "1","TD+","X_ENET1_TX_P","1.8/2.5V","DIFF","Ethernet transmit positive"
   "2","TD-","X_ENET1_TX_N","1.8/2.5V","DIFF","Ethernet transmit negative"
   "3","RD+","X_ENET1_RX_P","1.8/2.5V","DIFF","Ethernet receive positive"
   "6","RD-","X_ENET1_RX_N","1.8/2.5V","DIFF","Ethernet receive negative"
   "4","PoE_V+","NC","NA","PWR","PoE positive (not used)"
   "5","PoE_V+","NC","NA","PWR","PoE positive (not used)"
   "7","PoE_V-","NC","NA","PWR","PoE negative (not used)"
   "8","PoE_V-","NC","NA","PWR","PoE negative (not used)"
   "9","LED1_A","X_ENET1_LED0","3.3V","OUT","Ethernet LED 0 control"
   "10","LED1_K","GND","NA","NA","LED ground"
   "11","LED2_A","X_ENET1_LED1","3.3V","OUT","Ethernet LED 1 control"
   "12","LED2_K","GND","NA","NA","LED ground"
   "13","SHIELD1","GND","NA","NA","Connector shield"
   "14","SHIELD2","GND","NA","NA","Connector shield"

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 16: Pin Assignment of J3
   </div>
.. raw:: html

   <br>

.. note::

   The **Ethernet port (J3)** uses the **ENET1 interface** from the SOM and supports **10/100 Mbps** operation. Link and activity status are indicated through integrated **bi-color LEDs** (green for LINK, yellow for SPEED).


DB9 Pin Mating (P4)
=======================

The RB-DCU i.MX 6ULL-1P1 provides up to 4 high-speed universal asynchronous
interfaces. UART2 at RS232(U3) and UART6 at RS485(U11) is available at DB9
pin mating Male connector(P4).

.. figure:: ../images/image/rs232_rs485.jpeg
   :alt: RS-232 and RS‑485 Interface Connectors at P4
   :width: 300px
   :align: center

   **Figure 18: RS-232 and RS‑485 Interface Connectors at (P4)**

.. raw:: html

   <br>


.. csv-table::
   :header: "Connector Pin No","Connector Signal","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 25, 30, 12, 12, 25

   "1","GND","GND","N/A","N/A","Ground reference"
   "2","DB_RS232_RX_1","X_UART2_RX","3.3V","IN","RS232 receive channel 1"
   "3","DB_RS232_TX_1","X_UART2_TX","3.3V","OUT","RS232 transmit channel 1"
   "4","DB_RS485_N","X_CSI_PIXCLK_UART6_RX","3.3V","I/O","RS485 differential negative"
   "5","GND","GND","N/A","N/A","Ground reference"
   "6","DB_RS485_P","X_CSI_MCLK_UART6_TX","3.3V","I/O","RS485 differential positive"
   "7","DB_RS232_RX_2","X_UART2_RTS_B","3.3V","IN","RS232 receive channel 2"
   "8","DB_RS232_TX_2","X_UART2_CTS_B","3.3V","OUT","RS232 transmit channel 2"
   "9","GND","GND","N/A","N/A","Ground reference"
   "10","GND","GND","N/A","N/A","Ground reference"

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 18: Pin Assignment of P4
   </div>

.. raw:: html

   <br>

.. note::

   On the RB-DCU i.MX 6ULL-1P1 board:

   - **RS232 communication uses UART2**
   - **RS485 communication uses UART6**


   
RF-Connector 1 (P9)
=======================

RF (Radio Frequency) connectors are used for interfacing with wireless
communication modules and antennas. These connectors allow to send and
receive RF signals, which can be essential for applications involving Wi-Fi,
Bluetooth, GPS, cellular networks, and other wireless communication
technologies.RF connector1 is using **UART4 interface**.

.. warning::

   Do not hot-plug RF modules into the connector while the board is powered on, 
   as this may cause signal disruption or hardware damage.
.. raw:: html

   <br>

.. figure:: ../images/image/rf1.jpeg
   :alt: RF_CONNECTOR-1 (P9)
   :width: 300px
   :align: center

   **Figure 19: RF-Connector-1 (P9)**

.. raw:: html

   <br>

.. csv-table::
   :header: "Connector Pin No","Connector Signal","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 28, 30, 12, 12, 26

   "1","VCC_3V3","VCC_3V3","3.3V","PWR","3.3V power supply"
   "2","GND","GND","N/A","N/A","Ground reference"
   "3","VCC_3V3","VCC_3V3","3.3V","PWR","3.3V power supply"
   "4","GND","GND","N/A","N/A","Ground reference"
   "5","RF_UART4_TX","X_UART4_TX","3.3V","OUT","UART4 transmit"
   "6","GND","GND","N/A","N/A","Ground reference"
   "7","RF_UART4_RX","X_UART4_RX","3.3V","IN","UART4 receive"
   "8","GND","GND","N/A","N/A","Ground reference"
   "9","RF_GPIO2_IO9_RF1_RST","X_GPIO2_IO9","3.3V","OUT","RF module reset"
   "10","GND","GND","N/A","N/A","Ground reference"
   "11","RF_GPIO5_IO9_RF1_1","X_GPIO5_IO9","3.3V","I/O","RF control signal 1"
   "12","GND","GND","N/A","N/A","Ground reference"
   "13","RF_GPIO2_IO14_RF1_2","X_GPIO2_IO14","3.3V","I/O","RF control signal 2"
   "14","GND","GND","N/A","N/A","Ground reference"


.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 19: Pin Assignment of P9
   </div>

.. raw:: html

   <br>

.. note::

   RF_CONNECTOR 1 is typically connected to external antennas or RF modules 
   that support UART communication. Confirm the module's specifications 
   before connection.

   
RF-Connector 2 (P12)
========================

RF (Radio Frequency) connectors are used for interfacing with wireless
communication modules and antennas. These connectors allow to send and
receive RF signals, which can be essential for applications involving Wi-Fi,
Bluetooth, GPS, cellular networks, and other wireless communication
technologies.RF connector1 is using **UART3 interface**.

.. figure:: ../images/image/rf2.jpeg
   :alt: RF_CONNECTOR 2 (P12)
   :width: 280px
   :align: center

   **Figure 20: RF-Connector-2 (P12)**

.. raw:: html

   <br>

.. csv-table::
   :header: "Connector Pin No","Connector Signal","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 28, 30, 12, 12, 26

   "1","VCC_3V3","VCC_3V3","3.3V","PWR","3.3V power supply"
   "2","GND","GND","N/A","N/A","Ground reference"
   "3","VCC_3V3","VCC_3V3","3.3V","PWR","3.3V power supply"
   "4","GND","GND","N/A","N/A","Ground reference"
   "5","RF_UART3_TX","X_UART3_TX","3.3V","OUT","UART3 transmit"
   "6","GND","GND","N/A","N/A","Ground reference"
   "7","RF_UART3_RX","X_UART3_RX","3.3V","IN","UART3 receive"
   "8","GND","GND","N/A","N/A","Ground reference"
   "9","RF_GPIO1_IO10_RF2_RST","X_GPIO1_IO10","3.3V","OUT","RF2 module reset"
   "10","GND","GND","N/A","N/A","Ground reference"
   "11","RF_GPIO2_IO15_RF2_1","X_GPIO2_IO15","3.3V","I/O","RF2 control signal 1"
   "12","GND","GND","N/A","N/A","Ground reference"
   "13","RF_GPIO1_IO14_RF2_2","X_GPIO1_IO14","3.3V","I/O","RF2 control signal 2"
   "14","GND","GND","N/A","N/A","Ground reference"

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 20: Pin Assignment of P12
   </div>


Optical UART (D30 & D31)
========================

An "Optical UART" typically refers to a communication interface that combines
the principles of UART (Universal Asynchronous Receiver/Transmitter) with
optical signalling for data transmission. In this system, instead of electrical
signals transmitted over copper wires, light pulses are used, often through
optical fibbers or LEDs and photodiodes. The benefits of optical
communication include immunity to electromagnetic interference (EMI) and
enhanced isolation for sensitive systems. It is using UART7 interface and for
transmit and receive data pins are:


.. figure:: ../images/image/optical.jpeg
   :alt: Optical UART
   :width: 300px
   :align: center

   **Figure 21: Optical UART (D30 & D31)**

.. raw:: html

   <br>

+-------------------+------------------+---------------------------+---------------+--------------+-----------------------------------------------+
| Connector Pin No  | Connector Signal | SOM Signal                | Signal Level  | Signal Type  | Description                                   |
+===================+==================+===========================+===============+==============+===============================================+
| 1                 | OPTICAL_TX       | X_LCD_D16_UART7_TX        | 3.3V          | OUT          | UART7 transmit via IR LED (optical output)    |
+-------------------+------------------+---------------------------+---------------+--------------+-----------------------------------------------+
| 2                 | OPTICAL_RX       | X_LCD_D17_UART7_RX        | 3.3V          | IN           | UART7 receive via phototransistor (optical in)|
+-------------------+------------------+---------------------------+---------------+--------------+-----------------------------------------------+

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 21: Pin Assignment of D30 & D31
   </div>

.. raw:: html

   <br>
.. note::

   Optical UART offers galvanic isolation, making it ideal for use in electrically noisy or high-voltage environments.


SPI-LCD Header (P10)
========================

A **SPI-LCD header** allows to connect an LCD (Liquid Crystal Display) using the
**Serial Peripheral Interface (SPI)** communication protocol. SPI is a common
interface used to communicate with peripherals like displays, sensors, and other
devices.


.. warning::

   Incorrect wiring of SPI pins (MOSI, MISO, CLK, CS) may result in non-functional display or permanent damage to the LCD module.

.. raw:: html

   <br>

.. figure:: ../images/image/spilcd.jpeg
   :alt: SPI-LCD Header (P10)
   :width: 300px
   :align: center

   **Figure 22: SPI-LCD Header (P10)**

.. raw:: html

   <br>



.. csv-table::
   :header: "Connector Pin No","Connector Signal","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 25, 30, 12, 12, 25

   "1","SPI_CS","X_ECSPI1_SS0","3.3V","OUT","SPI chip select"
   "2","VCC_5V","VCC5V_IN_SW","5V","PWR","5V power supply"
   "3","RESET","X_RESET#","3.3V","OUT","LCD reset (active low)"
   "4","VCC_5V","VCC5V_IN_SW","5V","PWR","5V power supply"
   "5","SPI_MOSI","X_ECSPI1_MOSI","3.3V","OUT","SPI master out slave in"
   "6","LCD_DC","X_GPIO_DC","3.3V","OUT","Data/Command control"
   "7","SPI_SCLK","X_ECSPI1_SCLK","3.3V","OUT","SPI clock"
   "8","GND","GND","N/A","N/A","Ground reference"
   "9","SPI_MISO","X_ECSPI1_MISO","3.3V","IN","SPI master in slave out"
   "10","GND","GND","N/A","N/A","Ground reference"



.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 22: Pin Assignment of P10
   </div>

.. raw:: html

   <br>

.. note::

   The SPI-LCD header provides a compact and efficient connection method for graphic or character-based LCDs compatible with SPI.



Tamper Pins (TP48, TP49)
============================

**Tamper pins** are security-oriented hardware features designed to detect
unauthorized physical access or tampering with the device.They are used to
monitor the integrity of the device and respond to any physical breaches or
tampering attempts and **X_GPIO5_1, X_GPIO5_2** pins are used.



.. figure:: ../images/image/tamper.jpeg
   :alt: Tamper pins
   :width: 300px
   :align: center

   **Figure 23: Tamper Pins**

.. raw:: html

   <br>

.. note::

   Tamper detection is especially useful in security-critical applications such as financial terminals, industrial control systems, and IoT gateways.

.. raw:: html

   <br>

.. csv-table::
   :header: "Connector Pin No","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 15, 30, 15, 15, 30

   "TP48","X_GPIO5_1","3.3V","IN","Active low tamper detection input (TP48)"
   "TP49","X_GPIO5_2","3.3V","IN","Active low tamper detection input (TP49)"

.. raw:: html

   <div style="margin-top: -15px; text-align: center; font-style: italic; font-weight: bold;">
     Table 23: Pin Assignment of TP48 & TP49
   </div>

.. raw:: html

   <br>

.. tip::

   Configure tamper pins in software to trigger alerts, log events, or disable sensitive operations upon detection of tampering.


   
Digital Input HDR (P5)
==========================

A **digital input header** is a physical interface (set of pins) that allows to receive
**digital signals** from external devices or sensors. These pins are used to detect
binary states, which are usually either **high (1)** or **low (0)**, representing the
presence or absence of a voltage signal.
Note: Default State of Digital Input (Low) and Defined as Input Port When
Isolated Voltage connected upto 24V from external; MCU reads High (3.3V).

.. warning::

   Exceeding the 24V input limit may permanently damage the digital input circuitry. Always verify the voltage levels before connection.

.. raw:: html

   <br>

.. figure:: ../images/image/hdr.jpeg
   :alt: Digital Input HDR
   :width: 300px
   :align: center

   **Figure 24: Digital Input HDR (P5)**

.. raw:: html

   <br>

+-------------------+----------------------+-------------------+---------------+--------------+-----------------------------------------------+
| Connector Pin No  | Connector Signal     | SOM Signal        | Signal Level  | Signal Type  | Description                                   |
+===================+======================+===================+===============+==============+===============================================+
| 1                 | DIN(0–24V)_01        | X_GPIO5_5         | 3.3V          | IN           | Digital input channel 1 (0–24V isolated input)|
+-------------------+----------------------+-------------------+---------------+--------------+-----------------------------------------------+
| 2                 | DIN(0–24V)_02        | X_GPIO2_IO13      | 3.3V          | IN           | Digital input channel 2 (0–24V isolated input)|
+-------------------+----------------------+-------------------+---------------+--------------+-----------------------------------------------+
| 3                 | DIN(0–24V)_03        | X_GPIO1_01        | 3.3V          | IN           | Digital input channel 3 (0–24V isolated input)|
+-------------------+----------------------+-------------------+---------------+--------------+-----------------------------------------------+
| 4                 | DIN(0–24V)_04        | X_GPIO1_11        | 3.3V          | IN           | Digital input channel 4 (0–24V isolated input)|
+-------------------+----------------------+-------------------+---------------+--------------+-----------------------------------------------+
| 5                 | DGND_ISO_IN          | DGND_ISO_IN       | N/A           | N/A          | Isolated digital ground                       |
+-------------------+----------------------+-------------------+---------------+--------------+-----------------------------------------------+
| 6                 | DGND_ISO_IN          | DGND_ISO_IN       | N/A           | N/A          | Isolated digital ground                       |
+-------------------+----------------------+-------------------+---------------+--------------+-----------------------------------------------+

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 24: Pin Assignment of P5
   </div>

Micro SD Card (J2)
======================

The RB-DCU i.MX 6ULL-1P1 provides a standard micro SDHC card slot at **J2** for
connection to MMC/SD interface cards. It allows easy and convenient
connection to peripheral devices such as SD and MMC cards. Power to the SD
interface is supplied by inserting the appropriate card into the MMC/SD
connector, which features card detection, a lock mechanism, and a smooth
extraction function via Push-in/Push-out of the card.

Insertable jumper **J9** allows toggling between eMMC boot and boot from the
SD card. To boot from the SD card, **J9** must be set to change the boot
configuration (Boot Mode Jumper J9).


.. warning::

   Do not insert or remove the SD card while the system is powered on, as it may corrupt data or damage the card.

.. raw:: html

   <br>

.. figure:: ../images/image/sdcard.jpeg
   :alt: Micro SD Card Interface
   :width: 250px
   :align: center

   **Figure 25: Micro SD Card Interface at Connector (J2)**

.. note::

   The microSD card interface supports SDHC cards up to 32 GB. Use cards that are formatted as FAT32 for best compatibility.




.. csv-table::
   :header: "Connector Pin No","Connector Signal","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 25, 30, 12, 12, 25

   "1","DAT2","X_SD1_D2","3.3V","I/O","SD data line 2"
   "2","DAT3","X_SD1_D3","3.3V","I/O","SD data line 3"
   "3","CMD","X_SD1_CMD","3.3V","I/O","SD command line"
   "4","VCC","VCC_3V3","3.3V","PWR","SD card power supply"
   "5","CLK","X_SD1_CLK","3.3V","OUT","SD clock"
   "6","GND","GND","N/A","N/A","Ground reference"
   "7","DAT0","X_SD1_D0","3.3V","I/O","SD data line 0"
   "8","DAT1","X_SD1_D1","3.3V","I/O","SD data line 1"
   "9","CD","X_UART1_RTS_B_SD_CD","3.3V","IN","Card detect signal"
   "10–18","GND","GND","N/A","N/A","Ground (shield and return)"

.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 25: Pin Assignment of J2
   </div>

.. raw:: html

   <br>

.. tip::

   To boot from the SD card, make sure the J9 jumper is configured for SD boot **before powering on** the board.


Bluetooth (U14)
================

Bluetooth functionality enables wireless communication with other Bluetooth
devices, such as smartphones, computers, sensors, and other peripherals.It
uses **UART5 interface**.



.. figure:: ../images/image/bluetooth.jpeg
   :alt: Bluetooth Module
   :width: 300px
   :align: center

   **Figure 26: Bluetooth (U14)**



.. raw:: html

   <br>
   

.. csv-table::
   :header: "Connector Pin No","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 30, 12, 12, 30

   "1","GND","NA","NA","Ground reference"
   "8","SWCLK","3.3V","IN","Debug clock (SWD)"
   "9","SWDIO","3.3V","I/O","Debug data (SWD)"
   "10","SWO","3.3V","OUT","Debug trace output"
   "12","GND","NA","NA","Ground reference"
   "13","VCC_3V3_BLE","3.3V","PWR","Bluetooth module power"
   "14","X_UART5_RX","3.3V","IN","UART5 receive"
   "15","X_UART5_TX","3.3V","OUT","UART5 transmit"
   "16","X_UART5_CTS_B","3.3V","IN","UART5 CTS (active low)"
   "17","X_UART5_RTS_B","3.3V","OUT","UART5 RTS (active low)"
   "20","GND","NA","NA","Ground reference"
   "22","X_LCD_VSYNC_WATCH_DOG","3.3V","OUT","External watchdog signal"
   "30","X_GPIO_BLE_RST","3.3V","OUT","Bluetooth reset control"
   "31","GND","NA","NA","Ground reference"



.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 26: Pin Assignment of U14
   </div>

.. raw:: html

   <br>

.. tip::

   Ideal for short-range, low-power wireless communication in embedded IoT
   systems. Can be used for serial console, wireless sensor data, or configuration
   without cables.

   
Accelerometer, Gyroscope - 3 Axis (Embedded Temperature Sensor) (U23)  
======================================================================

An **Accelerometer** and a **Gyroscope** with an embedded temperature sensor,
typically in a 3-axis configuration, are common sensors used for motion
sensing, orientation tracking, and environmental monitoring. It is using **I2C1
interface**.



.. figure:: ../images/image/acc.jpeg
   :alt: Accelerometer, Gyroscope, Temp Sensor
   :width: 300px
   :align: center

   **Figure 27: Accelerometer, Gyroscope - 3 Axis (Embedded Temperature sensor) (U23)**



.. note::

   This sensor module communicates via the I2C1 bus. Ensure proper pull-up
   resistors on SDA and SCL lines if not already present on the board.


.. raw:: html

   <br>


.. csv-table::
   :header: "Connector Pin No","SOM Signal","Signal Level","Signal Type","Description"
   :widths: 12, 30, 12, 12, 30

   "1","VCC_3V3_SEN","3.3V","PWR","Sensor power supply"
   "2","VCC_3V3","3.3V","PWR","Main 3.3V supply"
   "3","VCC_3V3","3.3V","PWR","Main 3.3V supply"
   "4","X_CSI_FIELD_GPIO_3V3","3.3V","IN","Interrupt / GPIO input"
   "5","VCC_3V3","3.3V","PWR","Main 3.3V supply"
   "6","GND","NA","NA","Ground reference"
   "7","GND","NA","NA","Ground reference"
   "8","VCC_3V3","3.3V","PWR","Main 3.3V supply"
   "12","VCC_3V3_SEN","3.3V","PWR","Sensor power supply"
   "13","X_I2C1_SCL","3.3V","I/O","I2C clock (TP47)"
   "14","X_I2C1_SDA","3.3V","I/O","I2C data (TP46)"


.. raw:: html

   <div style="text-align: center; margin-top: -20px; font-style: italic; font-weight: bold;">
     Table 27: Pin Assignment of U23
   </div>

.. raw:: html

   <br>

.. tip::

   The combined use of accelerometer and gyroscope enables precise motion
   tracking, ideal for gesture detection, tilt sensing, and inertial navigation in
   embedded applications.



.. raw:: html

   <hr style="border: 0; border-top: 3px solid #ccc; margin: 20px 0;">



=====================
SD Card Setup Guide
=====================

SD Card Partition Setup
=======================

**Step 1:** Insert the SD card into your PC. Then open the application named **GParted Partition Editor**. It will prompt you for a password. After entering the password, GParted will open.

.. figure:: ../images/gpart/opened_gparted.jpeg
   :alt: GParted main window after launch
   :width: 600px
   :align: center

   **Figure 28: GParted application opened successfully**

.. raw:: html

   <br>

.. warning::
   Be careful when using GParted — your PC's SSD/HDD and the SD card partitions are all shown. Mistakes can lead to data loss!

---

**Step 2:** Select your SD card device in the dropdown at the top-right corner.

.. figure:: ../images/gpart/image.jpeg
   :alt: Selecting SD card device in GParted
   :width: 600px
   :align: center

   **Figure 29: Selecting the SD card device from GParted's device list**

.. raw:: html

   <br>


**Step 3:** Unmount all partitions on the SD card using right-click, then delete all partitions.

.. figure:: ../images/gpart/unmount.jpeg
   :alt: Right-click unmount partitions in GParted
   :width: 600px
   :align: center

   **Figure 30: Unmounting all partitions on the SD card**

.. raw:: html

   <br>

.. figure:: ../images/gpart/dd.png
   :alt: Deleting partitions using GParted
   :width: 600px
   :align: center

   **Figure 31: Deleting all partitions from the SD card**

.. raw:: html

   <br>

.. figure:: ../images/gpart/unmounted.jpeg
   :alt: Final unallocated state of SD card
   :width: 600px
   :align: center

   **Figure 32: Final view showing SD card with all partitions deleted**



.. raw:: html

   <br>

   
**Step 4:** Right-click on the unallocated partition and select the **New** option. A window titled *Create New Partition* will appear.

.. figure:: ../images/gpart/new.jpeg
   :alt: Create new partition window in GParted
   :width: 600px
   :align: center

   **Figure 33:Creating a new partition in GParted**

.. raw:: html

   <br>

**Step 5:** For the **boot** partition:
- Set “Free space preceding” to **8**
- Set “New size” to **2048**
- Select **fat32** as the file system
- Set label as **boot**
- Click **Add**

.. figure:: ../images/gpart/boot.jpeg
   :alt: Configuring boot partition parameters in GParted
   :width: 600px
   :align: center

   **Figure 34:Configuring parameters for the boot partition**

.. raw:: html

   <br>


**Step 6:** To create the **rootfs** partition:
- Right-click the remaining **unallocated** space
- Choose **New**
- Set “New size” to **1024** or use the remaining space
- Select **ext3** as the file system
- Label it as **rootfs**
- Click **Add**

.. figure:: ../images/gpart/root.jpeg
   :alt: Setting up rootfs partition in GParted
   :width: 600px
   :align: center

   **Figure 35:Setting up the rootfs partition**

.. raw:: html

   <br>


**Step 7:** Click the **✔️ Apply** button on the toolbar. It will apply all pending operations and may take a few seconds. Close the window after completion.

.. figure:: ../images/gpart/clicks.jpeg
   :alt: Apply pending operations in GParted
   :width: 600px 
   :align: center

   **Figure 36:Applying all pending partition changes**

.. raw:: html

   <br>

**Step 8:** Right-click the **boot** partition and choose **Manage Flags**. In the popup, enable the **boot** flag and then close the dialog.

.. figure:: ../images/gpart/flag.jpeg
   :alt: Setting the boot flag on boot partition in GParted
   :width: 600px  
   :align: center

   **Figure 37: Enabling the boot flag for the boot partition**

.. raw:: html

   <br>


**Step 9:** Now your SD card is ready to copy the **boot** and **rootfs** files for the **RB-DCU i.MX 6ULL** board.

.. raw:: html

   <hr style="border: 0; border-top: 3px solid #ccc; margin: 20px 0;">



Copying Files(images) to SD Card
================================

**Step 1:** Flashing barebox.bin into SD-card 8 MB raw space.
        
.. code-block:: console

   $ sudo dd if=<path of the barebox image> of=/dev/sd<a/b/c/d> bs=512 skip=2 seek=2
   $ sync

**Step 2:** Copy the kernel image(zImage), oftree image(.dtb) into the boot partition of the sdcard. Below are the command to copy into sd card.
        
.. code-block:: console

    $ cp zImage /media/<username>/BOOT
    $ cp oftree /media/<username>/BOOT  
    
**Step 3:** And root file system tar file should be extract to the rootfs partition of the sdcard using the below commands.
        
.. code-block:: console

   $ sudo tar -xvf <path of the rootfs tar file> -C <path of the sdcard rootfs partition>
   $ sync
   
TARGET :
Now insert the sdcard into the board and make the jumper positions for booting from sdcard.

.. raw:: html

   <br>
   
.. raw:: html

   <hr style="border: 0; border-top: 3px solid #ccc; margin: 20px 0;">



=======================
How to Handle the Board
=======================

ESD Safety
------------

**Before touching the board:**

* Work on a clean, non‑static surface (anti‑static mat if available).

* Wear an anti‑static wrist strap grounded to earth.

* Hold the board by its edges—avoid contact with chips or connectors.

* Avoid touching exposed metal parts or pins. 

.. warning::
   Always discharge any static build‑up before touching the board.


**Prepare Your Workspace:**

* Gather all needed items:
* RB-DCU i.MX 6ULL board
* SD card with boot image.
* Power adapter (5V).
* USB‑to‑TTL debugger cable
* Host PC (Linux recommended) with **minicom** or similar terminal software installed.

.. note::
   - Work in a clean, dry, low‑humidity area to minimize static buildup.
   - Keep food and liquids away from electronic components.



**Insert the SD Card:**

* Ensure the SD card is formatted correctly (e.g., FAT32 for boot images).

* Find the card slot on the board and insert.

* Align contacts, then gently push until you hear or feel a click.

* If it resists, pull out, realign, and try again—never force it.


**Connect the Power Adapter:**

* Ensure the SD card is inserted but do not power on the board switch yet.

* Plug the adapter into a grounded wall outlet.

* Attach the barrel connector to the board’s power input jack.

**Connect the USB‑to‑TTL Debugger Cable:**

* Locate the board’s debug port (USB‑to‑TTL header or micro‑USB).

* Insert the TTL end into the board’s debug header pins. Plug the USB end into your host PC.

On Linux, verify with:

.. code-block:: console

   $ lsusb

**Power On the Board:**

* Confirm both the adapter and USB‑to‑TTL cable are connected.

* Turn the board’s power switch to ON.

* LEDs should light up, and the boot process begins.

.. raw:: html

   <hr style="border: 0; border-top: 3px solid #ccc; margin: 20px 0;">



======================================
How to Connect the Board with a PC
======================================

Connect to the Board via Serial Console (Minicom)
=================================================

Install Minicom (if it is not already installed):

.. code-block:: console

   $ sudo apt update && sudo apt install minicom

Identify the serial port after connecting the USB-to-TTL cable:

.. code-block:: console

   $ dmesg | grep -i tty

Look for a newly listed device such as `/dev/ttyUSB0` or `/dev/ttyACM0`.

**Start Minicom with the correct port and baud rate (115200):**

**1.** In your host machine terminal:

.. code-block:: console

   $ minicom -s

.. raw:: html

   <br>

**2.** Choose **"Serial port setup"** and configure the following:

.. figure:: ../images/minicom/open_minicom.jpeg
   :alt: Minicom startup interface for configuration
   :width: 300px
   :align: center

   **Figure 38: Minicom startup screen where the serial configuration menu is accessed**

.. raw:: html

   <br>

**3.** Set the serial device to your USB-to-TTL port (e.g., `/dev/ttyUSB0`).

**4.** Set the baud rate to **115200**.

**5.** Disable **hardware flow control** (set to “No”).

.. figure:: ../images/minicom/change.jpeg
   :alt: Configuring serial port and baud rate in Minicom
   :width: 600px
   :align: center

   **Figure 39: Minicom serial settings menu where device, baud rate, and flow control options are configured**

.. raw:: html

   <br>

**6.** Save the setup as the **default configuration**.

.. figure:: ../images/minicom/save.jpeg
   :alt: Saving default Minicom configuration
   :width: 300px
   :align: center

   **Figure 40: Saving the modified serial settings as the default configuration in Minicom**

.. raw:: html

   <br>

**7.** Exit the setup menu to start the Minicom serial console.

**Shutting Down the Board:**

To safely power off the target board, run the following command in the target terminal:

.. code-block:: console

   $ poweroff

.. raw:: html

   <hr style="border: 0; border-top: 3px solid #ccc; margin: 20px 0;">



Connect to the Board via SSH (Network Access)
=============================================

You can also connect to the board over the network using SSH. Follow the steps below:

.. note::

   Before using SSH, ensure **both your PC and the embedded board are on the same network**—whether via the same Wi-Fi router, LAN switch, or direct Ethernet connection with static IPs.

   SSH requires proper IP connectivity. If the devices are not on the same subnet or not routable, **SSH will fail**. Always verify connectivity using `ping` or by checking IP addresses.

**Step 1: Check the IP Address of the Host PC**

Use the following command to check your PC’s IP address:

.. code-block:: console

   $ ip a

If no IP is assigned, configure a static IP using:

.. code-block:: console

   $ sudo ip addr add 192.168.2.1/24 dev <network_interface_name>

**Example:**

.. code-block:: console

   $ sudo ip addr add 192.168.2.1/24 dev enp0s31f6

.. figure:: ../images/ssh/add_ip.jpeg
   :alt: Assigning static IP to host interface
   :width: 600px
   :align: center

   **Figure 41: Manually assigning a static IP address to the host machine's Ethernet interface**

.. raw:: html

   <br>


**Step 2: Configure the IP Address on the Target Board**

On the target board, verify its IP address:

.. code-block:: console

   $ ip a

If none is assigned, manually configure one:

.. code-block:: console

   $ ifconfig eth0 192.168.11.10 netmask 255.255.255.0 up
   $ route add default gw 192.168.11.1

.. note::

   Make a note of both the assigned IP address and the hostname of the target board for later use.

**Step 3: Install and Enable SSH on the Host PC**

Ensure SSH is installed and running:

.. code-block:: console

   $ sudo apt install ssh
   $ sudo systemctl enable ssh
   $ sudo systemctl start ssh

**Step 4: Connect to the Target Board via SSH**

Once everything is set, connect to the target board using:

.. code-block:: console

   $ sudo ssh <target_board_name>@<target_board_ip>

**Example:**

.. code-block:: console

   $ sudo ssh root@192.168.11.110

.. figure:: ../images/ssh/connect_ip.jpeg
   :alt: SSH connection to the target board
   :width: 600px
   :align: center

   **Figure 42: Successful SSH session established from the host to the embedded target board**

.. raw:: html

   <br>

.. raw:: html

   <hr style="border: 0; border-top: 3px solid #ccc; margin: 20px 0;">
