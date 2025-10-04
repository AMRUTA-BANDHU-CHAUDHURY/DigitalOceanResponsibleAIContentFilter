We are using Detoxify library, which is a Python package built to detect toxicity in text using pretrained transformer models.

Detoxify provides an easy-to-use interface to detect toxic comments using models fine-tuned for this purpose (like original, unbiased, etc.).

# 1. Install Detoxify
First, install it using pip

pip install detoxify

# 2. Basic Usage (Code Examples)

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





# 3. Batch Predictions (Multiple Sentences)

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



# 4. dealing with non-English texts, use the multilingual model
                   model = Detoxify('multilingual')
                




