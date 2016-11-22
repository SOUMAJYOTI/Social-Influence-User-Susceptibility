from sklearn.metrics import roc_curve,auc
import numpy as np
import matplotlib.pyplot as plt

def read_LIS_output(path,datatype):
    y = []
    with open(path,'r') as f:
        for line in f:
            ls = line[:-1].split("|")
            calcId = int(ls[0])
            if len(ls[1])>0:
                probVals = ls[1].split(",")
                for v in probVals:
                    y.append(float(v))
    return y


def roc_curve_(y,scores):
    fpr, tpr, thresholds = roc_curve(y, scores,pos_label=1)
    roc_auc = auc(fpr,tpr)
    return fpr,tpr,roc_auc


def plot_roc(fpr,tpr,roc_auc):
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()

if __name__ == '__main__':
    path1 = "../res_final1/0.0/lisprobVals200"
    path2 = "../res_final1/0.0/lislabels200"
    probVals = read_LIS_output(path1,'float')
    y = read_LIS_output(path2,'int')
    fpr,tpr,roc_auc = roc_curve_(y,probVals)

    plot_roc(fpr,tpr,roc_auc)