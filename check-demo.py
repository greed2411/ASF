# a validation set for testing out the multinomial naive Bayes model.

from sklearn.externals import joblib
nb2 = joblib.load('spam_data_pugaar.pkl')
test = ["pls dont call me anymore", 
        "fuck off",
        "unlimited sales this summer", 
        "fuck you slut",
        "cunt never cross me again",
        "water tap not working",
        "behenchod landlalala",
        "tube light broke",
        "fix cupboard lock",
        "almirah lock problem",
        "toilet cleaning",
        "pussy maintenance",
        "pussy maintanence",
        "ac smoke coming",
        "otha omale",
        "water cooler leaking",
        "",
        "cunt office",
        "cunt"
        ]
print(nb2.predict(test))