x = 5

x = "Example"

x = 4
y = 5
z = x * y

list_of_animals = ["Lion", "Tiger", "Polar Bear", "Weasel", "Rabbit"]
print(list_of_animals[1])

print(list_of_animals[-1])

print(list_of_animals[2:])

x = 4
if x > 3:
    print("x is greater than 3")
elif x == 3:
    print("x equals 3")
else:
    print("x is less than 3")


x = 4
y = "Nothing"
if x > 3 and y == "Nothing":
    print("Condition true")
else:
    print("Condition false")


list_of_animals = ["lion", "weasel", "tiger", "polar bear", "rabbit"]
if len(list_of_animals) > 4:
    print("Enough animals to start a zoo")
else:
    print("Not enough animals")


for x in range(10):
    if x % 2 == 0:
        print(x)


list_of_animals = ["lion", "weasel", "tiger", "polar bear", "rabbit"]
for animal in list_of_animals:
    print(animal)


def return_highest_number(first, second):
    if first > second:
        return first
    else:
        return second

x = return_highest_number(15, 500)
print(x)


list_of_animals = ["lion", "weasel", "tiger", "polar bear", "rabbit"]
list_of_animals.sort()
print(list_of_animals)


def words_in_text(list_of_words, text):
    matching_words = []
    for word in text.split(" "):
        if word.lower() in list_of_words:
            matching_words.append(word)
    return matching_words

list_of_animals = ["lion", "weasel", "tiger", "polar bear", "rabbit"]
story_text = "The weasel and the rabbit were the best of friends, they spent all their days together"
print(words_in_text(list_of_animals, story_text))