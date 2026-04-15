import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import pickle

# ✅ NO repetition — real data only
safe_texts = [
    "I love you", "You are a good guy", "This is amazing", "Great job",
    "Nice work", "Wonderful day", "You're awesome", "Good morning everyone!",
    "I appreciate your help", "Beautiful day today", "Thank you so much",
    "You are doing great work", "Love this community",
    "Congratulations on your success", "Keep up the good work",
    "Very helpful information", "Have a wonderful day",
    "Thanks for sharing", "Great job team", "Positive vibes only",
    "You rock!", "Excellent presentation", "Well done everyone",
    "I'm proud of you",

    # ✅ IMPORTANT contextual sentences
    "you are not bad",
    "this is not wrong",
    "i dont hate you",
    "you are fine",
    "its okay",
    "no problem",
    "everything is fine",
    "i like this",
    "this is good",
    "you did well"
]

toxic_texts = [
    "You are an idiot", "Shut up loser", "I hate you all",
    "Go kill yourself", "Stupid worthless person",
    "You're ugly and dumb", "Nobody likes you",
    "Die in a fire", "Fat loser", "Retarded moron",
    "Disgusting creep", "Pathetic weakling",
    "Burn in hell", "Rotten bastard",
    "annoying piece of shit", "Get a life freak",
    "Cringe failure", "Trash human being",

    # ✅ more variations
    "i really hate you",
    "you are so stupid",
    "you are completely useless",
    "you are garbage",
    "you are trash",
    "idiot person",
    "dumb human",
    "hate you so much"
]

# Create dataset
texts = safe_texts + toxic_texts
labels = [0]*len(safe_texts) + [1]*len(toxic_texts)

df = pd.DataFrame({"text": texts, "label": labels})

print("Dataset size:", len(df))

# ✅ FIXED vectorizer (NO stop_words)
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(df["text"])

# ✅ BETTER MODEL (SVM)
model = LinearSVC()

model.fit(X, df["label"])

# ✅ Test before saving
test_samples = [
    "I love you",
    "You are stupid",
    "Good morning",
    "you are not bad",
    "i hate exams"
]

print("\nTest Predictions:")
for t in test_samples:
    vec = vectorizer.transform([t])
    pred = model.predict(vec)[0]
    print(t, "→", "Toxic" if pred == 1 else "Not Toxic")

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("\n✅ Model trained & saved successfully!")