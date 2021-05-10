import numpy as np
import matplotlib.pyplot as plt
from library.class_AE import get_compiled_model
from library.save_and_load_AE_model import save_my_model
from class_SysParam import SystemParameters

from library.define_folder_name import my_folder_name
import pickle

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # use CPU

""" Load the system parameters """
SysParam = SystemParameters()
n_Tx = SysParam.n_Tx  # number of transmitters
n_Rx = SysParam.n_Rx  # number of receive antennas
snrdB_Bob = SysParam.snrdB_Bob  # in dB
snrdB_Eve = SysParam.snrdB_Eve  # in dB
DOA_Bob_list = SysParam.DOA_Bob_list  # in degrees
DOA_Eve = SysParam.DOA_Eve  # in degrees
K = SysParam.Rician_factor
NLOS = SysParam.n_NLOS_paths

""" Name the folder that contains the data """
folder_name = my_folder_name(n_Tx, n_Rx,
                             snrdB_Bob, DOA_Bob_list,
                             snrdB_Eve, DOA_Eve,
                             K, NLOS)

###
cur_path = os.path.abspath(os.getcwd())
path_to_datasets = os.path.join(cur_path, 'input/' + folder_name)

anomalous_imgs_train = np.load(path_to_datasets + '/imgs_train_anomalous.npy')
normal_imgs_train = np.load(path_to_datasets + '/imgs_train_normal.npy')
imgs_test = np.load(path_to_datasets + '/imgs_test.npy')

# ============================================================================
num_angles = 180
angles = np.linspace(-num_angles/2, num_angles/2, num_angles)

# ============================================================================
plt.grid()
plt.plot(angles, anomalous_imgs_train[0])
plt.title("An Anomalous Spectrum")
plt.show()

""" Plot an normal SPECTRUM """
plt.grid()
plt.plot(angles, normal_imgs_train[0])
plt.title("A Normal Spectrum")
plt.show()

# =============================================================================
""" Compile and train the AUTO-ENCODER model """
model = get_compiled_model(num_angles)
history = model.fit(normal_imgs_train,
                    normal_imgs_train,
                    epochs=100, batch_size=2**6,
                    validation_data=(imgs_test, imgs_test),
                    shuffle=True, verbose=False)

# =============================================================================
""" Plot the loss function during training """
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.legend()
plt.show()

# =============================================================================
""" Save the trained AUTO-ENCODER model """
save_my_model(model, folder_name)
del model
