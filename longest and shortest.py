data = ("package", "age", "public", "army", "number", "island", "build", "reading", "smell", "direction")

longest_word = max(data, key=len)
shortest_word = min(data, key=len)

print(f"The longest word is: {longest_word}")
print(f"The shortest word is: {shortest_word}")