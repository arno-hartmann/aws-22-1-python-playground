counter = 2
number = 250

def is_prime_number(number):
    counter = 1
    for counter in range(2, number):
    #    print(counter)
        if (number % counter) == 0:
            return True

def write_to_file(var):
    with open('prime.txt','a') as file:
        file.write(str(var))
        file.write('\n')
#        file.write("hallo")


       
for counter in range (2,number):
    if not is_prime_number(counter):
        print("Nummber", counter,"ist eine Primzahl")
        write_to_file(counter)
    counter += 1
    