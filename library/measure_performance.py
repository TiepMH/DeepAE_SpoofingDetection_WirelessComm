import numpy as np
from library.mean_and_std_of_imgs import mean_of_imgs


def compute_TP_and_FN(threshold, diffs,
                      actual_imgs_are_normal=True):
    TPos = 0  # True Positive = True 'NORMAL'
    FNega = 0  # False Negative = False 'ANOMALOUS'
    num_testing_samples = len(diffs)
    for i in range(num_testing_samples):
        SSD = np.linalg.norm(diffs[i])**2
        ###
        if SSD <= threshold:
            # print("The unknown img is closer to 'NORMAL' imgs")
            if actual_imgs_are_normal == True:
                TPos += 1
            else:
                return None
        ###
        else:
            # print("The unknown img is closer to 'ANOMALOUS' imgs")
            if actual_imgs_are_normal == True:
                FNega += 1
            else:
                return None
        ###
    return TPos, FNega


def compute_FP_and_TN(threshold, diffs,
                      actual_imgs_are_anomalous=True):
    FPos = 0  # False Positive = False 'NORMAL'
    TNega = 0  # True Negative = True 'ANOMALOUS'
    num_testing_samples = len(diffs)
    for i in range(num_testing_samples):
        SSD = np.linalg.norm(diffs[i])**2
        ###
        if SSD <= threshold:
            # print("The unknown img is closer to 'NORMAL' imgs")
            if actual_imgs_are_anomalous == True:
                FPos += 1
            else:
                return None
        ###
        else:
            # print("The unknown img is closer to 'ANOMALOUS' imgs")
            if actual_imgs_are_anomalous == True:
                TNega += 1
            else:
                return None
        ###
    return FPos, TNega


def avg_diff_bw_TRAIN_in__out(imgs_train_normal,
                              imgs_train_normal_decoded):
    diffs = imgs_train_normal - imgs_train_normal_decoded
    avg_diff = mean_of_imgs(diffs)
    return avg_diff


def diffs_bw_TEST_in__out(test_input,
                          test_output_decoded):
    diffs = test_input - test_output_decoded
    return diffs


def detection_metrics(threshold,
                      imgs_train_normal,
                      imgs_train_normal_decoded,
                      imgs_test_normal,
                      imgs_test_normal_decoded,
                      imgs_test_anomalous,
                      imgs_test_anomalous_decoded):
    ###
    avg_diff_TRAIN = avg_diff_bw_TRAIN_in__out(imgs_train_normal,
                                               imgs_train_normal_decoded)
    diffs_TEST_NORMAL = diffs_bw_TEST_in__out(imgs_test_normal,
                                              imgs_test_normal_decoded)
    diffs_TEST_ANOMALOUS = diffs_bw_TEST_in__out(imgs_test_anomalous,
                                                 imgs_test_anomalous_decoded)
    diffs_normal = diffs_TEST_NORMAL - avg_diff_TRAIN
    diffs_anomalous = diffs_TEST_ANOMALOUS - avg_diff_TRAIN
    ###
    TPos, FNega = compute_TP_and_FN(threshold, diffs_normal,
                                    actual_imgs_are_normal=True)
    FPos, TNega = compute_FP_and_TN(threshold, diffs_anomalous,
                                    actual_imgs_are_anomalous=True)
    ###
    acc = (TPos + TNega)/(TPos + TNega + FPos + FNega)
    TPR = TPos/(TPos + FNega)  # True Positive Rate = Recall = Sensitivity
    FPR = FPos/(FPos + TNega)  # False Positive Rate = Fall-out
    FNR = FNega/(FNega + TPos)  # False Negative Rate = Miss rate
    TNR = TNega/(TNega + FPos)  # True Negative Rate = Specificity
    return acc, TPR, FPR, FNR, TNR
