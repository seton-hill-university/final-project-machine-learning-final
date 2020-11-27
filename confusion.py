from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def confusionMatrix(y, x, predict):
    y_test = y
    x_test = x
    p = predict
    labels = [0, 1, 2, 3]

    conMat = confusion_matrix(y_test, p)

    disp = ConfusionMatrixDisplay(confusion_matrix=conMat, display_labels=labels)
    disp = disp.plot(include_values=True)
    plt.show()

#    print(conMat)
 #   print(classification_report(y_test, p))