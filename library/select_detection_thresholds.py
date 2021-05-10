import numpy as np
from library.mean_and_std_of_imgs import mean_of_imgs, std_of_imgs


def thrsh_based_on_diff_bw_out__avg_in(imgs_train_normal,
                                       imgs_train_normal_decoded):
    # diffs = imgs_train_normal_decoded - imgs_train_normal
    diffs = imgs_train_normal_decoded - mean_of_imgs(imgs_train_normal)
    # diffs.shape = [number of imgs in the training data, number of angles]
    # avg_diff = mean_of_imgs(diffs)  # shape = (number of angles,)
    std_diff = std_of_imgs(diffs)  # shape = (number of angles,)
    threshold = np.linalg.norm(std_diff)**2
    return threshold


def thrsh_based_on_diff_bw_out__in(imgs_train_normal,
                                   imgs_train_normal_decoded):
    diffs = imgs_train_normal_decoded - imgs_train_normal
    std_diff = std_of_imgs(diffs)  # shape = (number of angles,)
    threshold = np.linalg.norm(std_diff)**2
    return threshold
