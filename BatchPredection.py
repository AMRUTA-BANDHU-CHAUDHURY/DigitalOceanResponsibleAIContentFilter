from detoxify import Detoxify

texts = [
    "You are amazing!",
    "You're a horrible person.",
    "I hope you have a great day!"
]

results = Detoxify('unbiased').predict(texts)

for i, text in enumerate(texts):
    print(f"\nText: {text}")
    for label in results:
        print(f"{label}: {results[label][i]:.4f}")
