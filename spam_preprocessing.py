import pandas as pd
st = pd.read_table('sms.tsv', header=None, names=['label', 'message'])
# st referring to spam_table
# print(st.head())
# print(st.shape)
# print(st.label.value_counts)
"""
About the dataset :

Observations(m) : 5572

label
ham     4825
spam     747
"""
# convert label to a numerical variable
st['label_num'] = st.label.map({'ham':0, 'spam':1})
#print(st.head(10))

# initializing feature matrix 'X' and response vector 'y'
X = st.message
y = st.label_num
# print(X.shape, y.shape) (5572,) for both

# for splitting the dataset into training and testing
# testing dataset is of 25% of original dataset.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# import and instantiate CountVectorizer (with the default parameters)
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()

# combine fit and transform into a single step, slightly faster
X_train_dtm = vect.fit_transform(X_train)
# print(type(X_train_dtm))

X_test_dtm = vect.transform(X_test)

# Follow IIFP - Import, Instantiate, Fit, Predict
# import and instantiate a Multinomial Naive Bayes model
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train_dtm, y_train)
# make class predictions for X_test_dtm
y_pred_class = nb.predict(X_test_dtm)

# calculate accuracy of class predictions
from sklearn import metrics
print('\nTesting accuracy of Naive Bayes model is', metrics.accuracy_score(y_test, y_pred_class))
print('\nConfusion matrix\n', metrics.confusion_matrix(y_test, y_pred_class))

# Now fitting with entire dataset instead of X_train
# X_dtm = vect.fit_transform(X)
# nb2 = MultinomialNB()
# nb2.fit(X_dtm, y)
print('pickling ...')

from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer()),
                      ('nb2', MultinomialNB())])
text_clf = text_clf.fit(X, y)
# joblib is more efficient at handling numpy arrays than python pickler.
from sklearn.externals import joblib
_ = joblib.dump(text_clf, 'spam_data.pkl', compress = 9)
print('Done pickling...')


# test = ["lifetime unlimited offer."]
# # transform testing data into a document-term matrix (using existing vocabulary)
# simple_test_dtm = vect.transform(test)
# simple_test_dtm = simple_test_dtm.toarray()
# print(nb2.predict(simple_test_dtm))

# print('reloading...')
# clf = joblib.load('spam_data.pkl')
# print(clf)