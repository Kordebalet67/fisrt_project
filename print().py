import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

data = pd.DataFrame({
    "animal": ["cat", "cat", "dog", "dog", "cat", "dog"],
    "weight" :[1,1.5,50,90,5,30],
    "height" :[10,15,50,45,5,80],
    "label": ["home", "home", "service", "service", "home", "service"]
})
 
encoder = OneHotEncoder ()
x_encoded = encoder.fit_transform (data[["animal"]])

X = np.hstack([x_encoded.toarray(), data[["weight", "height"]].values])

y = data["label"]
new = encoder.transform([["dog"]]).toarray()

tree = DecisionTreeClassifier(max_depth=6).fit(X,y)
new_data = np.hstack([new, [[ 2, 5]]])
print(f"Decision tree : {tree.predict(new_data)} \n")

knn  = KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)
print(f"Kneighboors : {knn.predict(new_data)}")
