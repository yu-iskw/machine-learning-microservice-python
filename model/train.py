from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib

# load iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# train model
clf = svm.LinearSVC()
clf.fit(X, y)

# persistent model
joblib.dump(clf, 'iris_model.pickle')

# test code to check the saved model
#clf = joblib.load('iris_model.pickle')
#result = clf.predict([[ 5.0,  3.6,  1.3,  0.25]])
#print(result)
