from tkinter import *
from tkinter import ttk
import pyperclip

#ttk.Button(main, text = "", command = lambda: pyperclip.copy(r"")).grid(column = , row = row, sticky = (W, E))

#ttk.Label(main, text = "").grid(column = 0, row = row, sticky = W)
#ttk.Button(main, text = "Text", command = lambda: pyperclip.copy(r"")).grid(column = 1, row = row, sticky = (W, E))
#ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"")).grid(column = 3, row = row, sticky = (W, E))
#ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"")).grid(column = 4, row = row, sticky = (W, E))


root = Tk()
root.title("YourTutor Helper")
root.wm_attributes("-topmost", 1)

main = ttk.Frame(root, padding = "1")
main.grid(column = 0, row = 0, sticky=(N, W, E, S))

row = 0

#Misc

ttk.Button(main, text = "Spelling", command = lambda: pyperclip.copy("Check the spelling on this. :)")).grid(column = 0, row = row, sticky = (W, E))
ttk.Button(main, text = "Typo", command = lambda: pyperclip.copy("This looks like a typo. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Capital", command = lambda: pyperclip.copy("Only the first words of sentences and proper nouns should be capitalized. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Meaning", command = lambda: pyperclip.copy("You may want to check the meaning of this. :)")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Misc 2
ttk.Button(main, text = "Conjugation", command = lambda: pyperclip.copy("Check the conjugation on this verb. :)")).grid(column = 0, row = row, sticky = (W, E))
ttk.Button(main, text = "Modifying", command = lambda: pyperclip.copy("Modifying clauses should be surrounded by commas on both sides.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Semicolon", command = lambda: pyperclip.copy("Semicolons are used to connect two independent clauses (full sentences). :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Impact", command = lambda: pyperclip.copy("\"Impact\" only needs to be followed by \"on\" when used as a noun.\ne.g. Recycling impacts the environment.\nRecycling has an impact on the environment.")).grid(column = 3, row = row, sticky = (W, E))


row += 1

#Misc 3

ttk.Button(main, text = "O + S", command = lambda: pyperclip.copy("This is acting as both an object and a subject, which isn't allowed.")).grid(column = 0, row = row, sticky = (W, E))
ttk.Button(main, text = "A/Effect", command = lambda: pyperclip.copy("affect -> verb\neffect -> noun")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "I. start", command = lambda: pyperclip.copy("This is informal when used to start a sentence. :) Move it inside the sentence for an easy fix.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "2 Clauses", command = lambda: pyperclip.copy("This expects two clauses.\ne.g. ")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Articles
ttk.Label(main, text = "Articles").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "None", command = lambda: pyperclip.copy(r"This needs an article. :) (hint: )")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Be careful with articles in your writing. :) The article used on a noun (including the lack of an article) modifies the meaning of the noun. \nFor example, 'the' indicates a specific noun, whereas 'a' refers to one non-specific object. \nHere's a comprehensive guide to articles that includes examples. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://www.davidappleyard.com/english/articles.htm")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Abstract noun
ttk.Label(main, text = "Abstract").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Plural", command = lambda: pyperclip.copy(r"This is an abstract noun and should be plural. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Article", command = lambda: pyperclip.copy(r"This is an abstract noun, so it doesn't need an article. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Abstract nouns are nouns that refer to things in general. They're written in their plural forms without any articles.")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#possessives
ttk.Label(main, text = "Possessives").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Possessive", command = lambda: pyperclip.copy(r"This should be possessive. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("When one noun belongs to another, use an apostrophe to indicate the possession. For example, in ")).grid(column = 2, row = row, sticky = (W, E))


row += 1

#plurals
ttk.Label(main, text = "Plurals").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Plural", command = lambda: pyperclip.copy(r"The apostrophe makes this possessive instead of plural. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Be careful not to use apostrophes with plural nouns. Apostrophes are used to indicate possession. :)")).grid(column = 2, row = row, sticky = (W, E))

row += 1

#Countable and uncountable nouns
ttk.Label(main, text = "Countable").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Plural", command = lambda: pyperclip.copy(r"This is an uncountable noun and can't be plural. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Some nouns are categorized as either countable or uncountable, and these have different grammar rules associated with them. :) For example, 'a' and some other words can't be used with uncountable nouns. Here's a guide that details the differences between the two.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://en.oxforddictionaries.com/grammar/countable-nouns")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Comma splice
ttk.Label(main, text = "Comma splice").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Splice", command = lambda: pyperclip.copy(r"This is a comma splice. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Be careful with comma splicing. :) Comma splicing is when you take two sentences that are complete on their own and connect them with nothing but a comma. Instead, use a connecting word or write two separate sentences. :)\nFor example, \nI went to the beach, my family came along.\nThis should be either\nI went to the beach and my family came along.\nor\nI went to the beach. My family came along.")).grid(column = 2, row = row, sticky = (W, E))

row += 1

#Comma abuse
ttk.Label(main, text = "Comma abuse").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "S + V", command = lambda: pyperclip.copy(r"This comma is separating subject and verb.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Try not to put commas in the middle of clauses. :) For example, in this sentence \nThis, is an example.\nThe comma is separating the subject and the verb.")).grid(column = 2, row = row, sticky = (W, E))

row += 1

#Lists
ttk.Label(main, text = "Lists").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Consistency", command = lambda: pyperclip.copy(r"Items in a list should all be grammatically sound with the lead-in.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Punctuation", command = lambda: pyperclip.copy(r"There's no need for any punctuation when the lead-in to a list is grammatically sound with the contents. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"When writing lists (including two-item lists), the parts of the sentence before and after it should both be sound with all of the list contents. This means that if you were to replace the list with any one of the list items, the sentence would still make sense grammatically and logically. :)")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Dialogue
ttk.Label(main, text = "Dialogue").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Comma", command = lambda: pyperclip.copy(r"There should be a comma here. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Dialogue embedded into text has its own special punctuation rules. For example, it's customary to put commas after tags like 'he said' and periods outside of the quotation marks. Here's a guide on punctuation and grammar used when dealing with dialogue. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://www.thebalance.com/punctuating-dialogue-properly-in-fiction-writing-1277721")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Quotes
ttk.Button(main, text = "Period", command = lambda: pyperclip.copy(r"Quotations should only have a period outside the quotation marks and after the reference.")).grid(column = 0, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Be careful about punctuation around your quotes. :) Punctuation goes after the reference and outside the quotation. This way, the reference is part of the sentence instead of beginning the next sentence.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Label", command = lambda: pyperclip.copy(r"This is a quote standing on its own.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy('Quotations should have some of your own text accompanying them. For example, Einstein explains, "Light travels very fast".\nThe text accompanying the quote provides context for the information being presented.')).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Incomplete sentences
ttk.Label(main, text = "Incomplete").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Subject", command = lambda: pyperclip.copy(r"This is missing a subject.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Verb", command = lambda: pyperclip.copy(r"This is missing a verb.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Make sure your sentences are complete. A complete sentence has a subject, which is what the sentence is about, and a predicate, which describes what the subject does or what happens to the subject. A sentence missing either of these is incomplete. :)")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Wrong forms
ttk.Button(main, text = "Noun", command = lambda: pyperclip.copy(r"This is a noun.")).grid(column = 0, row = row, sticky = (W, E))
ttk.Button(main, text = "Verb", command = lambda: pyperclip.copy(r"This is a verb.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Adjective", command = lambda: pyperclip.copy(r"This is an adjective.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Make sure you have the right forms of words (nouns, verbs, adjectives, etc.) Words in English can have multiple forms. For example, distinction is a noun, distinguish is a verb, and distinct and distinctive are adjectives. Use a dictionary to make sure you have the right form of a word. :)")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Formality
ttk.Button(main, text = "And", command = lambda: pyperclip.copy(r"Sentences shouldn't start with 'and'. :)")).grid(column = 0, row = row, sticky = (W, E))
ttk.Button(main, text = "But", command = lambda: pyperclip.copy(r"Sentences shouldn't start with 'but'. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy('Some of the words in your writing are a bit informal and can be replaced by more formal versions. For example, "" can be replaced by "". Here\'s a guide that has other formal versions of common words. :)')).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://depts.gpc.edu/gpcltc/handouts/communications/levelsofformality.pdf")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Passive and Active
ttk.Label(main, text = "Passive/Active").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "A -> P", command = lambda: pyperclip.copy(r"This makes the verb passive, which changes its meaning.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy('Be careful with active and passive forms of verbs. :) Getting them confused can turn subjects into objects and objects into subjects! For example, "I found" means that I am the one doing the finding, while "I was found" means that someone else found me. Here\'s a guide that details a bit more about active and passive forms.')).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://en.oxforddictionaries.com/grammar/active-and-passive-verbs")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Passive voice
ttk.Label(main, text = "Passive voice").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Passive", command = lambda: pyperclip.copy(r"This is written in passive voice.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Writing in passive voice makes your sentences longer and possibly harder to understand. Try to avoid it in formal writing when you can. :)")).grid(column = 2, row = row, sticky = (W, E))


for child in main.winfo_children():
    child.grid_configure(padx = 0, pady = 2)

root.mainloop()