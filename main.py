# app/main.py

from dummy_model import DummyModel
from joblib import load



def classify_text(text, model):
    """Classify text as spam or not."""
    prediction = model.predict([text]) # it is pass in [] becasue string treat as iterable thing in python
    if prediction[0] == 1: #it gives output in list
        return "Spam"
    return "Not Spam"

if __name__ == "__main__": #__name__: It's a built-in variable in Python that represents the name of the current module.
    #If this code run directly main value will come in __name__ if imported then not come- so run this code when directly
    model = load('spam_model.joblib')

    sample_text = "Congratulations! You've won a $1000 gift card ! "
    print(f"Prediction for '{sample_text}': {classify_text(sample_text, model)}")