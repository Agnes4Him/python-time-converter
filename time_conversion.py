def to_seconds(hours, minutes, seconds):
    return hours*3600 + minutes*60 + seconds

print("Welcome to this time converter")
cont = "yes"
while(cont == "yes"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))
    print("The answer is {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to perform another conversion? [Yes to continue]")
print("Goodbye!")