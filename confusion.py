from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Let's create and display a confusion matrix to show the accuracy of our decisiontree model
def confusionMatrix(y, predict):
    y_test = y #test sample
    p = predict #prediction made by the decision tree
    labels = ['allow', 'deny', 'drop', 'reset-both'] #labels for the graphical display

    conMat = confusion_matrix(y_test, p) # use the sklearn kit to generate a confusion matrix by comparing true v predict

    # set up the display data for the confusion matrix
    disp = ConfusionMatrixDisplay(confusion_matrix=conMat, display_labels=labels)
    disp = disp.plot(include_values=True) # plot the data
    plt.show() # display the confusion matrix