user_rating = input("What rating are you interested in?")

#open the file
with open("movie_info.txt") as movie_file:
#go through the file line by line
    for line in movie_file:
        #cleaning file
        clean_line = line.strip()
        #break it into lists
        split_line = clean_line.split(",")
        #get the title
        title = split_line[0]
        #get the rating
        rating = split_line[2]
        #get the year
        year = split_line[1]
        #print it out
        print(f"Title: {title} (Rated {rating})")

        