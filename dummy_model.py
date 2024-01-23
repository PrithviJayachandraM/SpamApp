class DummyModel:
    def predict(self, texts):
        return [1 if "won" in text or "gift" in text else 0 for text in texts]
        #IF won and gift present in text then it is spam (1) otherewise no spam(0)
