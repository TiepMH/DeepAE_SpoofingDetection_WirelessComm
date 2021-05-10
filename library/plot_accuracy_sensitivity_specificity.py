import matplotlib.pyplot as plt


def plot_acc_TPR_TNR_together(alpha_list, acc_list, TPR_list, TNR_list):
    plt.plot(alpha_list, acc_list*100,
             ' ', markerfacecolor='None', markersize=8,
             linestyle='-', linewidth=3, color='k',
             label='Accuracy')
    plt.plot(alpha_list, TPR_list*100,
             's', markerfacecolor='None', markersize=8,
             linestyle='--', linewidth=3, color='b',
             label='Sensitivity')
    plt.plot(alpha_list, TNR_list*100,
             'o', markersize=8,
             linestyle='--', linewidth=3, color='r',
             label='Specificity')
    plt.legend(loc='lower right', fontsize=12)
    plt.xlabel(r'Threshold-determining coefficient $\alpha$', fontsize=12)
    plt.ylabel(r'Performance (%)', fontsize=12)
    plt.xlim(0, 1)
    plt.ylim(0, 100.5)
    plt.tight_layout()
    plt.show()
    return None
