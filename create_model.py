from joblib import dump
from dummy_model import DummyModel



model = DummyModel()
# Save the model
dump(model, 'spam_model.joblib')
