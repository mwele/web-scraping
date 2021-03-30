from collections import namedtuple
Book=namedtuple("Book","Author title genre")
books=[
Book("Pratchett","Nightwatch","fantasy"),
Book("Pratchett","Thief of Time","fantasy"),
Book("Le Guin","The Dispossesed","Scifi"),
Book("Le Guin","A Wizard Of Earthsea","fantasy"),
Book("Turner","The Thief","fantasy"),
Book("Philips","Preston Diamond","Western"),
Book("Philips","Twice Upon A Time","Scifi"),


]
fantasy_authors={
	b.Author for b in books if b.genre == 'fantasy'
}
print(fantasy_authors)
fantasy_authors_list=[
b.Author for b in books if b.genre == 'fantasy'
]
print(fantasy_authors_list)

fantasy_authors_dict ={
	
	b.Author: b for b in books if b.genre == 'fantasy'
}
print(fantasy_authors_dict)