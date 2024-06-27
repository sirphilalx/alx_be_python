# Mad Libs Python Script

# Prompts for user inputs
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
place = input("Enter a place: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")
adjective3 = input("Enter one more adjective: ")
verb3 = input("Enter another verb: ")
adverb = input("Enter an adverb: ")

# Mad Libs story
story = f"""
Once upon a time in a {adjective1} land, there was a {noun1} who loved to {verb1}.
Every day, the {noun1} would {verb1} around the {place}, making everyone {adjective2}.
One day, a {adjective3} {noun2} appeared and {verb2} everything!
In the end, everyone learned to {verb3} and lived {adverb} ever after.
"""

# Print the completed story
print(story)
