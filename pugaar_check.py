from sklearn.externals import joblib
nb2 = joblib.load('spam_data_pugaar.pkl')

def check(description):
    
    try:

        value = nb2.predict([description])

        if value[0] == 1:
            return True
        elif value[0] == 0:
            return False
        else:
            return 'error occured.'
    
    except Exception as e:

        return False