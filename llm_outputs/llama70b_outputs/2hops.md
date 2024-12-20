### 2-hop person -> room -> device (Question:  give me a list of all person and all devices the person have.)

--------------------------------------------------------------------------------------------------------
- Daniel: http://example.com/ontology#Daniel, device: http://example.com/td/td1 [x]
- Daniel: http://example.com/ontology#Daniel, device: http://example.com/td/td4
- Tim: http://example.com/ontology#Tim, device: http://example.com/td/td2 [x][m]
- Tim: http://example.com/ontology#Tim, device: http://example.com/td/td3 
- Zhou: http://example.com/ontology#Zhou, device: http://example.com/td/td6 [x][m]
- Zhou: http://example.com/ontology#Zhou, device: http://example.com/td/td38
- Sebastian: http://example.com/ontology#Sebastian, device: http://example.com/td/td5[x][m]
- Micheal: http://example.com/ontology#Micheal, device: http://example.com/td/td21[x][m][m]
- Monika: http://example.com/ontology#Monika, device: http://example.com/td/td10
- Monika: http://example.com/ontology#Monika, device: http://example.com/td/td26
- Monika: http://example.com/ontology#Monika, device: http://example.com/td/td39
- Andreas: http://example.com/ontology#Andreas, device: http://example.com/td/td9[m]
- Marco: http://example.com/ontology#Marco, device: http://example.com/td/td7 [x]
- Marco: http://example.com/ontology#Marco, device: http://example.com/td/td36 [x]
- Rene: http://example.com/ontology#Rene, device: http://example.com/td/td22 [m][m]
- Thomas: http://example.com/ontology#Thomas, device: http://example.com/td/td6 [x][m]
- Layla: http://example.com/ontology#Layla, device: http://example.com/td/td37 [x][m][m]

real    0m33,479s
user    0m0,541s
sys     0m0,067s

[with CoT: seems better?]

- Daniel: http://example.com/ontology#Daniel, device: http://example.com/td/td1
- Daniel: http://example.com/ontology#Daniel, device: http://example.com/td/td4
- Tim: http://example.com/ontology#Tim, device: http://example.com/td/td3
- Zhou: http://example.com/ontology#Zhou, device: http://example.com/td/td2
- Sebastian: http://example.com/ontology#Sebastian, device: http://example.com/td/td5
- Micheal: http://example.com/ontology#Micheal, device: http://example.com/td/td6
- Monika: http://example.com/ontology#Monika, device: http://example.com/td/td10
- Andreas: http://example.com/ontology#Andreas, device: http://example.com/td/td9
- Marco: http://example.com/ontology#Marco, device: http://example.com/td/td8
- Rene: http://example.com/ontology#Rene, device: http://example.com/td/td7
- Thomas: http://example.com/ontology#Thomas, device: http://example.com/td/td5
- Layla: http://example.com/ontology#Layla, device: http://example.com/td/td6

real    0m23,759s
user    0m0,529s
sys     0m0,071s




--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------




### 2-hop  storey -> room -> device (Question:  give me a list of all storeys and all devices in each storey.)

--------------------------------------------------------------------------------------------------------

- Storey: https://w3id.org/bot#Storey1, Device: None 
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td9, http://example.com/td/td10, http://example.com/td/td11, http://example.com/td/td12, http://example.com/td/td25, http://example.com/td/td26, http://example.com/td/td40, http://example.com/td/td41, http://example.com/td/td42, http://example.com/td/td43 [m][m]
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td5, http://example.com/td/td6, http://example.com/td/td7, http://example.com/td/td8, http://example.com/td/td13, http://example.com/td/td14, http://example.com/td/td21, http://example.com/td/td22, http://example.com/td/td23, http://example.com/td/td24, http://example.com/td/td27, http://example.com/td/td28, http://example.com/td/td29, http://example.com/td/td30, http://example.com/td/td34[m][m][m][m]
- Storey: https://w3id.org/bot#Storey4, Device: http://example.com/td/td1, http://example.com/td/td2, http://example.com/td/td3, http://example.com/td/td4, http://example.com/td/td15, http://example.com/td/td16, http://example.com/td/td17, http://example.com/td/td18, http://example.com/td/td19, http://example.com/td/td20, http://example.com/td/td31, http://example.com/td/td32, http://example.com/td/td33, http://example.com/td/td35, http://example.com/td/td36,[x] http://example.com/td/td37,[o] http://example.com/td/td38, http://example.com/td/td39[o]

real    0m39,428s
user    0m0,510s
sys     0m0,057s


[with CoT: seems better]
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
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td27
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td28
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td29
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td30
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td31
- Storey: https://w3id.org/bot#Storey3, Device: http://example.com/td/td36
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td9
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td10
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td11
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td12
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td25
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td26
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td40
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td41
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td42
- Storey: https://w3id.org/bot#Storey2, Device: http://example.com/td/td43

real    1m18,444s
user    0m0,690s
sys     0m0,062s

--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------

