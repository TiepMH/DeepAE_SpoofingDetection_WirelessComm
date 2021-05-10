# Deep Auto-Encoders for Anomaly Detection with 2 legitimate users and 1 eavesdropper

A system that consists of TWO legitimate users and ONE eavesdropper is considered.

Conventionally, the legitimate users (Bob_1 and Bob_2) sends a signal to a base station (BS) to request access to the network. In the case that Eve keeps silent and the BS authenticates Bob's signal correctly, then the signal will be labelled as NORMAL.

However, if Eve impersonates Bob_1 (or Bob_2), then the BS must be capable of detecting if its received signal is associated with Eve or not. In the case the detection is correct, then the signal received at the BS will be labelled as ANOMALOUS. By contrast, the signal will be labelled NORMAL, in this case, we have false detection because the received signal (constituted by Bob's transmitted signal and Eve's transmitted signal) is misunderstood as a normal signal.

---
The goal is to detect if the signal received at the BS is associated with a spoofing attack or not.

---
![alt text](
https://github.com/TiepMH/AE_for_Anomaly_Detection__with_2_legitimate_users_and_1_eavesdropper/blob/main/Figure_1.png
)

![alt text](
https://github.com/TiepMH/AE_for_Anomaly_Detection__with_2_legitimate_users_and_1_eavesdropper/blob/main/Figure_2.png
)

![alt text](
https://github.com/TiepMH/AE_for_Anomaly_Detection__with_2_legitimate_users_and_1_eavesdropper/blob/main/Figure_2.png
)

![alt text](
https://github.com/TiepMH/AE_for_Anomaly_Detection__with_2_legitimate_users_and_1_eavesdropper/blob/main/Figure_4.png
)

---
Used packages include:
- tensorflow
- numpy
- matplotlib
- sklearn
- scipy
- pickle
- os, pathlib
---

---
Styles:
- Object-oriented programming
- PEP 8
