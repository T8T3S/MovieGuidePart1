list_of_movies = ['Monty Python and the Holy Grail','On the Waterfront','Cat on a Hot Tin Roof']
def print_intro():
    print('The Movie List program')
    print('\nCOMMAND MENU')
    print('list - List all movies')
    print('add  - Add a movie')
    print('del  - Delete a movie')
    print('exit - Exit program')

def list_all_movies():
    for index, m in enumerate(list_of_movies, start=1):
        print(f'{index}. {m}')

def add_movie(movie_name):
    list_of_movies.append(movie_name)
    print(f'{movie_name} was added.')

def delete_movie(which_movie):
    movie = list_of_movies.pop(which_movie-1)
    print(f'{movie} was deleted.')

def exit_program():
    print('Bye!')
    exit()
print_intro()
while True:
    command = input('\nCommand: ')
    if command.lower() == 'list':
        list_all_movies()
    elif command.lower() == 'add':
        movie_name = input('Name: ')
        add_movie(movie_name)
    elif command.lower() == 'del':
        which_movie = int(input('Number: '))
        if which_movie > len(list_of_movies) or which_movie < 0:
            print('Invalid movie number.')
        else:
            delete_movie(which_movie)
    elif command == 'exit':
        exit_program()
    else:
        print('Not a valid command. Please try again.')