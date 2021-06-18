chosen_year = input("Enter the year of interest: ")
greatest = 0
greatest_country = "nonexist"
smallest = 10000
smallest_country = "nonexist"
chosen_greatest = 0
chosen_greatest_country = "nonexist"
chosen_smallest = 100000
chosen_smallest_country = "nonexist"
total = 0
#open file
with open("life-expectancy.csv") as data:
    #skip header
    header = data.readline()
    #iterate through list
    for line in data:
        #clean and split
        clean_line = line.strip()
        split_line = clean_line.split(",")

        #different lists
        country = split_line[0]
        country_code = split_line[1]
        year = split_line[2]
        life_expectancy = float(split_line[3])
        #variable creation
        if life_expectancy > greatest:
            greatest = life_expectancy
            greatest_country = country
            greatest_year = year
    
        if life_expectancy < smallest:
            smallest = life_expectancy
            smallest_country = country
            smallest_year = year

        if year == chosen_year:
            if life_expectancy > chosen_greatest:
                chosen_greatest = life_expectancy
                chosen_greatest_country = country
            if life_expectancy < chosen_smallest:
                chosen_smallest = life_expectancy
                chosen_smallest_country = country
            
            

print("")
print("For every year in the database:")
print(f"The greatest life expectancy is {greatest:.2f} from {greatest_country} in {greatest_year}")
print(f"The smallest life expectancy is {smallest:.2f} from {smallest_country} in {smallest_year}")
print("")
print(f"For the year {chosen_year}:")
print(f"The max life expectancy was in {chosen_greatest_country} with {chosen_greatest}")
print(f"The min life expectancy was in {chosen_smallest_country} with {chosen_smallest}")



