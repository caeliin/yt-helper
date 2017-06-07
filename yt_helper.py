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
#Conjugation
ttk.Label(main, text = "Conjugation").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Verb", command = lambda: pyperclip.copy(r"Check the conjugation on this verb.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Other", command = lambda: pyperclip.copy(r"What does this refer to? Is this the right form?")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Check the conjugation on your verbs. Make sure you know what the subject is before you write a verb. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://conjugator.reverso.net/conjugation-english.html")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Articles
ttk.Label(main, text = "Articles").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "None", command = lambda: pyperclip.copy(r"This needs an article.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Wrong", command = lambda: pyperclip.copy(r"Try another article.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Check your nouns to make sure their articles are correct. :) I've highlighted a number of examples of these for you.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://www.davidappleyard.com/english/articles.htm")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Abstract noun
ttk.Label(main, text = "Abstract").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Plural", command = lambda: pyperclip.copy(r"This is an abstract noun and should be plural. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Article", command = lambda: pyperclip.copy(r"This is an abstract noun, so it doesn't need an article.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Abstract nouns are nouns that refer to things in general. They're written in their plural forms without any articles.")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Prepositions
ttk.Label(main, text = "Prepositions").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "None", command = lambda: pyperclip.copy(r"This needs a preposition.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Wrong", command = lambda: pyperclip.copy(r"Try another preposition. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Here's a guide to prepositions. Because of the nature of the English language, this obviously isn't complete, but you can use Google to figure out what prepositions specific verbs take. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://www.ego4u.com/en/cram-up/grammar/prepositions")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Plurals and possessives
ttk.Label(main, text = "Possessives").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Plural", command = lambda: pyperclip.copy(r"The apostrophe makes this possessive instead of plural.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Possessive", command = lambda: pyperclip.copy(r"This should be possessive.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Be careful with your plurals and your possessives. :) Here's a guide on the grammar differences between the two.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://www.englishbaby.com/lessons/grammar/plural_vs_possessive_s")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Countable and uncountable nouns
ttk.Label(main, text = "Countable").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Plural", command = lambda: pyperclip.copy(r"This was originally an uncountable noun, but changing it to plural forces it to the countable version. This changes the meaning of the word.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Incompatible", command = lambda: pyperclip.copy(r"This can't be used with uncountable nouns.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Some nouns are categorized as either countable or uncountable, and these have different grammar rules associated with them. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://en.oxforddictionaries.com/grammar/countable-nouns")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Comma splice
ttk.Label(main, text = "Comma splice").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Text", command = lambda: pyperclip.copy(r"This is a comma splice.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Watch out for comma splicing when you write. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://grammar.ccc.commnet.edu/grammar/runons.htm")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Comma abuse
ttk.Label(main, text = "Comma abuse").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "S + V", command = lambda: pyperclip.copy(r"This comma is separating subject and verb.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Other", command = lambda: pyperclip.copy(r"This comma is in the middle of a clause.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Try not to put commas in the middle of clauses. :) Here's a guide detailing common comma errors.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://owl.english.purdue.edu/owl/owlprint/607/")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Needs a comma
ttk.Label(main, text = "Add comma").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Ambiguity", command = lambda: pyperclip.copy(r"Add a comma here to remove ambiguity. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Modifying", command = lambda: pyperclip.copy(r"Modifying clauses should be surrounded by commas on both sides.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Here's a pretty comprehensive guide on when to use commas. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://www.grammarbook.com/punctuation/commas.asp")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Lists
ttk.Label(main, text = "Lists").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Consistency", command = lambda: pyperclip.copy(r"Items in a list should all be grammatically sound with the lead-in.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Punctuation", command = lambda: pyperclip.copy(r"There's no need for any punctuation when the lead-in to a list is grammatically sound with the contents.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Here's a guide to grammar around lists. Take a look at the section starting with 'Each listed item also needs to begin in a way that is grammatically compatible with the introductory phrase or clause'. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://www.gsbe.co.uk/grammar-lists.html")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Dialogue
ttk.Label(main, text = "Dialogue").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Comma", command = lambda: pyperclip.copy(r"There should be a comma here. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Here's a guide on punctuation and grammar used when dealing with dialogue. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://www.thebalance.com/punctuating-dialogue-properly-in-fiction-writing-1277721")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Quotes
ttk.Label(main, text = "Quotes").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Period", command = lambda: pyperclip.copy(r"Quotations should only have one period, outside the quotation marks and after the reference.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Be careful about punctuation around your quotes. :) Punctuation goes after the reference and outside the quotation marks so that the entire sentence is ended and the reference is part of the sentence instead of beginning the next sentence.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Label", command = lambda: pyperclip.copy(r'Quotations should have some of your own text accompanying them. e.g. Einstein explains, "Light travels very fast".')).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Make sure you're explaining and contextualizing your quotes. :) A quote without an explanation is like a vase in a museum without a label or plaque.")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Semicolon
ttk.Label(main, text = "Semicolon").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Text", command = lambda: pyperclip.copy(r"Semicolons are used to connect two independent clauses.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Here's a fun guide on how to use semicolons, if you're interested. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://theoatmeal.com/comics/semicolon")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Hyphen
ttk.Label(main, text = "Hyphen").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Text", command = lambda: pyperclip.copy(r"Two-word adjectives need hyphens when they're ambiguous. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Here's a guide on when to use hyphens with adjectives.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://www.quickanddirtytips.com/education/grammar/how-to-use-a-hyphen")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Incomplete sentences
ttk.Label(main, text = "Incomplete").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Subject", command = lambda: pyperclip.copy(r"This is missing a subject.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Verb", command = lambda: pyperclip.copy(r"This is missing a verb.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Giant noun", command = lambda: pyperclip.copy(r"The way this is written makes this a giant noun, and a sentence fragment.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Make sure your sentences are complete. A complete sentence has a subject, verb, and possibly an object, depending on the verb chosen. It's also possible to write something that ends up being a noun with a modifying clause, making it an incomplete sentence.")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Wrong forms
ttk.Label(main, text = "Form").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Noun", command = lambda: pyperclip.copy(r"This is a noun.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Verb", command = lambda: pyperclip.copy(r"This is a verb.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Adjective", command = lambda: pyperclip.copy(r"This is an adjective.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Make sure you have the right forms of words (nouns, verbs, adjectives, etc.) Words in English can have multiple forms. Use Google to make sure you have the right form of a word. :)")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Formality
ttk.Label(main, text = "Formality").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Formal+", command = lambda: pyperclip.copy(r"Try a more formal equivalent of this, ")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "And/But", command = lambda: pyperclip.copy(r"You shouldn't start sentences with 'and or 'but'. Try the more formal equivalents, 'in addition' and 'however'. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Here's a guide on more formal versions of common phrases. This isn't complete, though, so Google any specific words that you'd like a more formal version of. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://depts.gpc.edu/gpcltc/handouts/communications/levelsofformality.pdf")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Passive and Active
ttk.Label(main, text = "Passive/Active").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Passive'd", command = lambda: pyperclip.copy(r"This makes the verb passive, which changes its meaning.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Be careful with active and passive forms of verbs. :) Getting them confused can turn subjects into objects and objects into subjects!")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://en.oxforddictionaries.com/grammar/active-and-passive-verbs")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Passive voice
ttk.Label(main, text = "Passive voice").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Text", command = lambda: pyperclip.copy(r"This is written in passive voice.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Writing in passive voice makes your sentences longer and possibly harder to understand. Try to avoid it in formal writing when you can. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://writingcenter.unc.edu/handouts/passive-voice/")).grid(column = 4, row = row, sticky = (W, E))


for child in main.winfo_children():
    child.grid_configure(padx = 0, pady = 2)

root.mainloop()