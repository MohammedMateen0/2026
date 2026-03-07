from sklearn.model_selection import KFold,StratifiedKFold,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
data =load_breast_cancer()
X=data.data
y=data.target
model=LogisticRegression(max_iter=10000)
kf=KFold(n_splits=5,shuffle=True,random_state=42)
scores=cross_val_score(model,X,y,cv=kf)
print("K-Fold Scores: ",scores)
print("Average SCore: ",scores.mean())
skf=StratifiedKFold(n_splits=5,shuffle=True,random_state=42)
scores_stratified=cross_val_score(model,X,y,cv=skf)
print("Stratified Scores: ",scores_stratified)
print("Average Stratified Score: ",scores_stratified.mean())