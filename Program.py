def get_number(starting_number = float(input("What is the starting number? ")), r_value = float(input("What is the R value? ")), days = int(input("How many days? ")), infected = ""):
    for i in range(days+1):
        infected += str(starting_number * r_value ** i) + " "
    return infected

print(get_number())

print("This is my virus-exp-growth branch")

print("Hello")

#given the number of infected
#and given the r value
#and given the time-frame
#then calculate number of infected in the time-frame