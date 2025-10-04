from detoxify import Detoxify

# Load the pre-trained model
model = Detoxify('original')  # options: 'original', 'unbiased', 'multilingual'

# Input text
text = "I hate you! You're the worst."

# Run toxicity detection
results = model.predict(text)

# Print results
print("Toxicity scores:")
for label, score in results.items():
    print(f"{label}: {score:.4f}")
