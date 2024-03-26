from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression as lg
from sklearn.model_selection import train_test_split as ts
# Load the digits dataset
digits = load_digits()

# Set the colormap to grayscale
plt.gray() 

# # Display the first 5 digits
# for i in range(5):
#     plt.matshow(digits.images[i])

# Show the plot
# plt.show()
# print(dir(digits))
# print(digits.data[0])
x_train,x_test,y_train,y_test = ts(digits.data,digits.target,test_size=0.25)
model = lg()
model.fit(x_train,y_train)
print(model.predict(digits.data[0:6]))
y_predict= (model.predict(x_test))
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predict)
print(cm)
import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()