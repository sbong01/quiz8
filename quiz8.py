#7
dict ={
"apple":"red",
"berry":"blue"
}

a=dict.values()
print(a)

#5
dict = {
"Stephen King":"The Shining",
"Tolkien":"The Lord of the Rings",
"The Book Thief":"Zusak"
}

a=dict.keys()
print(a)

#8
import random
guess = int(input("Enter any number: "))
print(guess)

def random(guess):
    import random
    n = random.randint(1,10)
    if n == guess:
        print("Congratulations, you guessed the number!")
    else:
        print("Sorry, try again!")

random(guess)
