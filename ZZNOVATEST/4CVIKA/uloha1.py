# Úloha 1
from collections import Counter

# Načtení souboru
with open("lorem_ipsum.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Rozdělení na slova
words = text.split()

# Počet slov
word_count = len(words)

# Počet unikátních slov
unique_words = len(set(words))
# Počet unikátních slov
unique_words = set(words)
unique_word_count = len(unique_words)

# Průměrná délka slova
average_word_length = sum(map(len, words)) / word_count

# Nejčastější slovo
most_common_word = Counter(words).most_common(1)[0]

# Výpis výsledků
print(f"Počet slov: {word_count}")
print(f"Počet unikátních slov: {unique_words}")
print(f"Průměrná délka slova: {average_word_length:.2f}")
print(f"Nejčastější slovo: {most_common_word[0]} ({most_common_word[1]}x)")
