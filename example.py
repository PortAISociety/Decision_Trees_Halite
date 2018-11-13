from sklearn import tree
import graphviz

data = [1,2,3]
labels = ["a","b","c"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data, labels)

clf.predict("d")

#dot_data = tree.export_graphviz(clf, out_file="numbers.dot",
#                filled=True, rounded=True, special_characters=True)
