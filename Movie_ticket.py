print("Welcome to the Movie Ticketing System!\nHere are the available tickets:")

tickets = {
    "comedy": [{"title": "Hot Fuzz", "price": 9.99},
               {"title": "Airplane!", "price": 8.99}],
    "romcom": [{"title": "When Harry Met Sally", "price": 10.99},
               {"title": "Sleepless in Seattle", "price": 9.49}],
    "action": [{"title": "John Wick", "price": 12.99},
               {"title": "Pacific Rim", "price": 11.49}],
    "sci-fi": [{"title": "Jurassic Park", "price": 14.99},
               {"title": "Blade Runner", "price": 13.49}],
}
# Defining functions
def print_tickets():
    for genre, movies in tickets.items():
        for movie in movies:
            print(f"{genre.capitalize()}: {movie['title']} - ${movie['price']:.2f}")

print_tickets()