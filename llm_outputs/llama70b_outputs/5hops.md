### 5_1_1: person -> filter(RA&ExternalPhD) -> place -> filter (office) -> device -> filter(light) (Question: give me a list of all Research Assistants in Offices and the Lights they own.)

--------------------------------------RA + Light----------------------------------------------

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1 [X]
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td2
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td3 [X]
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td4 [o]
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td5

real    0m10,184s
user    0m0,512s
sys     0m0,057s

[with CoT]


- person: http://example.com/ontology#Daniel, device: http://example.com/td/td1
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td2
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td3
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td4
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td5

real    0m10,159s
user    0m0,503s
sys     0m0,068s

----------------------------------------External PhD Students + light --------------------------------------------

- person: http://example.com/td/Tim, device: http://example.com/td/td3.
- person: http://example.com/td/Rene, device: None. [M]
- person: http://example.com/td/Marco, device: None. [M]

real    0m5,137s
user    0m0,539s
sys     0m0,065s


[with CoT]


- person: http://example.com/td/Tim, device: http://example.com/td/td3.
- person: http://example.com/td/Rene, device: None.
- person: http://example.com/td/Marco, device: None.

real    0m5,234s
user    0m0,535s
sys     0m0,062s


### 5_1_2: person -> filter(RA&ExternalPhD) -> place ->filter (office) -> device -> filter(heater) (Question: give me a list of all Research Assistants in Offices and the
eaters they own.)

------------------------------------------RA + heater------------------------------------------

- person: http://example.com/ontology#Daniel, device: http://example.com/td/td17 [X]
- person: http://example.com/ontology#Zhou, device: http://example.com/td/td22 [X]
- person: http://example.com/ontology#Sebastian, device: http://example.com/td/td21 [X]
- person: http://example.com/ontology#Thomas, device: http://example.com/td/td25 [X]
- person: http://example.com/ontology#Micheal, device: http://example.com/td/td24 [O]

real    0m10,170s
user    0m0,493s
sys     0m0,075s



[with CoT]

- person: http://example.com/td/Daniel, device: http://example.com/td/td19
- person: http://example.com/td/Zhou, device: http://example.com/td/td22
- person: http://example.com/td/Micheal, device: http://example.com/td/td24

real    0m6,227s
user    0m0,519s
sys     0m0,058s




----------------------------------------External PhD Students + heater --------------------------------------------

- person: http://example.com/td/Tim, device: http://example.com/td/td19.
- person: http://example.com/td/Rene, device: http://example.com/td/td20. [X]
- person: http://example.com/td/Marco, device: http://example.com/td/td21. [X]

real    0m6,473s
user    0m0,494s
sys     0m0,053s


[with CoT]

- person: https://w3id.org/bot#Tim, device: http://example.com/td/td19
- person: https://w3id.org/bot#Rene, device: http://example.com/td/td21
- person: https://w3id.org/bot#Marco, device: http://example.com/td/td22

real    0m6,831s
user    0m0,533s
sys     0m0,057s




### 5_2_1: storey ->filter(4&3th)-> room -> filter(office) -> device -> filter(light) (Question: give me a list of all Offices in Storey 4 and the Lights contained in them.)

----------------------------------------4th + Light--------------------------------------------

- Office: <#4-444>, Light: <http://example.com/td/td1>
- Office: <#4-443>, Light: <http://example.com/td/td2>
- Office: <#4-442>, Light: <http://example.com/td/td3>
- Office: <#4-441>, Light: <http://example.com/td/td4>

real    0m7,491s
user    0m0,503s
sys     0m0,067s


[with CoT]

- Office: <#4-444>, Light: <http://example.com/td/td1>
- Office: <#4-443>, Light: <http://example.com/td/td2>
- Office: <#4-442>, Light: <http://example.com/td/td3>
- Office: <#4-441>, Light: <http://example.com/td/td4>

real    0m7,633s
user    0m0,612s
sys     0m0,052s


--------------------------------------3th + Light----------------------------------------------

- Office: <#3-334>, Light: <http://example.com/td/td5>
- Office: <#3-333>, Light: <http://example.com/td/td6>
- Office: <#3-332>, Light: <http://example.com/td/td7>
-  [M]

real    0m5,891s
user    0m0,494s
sys     0m0,051s


[with CoT]


- Office: <#3-334>, Light: <http://example.com/td/td5>
- Office: <#3-333>, Light: <http://example.com/td/td6>
- Office: <#3-332>, Light: <http://example.com/td/td7>

real    0m5,870s
user    0m0,503s
sys     0m0,066s


### 5_2_2: storey ->filter(4_3th)-> room -> filter(office) -> device -> filter(Heater) (Question: give me a list of all Offices in Storey 4 and the Heaters contained in them.)

----------------------------------4th + Heater--------------------------------------------------

- Office: <#4-444>, Heater: <http://example.com/td/td17>
- Office: <#4-443>, Heater: <http://example.com/td/td18>
- Office: <#4-442>, Heater: <http://example.com/td/td19>
- Office: <#4-441>, Heater: <http://example.com/td/td20>

real    0m7,905s
user    0m0,580s
sys     0m0,079s

[with CoT]

- Office: <#4-444>, Heater: <http://example.com/td/td17>
- Office: <#4-443>, Heater: <http://example.com/td/td18>
- Office: <#4-442>, Heater: <http://example.com/td/td19>
- Office: <#4-441>, Heater: <http://example.com/td/td20>

real    0m7,566s
user    0m0,594s
sys     0m0,059s



-------------------------------------3th + Heater-----------------------------------------------

- Office: <#3-334>, Heater: <http://example.com/td/td21>
- Office: <#3-333>, Heater: <http://example.com/td/td22>
- Office: <#3-332>, Heater: <http://example.com/td/td23>
 [M]
real    0m6,205s
user    0m0,520s
sys     0m0,066s



[with CoT]

- Office: <#3-334>, Heater: <http://example.com/td/td21>
- Office: <#3-333>, Heater: <http://example.com/td/td22>
- Office: <#3-332>, Heater: <http://example.com/td/td23>

real    0m5,887s
user    0m0,508s
sys     0m0,067s
