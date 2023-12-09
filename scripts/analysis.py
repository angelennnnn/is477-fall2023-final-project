import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


df = pd.read_csv('C:/Users/Angel/Desktop/IS477-finalproject/data/breast_cancer_wisconsin/breast_cancer_wisconsin.csv')
summary_stats = df.describe()
summary_stats.to_csv('results/summary_statistics.csv')

X = df.drop(['ID number', 'Diagnosis'], axis=1)
y = df['Diagnosis'].map({'M': 1, 'B': 0})  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

class_report = classification_report(y_test, y_pred)
with open('results/classification_report.txt', 'w') as f:
    f.write(class_report)

conf_matrix = confusion_matrix(y_test, y_pred)
conf_df = pd.DataFrame(conf_matrix, index=['Actual Negative', 'Actual Positive'], 
                       columns=['Predicted Negative', 'Predicted Positive'])
conf_df.to_csv('results/confusion_matrix.csv')

feature_importances = pd.Series(classifier.feature_importances_, index=X.columns)
feature_importances.nlargest(10).plot(kind='barh')
plt.title('Top 10 Feature Importances')
plt.xlabel('Relative Importance')
plt.savefig('results/feature_importances.png')
plt.close()




