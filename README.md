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
Styles:
- Object-oriented programming
- PEP 8

---
NOTE for 'az_MAIN.py'
1) If you do NOT want to re-create the datasets, you should make lines 15 and 17 comments.

<img src="https://github.com/TiepMH/AE_for_Anomaly_Detection__with_2_legitimate_users_and_1_eavesdropper/blob/fb23647221776cd27f7a09c25b6a88c1110c2a60/library/Remove_parts_1_and_2.png" width="50%" height="50%">

2) If you do NOT want to re-create the datasets and do NOT want to re-train a deep neural network, you should make lines 15, 17 and 19 comments.

<img src="https://github.com/TiepMH/AE_for_Anomaly_Detection__with_2_legitimate_users_and_1_eavesdropper/blob/fb23647221776cd27f7a09c25b6a88c1110c2a60/library/Remove_parts_1_2_and_3.png?s=100" width="50%" height="50%">

3) If you only want to see some intuitive results immediately, you should make lines 15, 17, 19 and 21 comments.

<img src="https://github.com/TiepMH/AE_for_Anomaly_Detection__with_2_legitimate_users_and_1_eavesdropper/blob/fb23647221776cd27f7a09c25b6a88c1110c2a60/library/Remove_parts_1_2_3_and_4.png" width="50%" height="50%">

