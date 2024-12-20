### 5_1_1: person -> filter(RA&ExternalPhD) -> place ->filter (office) -> device -> filter(light) (Question: give me a list of all Research Assistants in Offices and the Lights they own.)
--------------------------------------RA + Light----------------------------------------------

- person: :Daniel, device: <http://example.com/td/td4>
- person: :Zhou, device: <http://example.com/td/td2>
- person: :Sebastian, device: <http://example.com/td/td1>
- person: :Micheal, device: <http://example.com/td/td15> [O]
- person: :Thomas, device: <http://example.com/td/td5>

real    0m4,235s
user    0m0,362s
sys     0m0,047s

[with CoT]

- person: :Daniel, device: <http://example.com/td/td4>
- person: :Zhou, device: <http://example.com/td/td2>
- person: :Sebastian, device: <http://example.com/td/td1>
- person: :Micheal, device: <http://example.com/td/td15>
- person: :Thomas, device: <http://example.com/td/td5>

real    0m3,418s
user    0m0,391s
sys     0m0,053s

-----------------------------------------External PhD Students + Light-------------------------------------------

- person: :Tim, device: <http://example.com/td/td3>
- person: :Marco, device: <http://example.com/td/td8>
- person: :Rene, device: <http://example.com/td/td6>

real    0m2,797s
user    0m0,409s
sys     0m0,046s

[with CoT]

- person: :Tim, device: <http://example.com/td/td3>
- person: :Marco, device: <http://example.com/td/td8>
- person: :Rene, device: <http://example.com/td/td6>

real    0m2,819s
user    0m0,403s
sys     0m0,026s

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------


### 5_1_2: person -> filter(RA&ExternalPhD) -> place ->filter (office) -> device -> filter(heater) (Question: give me a list of all Research Assistants in Offices and the heater they own.)

------------------------------------------RA + Heater------------------------------------------

- person: :Daniel, device: <http://example.com/td/td20>
- person: :Zhou, device: <http://example.com/td/td18>
- person: :Sebastian, device: <http://example.com/td/td17>
- person: :Micheal, device: <http://example.com/td/td31> [O]
- person: :Thomas, device: <http://example.com/td/td21>

real    0m3,635s
user    0m0,392s
sys     0m0,056s

[with CoT -> Actually figured out Michael should not return anything, not sure it's because Michael is not in an office or there is no heater (but AC) in the IoT lab]

- person: :Daniel, device: <http://example.com/td/td20>
- person: :Zhou, device: <http://example.com/td/td18>
- person: :Sebastian, device: <http://example.com/td/td17>
- person: :Micheal, device: none
- person: :Thomas, device: <http://example.com/td/td21>

real    0m3,040s
user    0m0,391s
sys     0m0,045s

-----------------------------------------External PhD Students + Heater-------------------------------------------

- person: :Marco, device: <http://example.com/td/td24>
- person: :Tim, device: <http://example.com/td/td19>
- person: :Rene, device: <http://example.com/td/td22>

real    0m2,892s
user    0m0,365s
sys     0m0,041s

[with CoT]

(reasoning) zhou@zhou-thinkpad:~/Documents/Reasoner_jena/llm_reasoning$ time python claude-sonnet.py
- person: :Tim, device: <http://example.com/td/td19>
- person: :Marco, device: <http://example.com/td/td24>
- person: :Rene, device: <http://example.com/td/td22>

real    0m3,579s
user    0m0,400s
sys     0m0,041s


### 5_2_1: storey ->filter(4&3th)-> room -> filter(office) -> device -> filter(light) (Question: give me a list of all Offices in Storey 4 and the Lights contained in them.)

-----------------------------------4 + Light-------------------------------------------------

- storey: <#4-444>, device: <http://example.com/td/td1>
- storey: <#4-443>, device: <http://example.com/td/td2>
- storey: <#4-442>, device: <http://example.com/td/td3>
- storey: <#4-441>, device: <http://example.com/td/td4>

real    0m3,427s
user    0m0,392s
sys     0m0,047s


[with CoT]

- storey: <#4-444>, device: <http://example.com/td/td1>
- storey: <#4-443>, device: <http://example.com/td/td2>
- storey: <#4-442>, device: <http://example.com/td/td3>
- storey: <#4-441>, device: <http://example.com/td/td4>

real    0m2,946s
user    0m0,376s
sys     0m0,033s

-------------------------------------------3 + Light-----------------------------------------

- storey: <#3-334>, device: <http://example.com/td/td5>
- storey: <#3-333>, device: <http://example.com/td/td6>
- storey: <#3-332>, device: <http://example.com/td/td7>
- storey: <#3-331>, device: <http://example.com/td/td8>

real    0m3,497s
user    0m0,376s
sys     0m0,035s

[with CoT]

- storey: <#3-334>, device: <http://example.com/td/td5>
- storey: <#3-333>, device: <http://example.com/td/td6>
- storey: <#3-332>, device: <http://example.com/td/td7>
- storey: <#3-331>, device: <http://example.com/td/td8>

real    0m3,240s
user    0m0,390s
sys     0m0,042s
----------------------------------------4 + heater--------------------------------------------

- storey: <#4-444>, device: <http://example.com/td/td17>
- storey: <#4-443>, device: <http://example.com/td/td18>
- storey: <#4-442>, device: <http://example.com/td/td19>
- storey: <#4-441>, device: <http://example.com/td/td20>

real    0m3,545s
user    0m0,381s
sys     0m0,042s

[with CoT]

- storey: <#4-444>, device: <http://example.com/td/td17>
- storey: <#4-443>, device: <http://example.com/td/td18>
- storey: <#4-442>, device: <http://example.com/td/td19>
- storey: <#4-441>, device: <http://example.com/td/td20>

real    0m3,337s
user    0m0,372s
sys     0m0,052s

----------------------------------------3 + heater--------------------------------------------

- storey: <#3-334>, device: <http://example.com/td/td21>
- storey: <#3-333>, device: <http://example.com/td/td22>
- storey: <#3-332>, device: <http://example.com/td/td23>
- storey: <#3-331>, device: <http://example.com/td/td24>

real    0m4,692s
user    0m0,412s
sys     0m0,049s

[with CoT]

- storey: <#3-334>, device: <http://example.com/td/td21>
- storey: <#3-333>, device: <http://example.com/td/td22>
- storey: <#3-332>, device: <http://example.com/td/td23>
- storey: <#3-331>, device: <http://example.com/td/td24>

real    0m3,620s
user    0m0,375s
sys     0m0,056s
