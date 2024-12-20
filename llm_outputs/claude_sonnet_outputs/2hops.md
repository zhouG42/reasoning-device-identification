### 2-hop person -> room -> device (Question:  give me a list of all person and all devices the person have.)
--------------------------------------------------------------------------------------------------------
I'll analyze the knowledge graph to list each person and the devices in their work location. A device is considered to belong to a person if it's in their work location (schema:workLocation).

Here's the breakdown:

1. Daniel (Room 4.441):
   - Light (td4)
   - Heater (td20)

2. Tim (Room 4.442):
   - Light (td3)
   - Heater (td19)
   - LED Strip (td35)

3. Zhou (Room 4.443):
   - Light (td2)
   - Heater (td18)
   - Kettle (td38)

4. Sebastian (Room 4.444):
   - Light (td1)
   - Heater (td17)

5. Michael (Room 4.436 - IoT Lab):
   - Light (td15)
   - Lock (td28)
   - AC (td31)

6. Monika (Room 2.221 - Secretary):
   - Light (td10)
   - Heater (td26)
   - Coffee Machine (td39)

7. Andreas (Room 2.222):
   - Light (td9)
   - Heater (td25)

8. Marco (Room 3.331):
   - Light (td8)
   - Heater (td24)

9. Rene (Room 3.333):
   - Light (td6)
   - Heater (td22)
   - Radio (td37)

10. Thomas (Room 3.334):
    - Light (td5)
    - Heater (td21)

11. Layla (Room 4.443):
    - Light (td2)
    - Heater (td18)
    - Kettle (td38)
    (Shares room with Zhou)

Note: Devices that have :personalDevice true are particularly relevant to the person working in that space, while devices with :personalDevice false are more general building infrastructure.

real    0m8,587s
user    0m0,487s
sys     0m0,051s
--------------------------------------------------------------------------------------------------------
I'll analyze the knowledge graph and list each person along with the devices in their workspace (workLocation). A device is considered to belong to a person if it's in their workLocation.

Here's the breakdown:

1. Daniel (Room 4.441):
   - Light (td4)
   - Heater (td20)

2. Tim (Room 4.442):
   - Light (td3)
   - Heater (td19)
   - LED Strip (td35)

3. Zhou (Room 4.443):
   - Light (td2)
   - Heater (td18)
   - Kettle (td38)

4. Sebastian (Room 4.444):
   - Light (td1)
   - Heater (td17)

5. Michael (Room 4.436 - IoT Lab):
   - Light (td15)
   - Lock (td28)
   - AC (td31)

6. Monika (Room 2.221 - Secretary):
   - Light (td10)
   - Heater (td26)
   - Coffee Machine (td39)

7. Andreas (Room 2.222):
   - Light (td9)
   - Heater (td25)

8. Marco (Room 3.331):
   - Light (td8)
   - Heater (td24)

9. Rene (Room 3.333):
   - Light (td6)
   - Heater (td22)
   - Radio (td37)

10. Thomas (Room 3.334):
    - Light (td5)
    - Heater (td21)

11. Layla (Room 4.443):
    - Light (td2)
    - Heater (td18)
    - Kettle (td38)
    (Shares room with Zhou)

This list shows all devices in each person's workspace. Note that some people share rooms and therefore share access to the same devices.

real    0m8,103s
user    0m0,473s
sys     0m0,045s

--------------------------------------------------------------------------------------------------------
I'll analyze the knowledge graph to list each person and the devices in their work location. A device is considered to belong to a person if it's in their work location (connected through schema:workLocation and bot:containsElement).

Here's the breakdown:

1. Daniel (Room #4-441):
- Light (td4)
- Heater (td20)

2. Tim (Room #4-442):
- Light (td3)
- Heater (td19)
- LedStrip (td35)

3. Zhou (Room #4-443):
- Light (td2)
- Heater (td18)
- Kettle (td38)

4. Sebastian (Room #4-444):
- Light (td1)
- Heater (td17)

5. Michael (Room #4-436):
- Light (td15)
- Lock (td28)
- AC (td31)

6. Monika (Room #2-221):
- Light (td10)
- Heater (td26)
- CoffeeMachine (td39)

7. Andreas (Room #2-222):
- Light (td9)
- Heater (td25)

8. Marco (Room #3-331):
- Light (td8)
- Heater (td24)

9. Rene (Room #3-333):
- Light (td6)
- Heater (td22)
- Radio (td37)

10. Thomas (Room #3-334):
- Light (td5)
- Heater (td21)

11. Layla (Room #4-443):
- Light (td2)
- Heater (td18)
- Kettle (td38)
(Shares office with Zhou)

This list shows all devices in each person's work location. Note that some people share offices and thus have access to the same devices.

real    0m7,998s
user    0m0,422s
sys     0m0,052s

--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------



### 2-hop  storey -> room -> device (Question:  give me a list of all storeys and all devices in each storey.)
--------------------------------------------------------------------------------------------------------
I'll analyze the knowledge graph and list all storeys and their devices:

Storey 4 (WiSo 4th Floor):
- Room 4.444: Light (td1), Heater (td17)
- Room 4.443: Light (td2), Heater (td18), Kettle (td38)
- Room 4.442: Light (td3), Heater (td19), LedStrip (td35)
- Room 4.441: Light (td4), Heater (td20)
- Room 4.436 (IoT Lab): Light (td15), Lock (td28), AC (td31)
- Room 4.435 (Meeting Room): Light (td16), TV (td32), Speaker (td33)

Storey 3 (WiSo 3rd Floor):
- Room 3.334: Light (td5), Heater (td21)
- Room 3.333: Light (td6), Heater (td22), Radio (td37)
- Room 3.332: Light (td7), Heater (td23), Display (td36)
- Room 3.331: Light (td8), Heater (td24)
- Room 3.326 (Technical Room): Light (td13), Lock (td27), Camera (td29)
- Room 3.325 (Copy Room): Light (td14), Camera (td30), Alarm (td34)

Storey 2 (WiSo 2nd Floor):
- Room 2.222: Light (td9), Heater (td25)
- Room 2.221 (Secretary): Light (td10), Heater (td26), CoffeeMachine (td39)
- Room 2.216 (Kitchen): Light (td11), Microwave (td40), Dishwasher (td41)
- Room 2.215 (Toilet): Light (td12), Dryer (td42), Ventilator (td43)

real    0m7,971s
user    0m0,411s
sys     0m0,050s

--------------------------------------------------------------------------------------------------------
I'll analyze the knowledge graph and create a list of all storeys and their devices. I'll organize this by storey and include all devices found in spaces on each floor.

**Storey 4 (WiSo 4th Floor)**
- Room 4.444: Light (td1), Heater (td17)
- Room 4.443: Light (td2), Heater (td18), Kettle (td38)
- Room 4.442: Light (td3), Heater (td19), LedStrip (td35)
- Room 4.441: Light (td4), Heater (td20)
- Room 4.436 (IoT Lab): Light (td15), Lock (td28), AC (td31)
- Room 4.435 (Meeting Room): Light (td16), TV (td32), Speaker (td33)

**Storey 3 (WiSo 3rd Floor)**
- Room 3.334: Light (td5), Heater (td21)
- Room 3.333: Light (td6), Heater (td22), Radio (td37)
- Room 3.332: Light (td7), Heater (td23), Display (td36)
- Room 3.331: Light (td8), Heater (td24)
- Room 3.326 (Technical Room): Light (td13), Lock (td27), Camera (td29)
- Room 3.325 (Copy Room): Light (td14), Camera (td30), Alarm (td34)

**Storey 2 (WiSo 2nd Floor)**
- Room 2.222: Light (td9), Heater (td25)
- Room 2.221 (Secretary): Light (td10), Heater (td26), CoffeeMachine (td39)
- Room 2.216 (Kitchen): Light (td11), Microwave (td40), Dishwasher (td41)
- Room 2.215 (Toilet): Light (td12), Dryer (td42), Ventilator (td43)

real    0m8,577s
user    0m0,475s
sys     0m0,068s


--------------------------------------------------------------------------------------------------------
I'll analyze the knowledge graph and list all storeys and their devices:

Storey 4 (WiSo 4th Floor):
- Room 4.444: Light (td1), Heater (td17)
- Room 4.443: Light (td2), Heater (td18), Kettle (td38)
- Room 4.442: Light (td3), Heater (td19), LedStrip (td35)
- Room 4.441: Light (td4), Heater (td20)
- Room 4.436 (IoT Lab): Light (td15), Lock (td28), AC (td31)
- Room 4.435 (Meeting Room): Light (td16), TV (td32), Speaker (td33)

Storey 3 (WiSo 3rd Floor):
- Room 3.334: Light (td5), Heater (td21)
- Room 3.333: Light (td6), Heater (td22), Radio (td37)
- Room 3.332: Light (td7), Heater (td23), Display (td36)
- Room 3.331: Light (td8), Heater (td24)
- Room 3.326 (Technical Room): Light (td13), Lock (td27), Camera (td29)
- Room 3.325 (Copy Room): Light (td14), Camera (td30), Alarm (td34)

Storey 2 (WiSo 2nd Floor):
- Room 2.222: Light (td9), Heater (td25)
- Room 2.221 (Secretary): Light (td10), Heater (td26), CoffeeMachine (td39)
- Room 2.216 (Kitchen): Light (td11), Microwave (td40), Dishwasher (td41)
- Room 2.215 (Toilet): Light (td12), Dryer (td42), Ventilator (td43)

real    0m10,337s
user    0m0,406s
sys     0m0,050s


--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
