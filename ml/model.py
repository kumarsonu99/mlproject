import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Large training dataset
data = {
    "text": [
        # Safe (0)
        "I love you", "You are a good guy", "This is amazing", "Great job", "Nice work", 
        "Wonderful day", "You're awesome", "Good morning everyone!", "I appreciate your help",
        "Beautiful day today", "Thank you so much", "You are doing great work", "Love this community",
        "Congratulations on your success", "Keep up the good work", "This is amazing content",
        "Very helpful information", "Have a wonderful day", "Thanks for sharing", "Great job team",
        "Positive vibes only", "You rock!", "Excellent presentation", "Well done everyone", "I'm proud of you",
        
        # Toxic (1) 
        "You are an idiot", "Shut up loser", "I hate you all", "Go kill yourself", "Stupid worthless person",
        "You're ugly and dumb", "Nobody likes you", "Die in a fire", "Fat loser", "Retarded moron",
        "You're terrible", "Disgusting creep", "Pathetic weakling", "Cancer patient", "Burn in hell",
        "Rotten bastard", "Annoying piece of shit", "Get a life freak", "Cringe failure", "Trash human being"
    ],
    "label": [0]*25 + [1]*22
}

df = pd.DataFrame(data)

# Convert text → numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

# Train model
model = LogisticRegression()
model.fit(X, df["label"])

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved!")
