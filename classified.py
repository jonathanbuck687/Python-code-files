target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]
text = input("Classifier: ")
text = text.lower()
for i in target_words:
    if i in text:
        index = text.find(i)
        text = text[:index] + "[REDACTED]" + text[index + len(i):]
print(text[0:1].upper() + text[1:])