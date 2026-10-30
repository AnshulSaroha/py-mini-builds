#story generator
#Ask user for some words and then present them a story
print("Welcome to Story Generator! Give me a few words and I'll write you a story.") 
print()#blank line for readability

#collect input from user
adjective = input("Give me an adjective (a describing word, like 'smelly'): ") 
animal = input("Give me an animal (like buffalo): " )
place = input("Give me a place (like Chandni Chowk): " )
verb = input("Give me a verb ending in -ing (like 'dancing'): ") 
adverb = input("Give me an adverb (a word ending in -ly, like 'badly'): ") 
food = input("Give me a food (like samosa): ")

#building story using f-strings 
story = (f'''
Here is your story: 

Yesterday, I was walking near {place} when I suddenly saw 
a {adjective} {animal}. It was {verb} very {adverb} 
and eating {food} at the same time. I have never seen anything 
like it in my life. I don't think anyone will believe me.''')

#print the final story
print(story.upper())