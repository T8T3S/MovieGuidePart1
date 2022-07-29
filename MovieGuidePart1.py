list_of_movies = ['Monty Python and the Holy Grail', 'On the Waterfront', 'Cat on a Hot Tin Roof']

def print_intro():
    print('The Movie List program')
    print('\nCOMMAND MENU')
    print('list - List all movies')
    print('add  - Add a movie')
    print('del  - Delete a movie')
    print('exit - Exit program')

def list_all_movies():
    for m in list_of_movies:
        print(f'{list_of_movies.index(m) + 1}. {m}')

def add_movie(movie_name):
    list_of_movies.append(movie_name)
    print(f'{movie_name} was added.')

def delete_movie(which_movie):
    print(f'{list_of_movies[which_movie]} was deleted.')
    list_of_movies.pop(which_movie)

def exit_program():
    print('Bye!')
    exit()
print_intro()
while True:
    command = input('\nCommand: ')
    if command == 'list':
        list_all_movies()
    elif command == 'add':
        movie_name = input('Name: ')
        add_movie(movie_name)
    elif command == 'del':
        which_movie = int(input('Number: '))
        if which_movie > len(list_of_movies):
            print('Invalid movie number.')
        elif which_movie < 0:
            print('Invalid movie number.')
        else:
            delete_movie(which_movie - 1)
    elif command == 'exit':
        exit_program()
    else:
        print('Not a valid command. Please try again.')