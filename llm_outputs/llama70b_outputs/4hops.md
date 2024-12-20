### 4_1: person -> filter(RA) -> place -> device -> filter(Light) (Question:  give me a list of all Research Assistants and the Lights they own.)

-------------------------------------------------------------------------

- :Daniel, <http://example.com/td/td1> [X]
- :Zhou, <http://example.com/td/td2>
- :Sebastian, <http://example.com/td/td3> [X]
- :Micheal, <http://example.com/td/td4> [X]
- :Thomas, <http://example.com/td/td5>

real    0m6,930s
user    0m0,520s
sys     0m0,065s

[with CoT]
- :Daniel, <http://example.com/td/td1>
- :Zhou, <http://example.com/td/td2>
- :Sebastian, <http://example.com/td/td3>
- :Micheal, <http://example.com/td/td4>
- :Thomas, <http://example.com/td/td5>

real    0m6,862s
user    0m0,506s
sys     0m0,080s

### 4_2: person -> filter(RA) -> room -> filter(office) -> device (Question: give me a list of all All Research Assistants and Devices they have in Office.)

-------------------------------------------------------------------------

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1 [X] [M]
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td2 [X] [M] [M]
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td3 [X] [M]
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td4 [O]
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td5 [M]

real    0m10,223s
user    0m0,503s
sys     0m0,059s

[with CoT]

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td2
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td3
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td4
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td5

real    0m10,230s
user    0m0,531s
sys     0m0,069s

### 4_3: person -> room -> filter(office) -> device -> filter(Light) (Question: give me a list of all All person and Lights they have in Office.)

-------------------------------------------------------------------------

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1 [X]
- person: http://example.com/ontology#Tim, device: http://example.com/td/td3
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td6 [X]
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td5 [X]
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td21 [O]
- person: http://example.com/ontology#Monika, device: http://example.com/td/td10
- person: http://example.com/ontology#Andreas, device: http://example.com/td/td9
- person: http://example.com/ontology#Marco, device: http://example.com/td/td8
- person: http://example.com/ontology#Rene, device: http://example.com/td/td7 [X]
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td5
-  [M]
real    0m19,443s
user    0m0,497s
sys     0m0,074s
(nlqa) zhou@zhou-

[with CoT]

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1
- person: http://example.com/ontology#Tim, device: http://example.com/td/td3
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td6
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td5
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td21
- person: http://example.com/ontology#Monika, device: http://example.com/td/td10
- person: http://example.com/ontology#Andreas, device: http://example.com/td/td9
- person: http://example.com/ontology#Marco, device: http://example.com/td/td8
- person: http://example.com/ontology#Rene, device: http://example.com/td/td7
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td5
- person: http://example.com/ontology#Layla, device: http://example.com/td/td6

real    0m21,363s
user    0m0,512s
sys     0m0,061s

### 4_4: storey -> filter(4th) -> room -> filter(office) -> device (Question: give me a list of all All Offices in Storey 4 and the Devices contained in them.)

-------------------------------------------------------------------------

- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td1
- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td2
- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td3
- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td4
- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td17
- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td18
- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td19
- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td20
- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td35
- Storey 4: https://w3id.org/bot#Storey4, Device: http://example.com/td/td38

real    0m24,349s
user    0m0,486s
sys     0m0,073s

[with CoT]

- :Storey4, :Light (xx1)
- :Storey4, :Heater (xx17)
- :Storey4, :Light (xx2)
- :Storey4, :Heater (xx18)
- :Storey4, :Light (xx3)
- :Storey4, :Heater (xx19)
- :Storey4, :Light (xx4)
- :Storey4, :Heater (xx20)
- :Storey4, :Light (xx5)
- :Storey4, :Heater (xx21)
- :Storey4, :Light (xx6)
- :Storey4, :Heater (xx22)
- :Storey4, :Light (xx7)
- :Storey4, :Heater (xx23)
- :Storey4, :Light (xx8)
- :Storey4, :Heater (xx24)
- :Storey4, :Light (xx9)
- :Storey4, :Heater (xx25)
- :Storey4, :Light (xx10)
- :Storey4, :Heater (xx26)

real    0m19,769s
user    0m0,517s
sys     0m0,051s

### 4_5: storey -> filter(4th) -> room -> device -> filter(Light) (Question: give me a list of all All Lights contained in Storey 4.)

-------------------------------------------------------------------------
- storey: http://example.com/ontology#Storey4, device: http://example.com/td/td1
- storey: http://example.com/ontology#Storey4, device: http://example.com/td/td2
- storey: http://example.com/ontology#Storey4, device: http://example.com/td/td3
- storey: http://example.com/ontology#Storey4, device: http://example.com/td/td4
 [M] [M]
real    0m9,070s
user    0m0,602s
sys     0m0,069s



[with CoT]


- storey: https://w3id.org/bot#Storey4, device: http://example.com/td/td1
- storey: https://w3id.org/bot#Storey4, device: http://example.com/td/td2
- storey: https://w3id.org/bot#Storey4, device: http://example.com/td/td3
- storey: https://w3id.org/bot#Storey4, device: http://example.com/td/td4

real    0m9,669s
user    0m0,557s
sys     0m0,065s


### 4_6: storey -> room -> filter(office) -> device -> filter(Light) (Question: give me a list of all All Offices in All Storeys and the Lights contained in them.)

-------------------------------------------------------------------------

- :Storey4, <#4-444>, http://example.com/td/td1
- :Storey4, <#4-443>, http://example.com/td/td2
- :Storey4, <#4-442>, http://example.com/td/td3
- :Storey4, <#4-441>, http://example.com/td/td4
- :Storey3, <#3-334>, http://example.com/td/td5
- :Storey3, <#3-333>, http://example.com/td/td6
- :Storey3, <#3-332>, http://example.com/td/td7
- :Storey2, <#2-222>, http://example.com/td/td9
 [M] [M]
real    0m14,137s
user    0m0,510s
sys     0m0,067s


[with CoT]


- Storey4: https://w3id.org/bot#Storey4, device: http://example.com/td/td1
- Storey4: https://w3id.org/bot#Storey4, device: http://example.com/td/td2
- Storey4: https://w3id.org/bot#Storey4, device: http://example.com/td/td3
- Storey4: https://w3id.org/bot#Storey4, device: http://example.com/td/td4
- Storey3: https://w3id.org/bot#Storey3, device: http://example.com/td/td5
- Storey3: https://w3id.org/bot#Storey3, device: http://example.com/td/td6
- Storey3: https://w3id.org/bot#Storey3, device: http://example.com/td/td7
- Storey3: https://w3id.org/bot#Storey3, device: http://example.com/td/td8
- Storey2: https://w3id.org/bot#Storey2, device: http://example.com/td/td9
- Storey2: https://w3id.org/bot#Storey2, device: http://example.com/td/td10

real    0m23,557s
user    0m0,540s
sys     0m0,068s
