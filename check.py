from sklearn.externals import joblib
nb2 = joblib.load('spam_data.pkl')
test = ["pls dont call me anymore", "otha omale","unlimited sales this summer"]
print(nb2.predict(test))