def greet():
    print("hello")
    print("how are you doing")
    print("today")
greet()

def greet_with_name(name):
    print(f"hello {name}")
greet_with_name("kishore")

def greet_with_name_location(name, location):
    print(f"hello {name}, are you from {location}")
greet_with_name_location("kiran","bangarupalyam")

# using keyword arguments
greet_with_name_location(location="bangarupalyam1", name = "kishore2")