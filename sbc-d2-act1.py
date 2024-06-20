word = "summer bootcamp"

print(word.title())
print(word.capitalize().replace("p", "P"))
print(word[7:11].capitalize().replace("B", "L"))
print(word[11:15].replace("p", "E"))
print(f"{word[-3].capitalize()}{word[5].capitalize()}")
print(word.replace(" ", "").isalpha())
