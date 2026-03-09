from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score,recall_score,f1_score
y_true=[1,0,1,1,0,1,0,0,1,0]
y_pred=[1,0,1,0,0,1,0,1,1,0]
cm=confusion_matrix(y_true,y_pred)
print("confusion Matrix:")
print(cm)
precision=precision_score(y_true,y_pred)
print("Precision Score")
print(precision)
recall=recall_score(y_true,y_pred)
print("Recall Score")
print(recall)
f1score=f1_score(y_true,y_pred)
print('F1 Score')
print(f1score)