def get_number(starting_number, r_value, days, infected = ""):
    for i in range(days+1):
        infected += str(starting_number * r_value ** i) + " "
    return infected

def get_r(starting_number, infected, days):
    return (infected/starting_number) ** (1/days)

print(get_r(float(input("What is the starting number? ")), int(input("What is the current number of infected? ")), int(input("How many days? "))))

print(get_number(float(input("What is the starting number? ")), float(input("What is the R value? ")), int(input("How many days? "))))

#given the number of infected
#and given the r value
#and given the time-frame
#then calculate number of infected in the time-frame