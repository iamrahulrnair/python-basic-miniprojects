play=True
while play:
    adjective1=input('input an adjective: ')
    adjective2=input('input an adjective: ')
    type_of_bird=input('input a type of word: ')
    room_in_house=input('name a room in a house: ')
    verb1=input('input a verb')
    relative_name=input("input a relative's name: ")
    noun1=input('input a noun: ')
    liquid=input('name a liquid: ')
    verb2=input('name a verb ending with -ing: ')
    body_part=input('name part of the body which is plural: ')
    plural1=input('input a plural noun: ')
    verb3=input('input a verb ending with -ing: ')
    noun2=input('input a noun: ')
    print(f"\n\nIt was a {adjective1}, cold November day. I\nwoke up to the {adjective2} smell of {type_of_bird}\nroasting in the {room_in_house} downstairs. I\n{verb1} down the stairs to see if i could\nhelp {verb2} the dinner. My mom said,\n\"see if {relative_name} needs a fresh {noun1}.\"So i\ncarried a tray of glasses full of {liquid} into\n the {verb2} room. When I got there, I\ncouldn't believe my {body_part}! There were {plural1} {verb3} on the {noun2}\n\n")
    
    _choice=input("\n\t\tWant to play again? press any character else press n/N or press Q/q to quit: \n\n")
    if _choice.lower()=='n':
        play=False
    elif _choice.lower()=='q':
        break
print("Thanks for playing.")