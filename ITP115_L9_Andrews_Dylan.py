# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Lab 8

# reads file, creates list of show based on genre user inputted
def read_file(user_genre, file_name = "shows.csv"):
    fileIn = open("shows.csv", "r")
    genres = []
    showsInGenre = []
    shows = []
    i = 0
    for line in fileIn:
        newLine = line.strip().split(",")
        genres.append(newLine[1])
        shows.append(newLine[0])
    while i < len(genres):
        if user_genre == genres[i]:
            showsInGenre.append(shows[i])
        i += 1
    fileIn.close()

    return showsInGenre


# writes a new file of all the shows in the selected genre
def write_file(genre, show_list):

    fileOut = open(genre + ".txt", "a")
    i = 0
    while i < len(show_list):
        print(show_list[i], file=fileOut)
        i += 1
    fileOut.close()

# prompts user to enter genre, and sends information to functions to read and write the necessary files
def main():


    print("TV Show\nPossible genres are action & adventure, animation, comedy, "
          "documentary, drama, mystery & suspense, science fiction & fantasy")
    genre = (input("Enter a genre: "))
    newGenre = genre.lower().strip()
    while (newGenre != "action & adventure" and newGenre != "animation" and newGenre != "comedy" and newGenre !=
           "documentary" and newGenre != "drama" and newGenre != "mystery & suspense" and newGenre !=
           "science fiction & fantasy"):
        genre = (input("Enter a genre: "))
        newGenre = genre.lower().strip()
    showsInGenre = read_file(newGenre)
    write_file(newGenre, showsInGenre)
    print("The file '" + newGenre + ".txt' has the following shows:")
    print(showsInGenre)



main()