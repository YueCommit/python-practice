#1
to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_values = to_be_changed.split("|")
print(changed_values)

#2
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.split('\n')
print(lyrics_split)

#3
changed_lyrics = lyrics.splitlines()
print(changed_lyrics)

#4
long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print(string_length)

#5
my_path = "   /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM    "
my_folder = my_path.strip()
print(my_folder)

#6
composers="Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
# Separate the composers
composers_split = composers.split(";")
# Get the third composer
third_composer = composers_split[2]
# Find the comma in the name
comma_position = third_composer.index(",")
# Use the slicing notation to get the last name
last_name = third_composer[:comma_position]
# Use the slicing notation to get the first name
first_name = third_composer[comma_position + 1:]
# Join the names to get the 3rd composer's name in "first last" format
third_composer_name = first_name + " " + last_name
# Print the composer's name
print(third_composer_name)

#7
left_padded = '                 Operators are standing by'
right_padded = 'Call now '
output = right_padded.rstrip() + '!'+ left_padded.lstrip()
print(output)