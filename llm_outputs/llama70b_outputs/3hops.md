### 3_1: person -> place -> device -> filter(Light) (Question:  give me a list of all person and all the lights the person have)

-------------------------------------------------------------------------------

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1
- person: http://example.com/ontology#Tim, device: http://example.com/td/td3
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td5
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td7
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td9
- person: http://example.com/ontology#Monika, device: http://example.com/td/td11
- person: http://example.com/ontology#Andreas, device: http://example.com/td/td13
- person: http://example.com/ontology#Marco, device: http://example.com/td/td15
- person: http://example.com/ontology#Rene, device: http://example.com/td/td17
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td19
- person: http://example.com/ontology#Layla, device: http://example.com/td/td21
real    0m21,456s
user    0m0,542s
sys     0m0,074s


[with CoT]

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1
- person: http://example.com/ontology#Tim, device: http://example.com/td/td3
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td6
- person: http://example.com/ontology#Sebastian, device: None
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td5
- person: http://example.com/ontology#Monika, device: http://example.com/td/td10
- person: http://example.com/ontology#Andreas, device: None
- person: http://example.com/ontology#Marco, device: http://example.com/td/td8
- person: http://example.com/ontology#Rene, device: None
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td7
- person: http://example.com/ontology#Layla, device: http://example.com/td/td9

real    0m19,491s
user    0m0,510s
sys     0m0,068s

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------


### 3_2: person -> room -> filter(office) -> device (Question:  give me a list of all person and their devices that are in an office room.)

-------------------------------------------------------------------------------

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1
- person: http://example.com/ontology#Tim, device: http://example.com/td/td3
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td6
- person: http://example.com/ontology#Sebastian, device: None
- person: http://example.com/ontology#Micheal, device: None
- person: http://example.com/ontology#Monika, device: None
- person: http://example.com/ontology#Andreas, device: None
- person: http://example.com/ontology#Marco, device: None
- person: http://example.com/ontology#Rene, device: None
- person: http://example.com/ontology#Thomas, device: None
- person: http://example.com/ontology#Layla, device: None

real    0m16,502s
user    0m0,521s
sys     0m0,053s


[with CoT]

- person: http://example.com/td/Daniel, device: http://example.com/td/td1
- person: http://example.com/td/Tim, device: http://example.com/td/td3
- person: http://example.com/td/Zhou, device: http://example.com/td/td6
- person: http://example.com/td/Micheal, device: http://example.com/td/td5

real    0m8,112s
user    0m0,508s
sys     0m0,072s


-------------------------------------------------------------------------------
-------------------------------------------------------------------------------


### 3_3: person -> filter(RA) -> room -> device (Question:  give me a list of all research assistant and the devices they have)

-------------------------------------------------------------------------------

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1[x][m]
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td2 [m][m]
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td3[x][m]
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td4[x][m][m]
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td5 [m]

real    0m10,232s
user    0m0,585s
sys     0m0,076s



[with CoT]

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td2
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td3
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td4
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td5

real    0m10,247s
user    0m0,539s
sys     0m0,073s


-------------------------------------------------------------------------------
-------------------------------------------------------------------------------



### 3_4: storey -> room -> device -> filter(Light) (Question:  give me a list of all storeys and the lights contained in them.)

-------------------------------------------------------------------------------




[with CoT]

- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td1
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td2
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td3
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td4
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td5 [x] [m]
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td6
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td7
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td8 [m][m][m]
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td9
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td10 [m][m]

real    0m22,674s
user    0m0,533s
sys     0m0,061s


-------------------------------------------------------------------------------
-------------------------------------------------------------------------------


### 3_5: storey -> room -> filter(office) -> device (Question:  give me a list of all storeys and the devices that are contained in office room.)

-------------------------------------------------------------------------------

(nlqa) zhou@zhou-thinkpad:~/Documents/Reasoner_jena/llm_reasoning$ time python llama_70b.py
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td1
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td2
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td3
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td4
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td17
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td18
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td19
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td20
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td35
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td38
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td5
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td6
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td7
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td8
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td21
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td22
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td23
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td24
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td36 [m]
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td9
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td10
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td25 [m][m]

real    1m2,206s
user    0m0,544s
sys     0m0,102s



[with CoT]

- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td1
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td2
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td3
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td4
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td17
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td18
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td19
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td20
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td35
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td38
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td39
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td5
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td6
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td7
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td8
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td21
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td22
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td23
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td24
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td36
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td9
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td10

real    0m49,272s
user    0m0,562s
sys     0m0,051s



-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

### 3_6: storey -> filter(4th)-> room -> device (Question:  give me a list of all devices in the 4th storey.)
-------------------------------------------------------------------------------
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td1
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td2
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td3
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td4
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td17
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td18
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td19
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td20
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td35
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td38
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td39[x][m][m][m][m][m]

real    0m25,014s
user    0m0,513s
sys     0m0,057s




[with CoT]

- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td1
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td2
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td3
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td4
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td17
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td18
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td19
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td20
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td35
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td37
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td38
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td39

real    0m27,288s
user    0m0,542s
sys     0m0,063s


-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
