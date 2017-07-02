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
ttk.Label(main, text = "Misc").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Spelling", command = lambda: pyperclip.copy(r"Check the spelling on this. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Typo", command = lambda: pyperclip.copy(r"This looks like a typoe. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Capital", command = lambda: pyperclip.copy(r"Only the first words of sentences and proper nouns should be capitalized. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Meaning", command = lambda: pyperclip.copy(r"You may want to check the meaning of this. :)")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Conjugation
ttk.Label(main, text = "Conjugation").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Verb", command = lambda: pyperclip.copy(r"Check the conjugation on this verb. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Other", command = lambda: pyperclip.copy(r"What does this refer to? Is this the right form? :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Check the conjugation on your verbs to make sure they agree with your subjects. :) In particular, I recommend looking out for the differences between singular and plural subjects.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://conjugator.reverso.net/conjugation-english.html")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Articles
ttk.Label(main, text = "Articles").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "None", command = lambda: pyperclip.copy(r"This needs an article. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Wrong", command = lambda: pyperclip.copy(r"Try another article. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Be careful with articles in your writing. :) The article used on a noun (including the lack of an article) modifies the meaning of the noun. \nFor example, 'the' indicates a specific noun, whereas 'a' refers to one non-specific object. \nHere's a comprehensive guide to articles that includes examples. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://www.davidappleyard.com/english/articles.htm")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Abstract noun
ttk.Label(main, text = "Abstract").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Plural", command = lambda: pyperclip.copy(r"This is an abstract noun and should be plural. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Article", command = lambda: pyperclip.copy(r"This is an abstract noun, so it doesn't need an article. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Abstract nouns are nouns that refer to things in general. They're written in their plural forms without any articles.")).grid(column = 3, row = row, sticky = (W, E))

row += 1

#Prepositions
ttk.Label(main, text = "Prepositions").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "None", command = lambda: pyperclip.copy(r"This needs the preposition")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Wrong", command = lambda: pyperclip.copy(r"Try another preposition,")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Prepositions are words used to indicate the relationship between a verb and its object. Not including them or using an incorrect one changes the meaning of the sentence. :) \nFor example, \nI left for school. -> 'for' indicates a purpose.\nI left at three o'clock. -> 'at' (in this case) indicates a time.\nHere's a guide to some common prepositions that you may find helpful. I've also indicated a few examples in your writing. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://www.ego4u.com/en/cram-up/grammar/prepositions")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Plurals and possessives
ttk.Label(main, text = "Possessives").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Plural", command = lambda: pyperclip.copy(r"The apostrophe makes this possessive instead of plural. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Possessive", command = lambda: pyperclip.copy(r"This should be possessive. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Be careful with your plurals and your possessives. :) In general, adding an apostrophe indicates possession while excluding one indicates plurality. Here's a more thorough guide on the differences between the two.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://www.englishbaby.com/lessons/grammar/plural_vs_possessive_s")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Countable and uncountable nouns
ttk.Label(main, text = "Countable").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Plural", command = lambda: pyperclip.copy(r"This is an uncountable noun and can't be plural. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Incompatible", command = lambda: pyperclip.copy(r" is an uncountable noun, so this can't be used with it. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Some nouns are categorized as either countable or uncountable, and these have different grammar rules associated with them. :) For example, 'a' and some other words can't be used with uncountable nouns. Here's a guide that details the differences between the two.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://en.oxforddictionaries.com/grammar/countable-nouns")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Comma splice
ttk.Label(main, text = "Comma splice").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Text", command = lambda: pyperclip.copy(r"This is a comma splice. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Be careful with comma splicing. :) Comma splicing is when you take two sentences that are complete on their own and connect them with nothing but a comma. Instead, use a connecting word or write two separate sentences. :)\nFor example, \nI went to the beach, my family came along.\nThis should be either\nI went to the beach and my family came along.\nor\nI went to the beach. My family came along.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://grammar.ccc.commnet.edu/grammar/runons.htm")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Comma abuse
ttk.Label(main, text = "Comma abuse").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "S + V", command = lambda: pyperclip.copy(r"This comma is separating subject and verb.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Other", command = lambda: pyperclip.copy(r"This comma is in the middle of a clause.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Try not to put commas in the middle of clauses. :) For example, in this sentence \nThis, is an example.\nThe comma is separating the subject and the verb. Here's a guide that details other common comma errors that you may find helpful. :)")).grid(column = 3, row = row, sticky = (W, E))
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
ttk.Button(main, text = "Punctuation", command = lambda: pyperclip.copy(r"There's no need for any punctuation when the lead-in to a list is grammatically sound with the contents. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"When writing lists (including two-word lists), the parts of the sentence before and after it should both be sound with all of the list contents. This means that if you were to replace the list with any one of the list items, the sentence would still make sense grammatically and logically. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://www.gsbe.co.uk/grammar-lists.html")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Dialogue
ttk.Label(main, text = "Dialogue").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Comma", command = lambda: pyperclip.copy(r"There should be a comma here. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Dialogue embedded into text has its own special punctuation rules. For example, it's customary to put commas after tags like 'he said' and periods outside of the quotation marks. Here's a guide on punctuation and grammar used when dealing with dialogue. :)")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://www.thebalance.com/punctuating-dialogue-properly-in-fiction-writing-1277721")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Quotes
ttk.Label(main, text = "Quotes").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Period", command = lambda: pyperclip.copy(r"Quotations should only have a period outside the quotation marks and after the reference.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Be careful about punctuation around your quotes. :) Punctuation goes after the reference and outside the quotation. This way, the reference is part of the sentence instead of beginning the next sentence.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Label", command = lambda: pyperclip.copy(r"This is a quote standing on its own.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy('Quotations should have some of your own text accompanying them. For example, Einstein explains, "Light travels very fast".\nThe text accompanying the quote provides context for the information being presented.')).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Semicolon
ttk.Label(main, text = "Semicolon").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Comma", command = lambda: pyperclip.copy(r"I'd suggest using a comma instead. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Semicolons are used to connect two independent clauses (two full sentences). :) Use a comma instead for connecting dependent clauses (incomplete sentences) and list items.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://theoatmeal.com/comics/semicolon")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Hyphen
ttk.Label(main, text = "Hyphen").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Need", command = lambda: pyperclip.copy(r"Two-word adjectives need hyphens when they're ambiguous. :)")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Abuse", command = lambda: pyperclip.copy(r"Hyphens are used to create two-word adjectives. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Here's a guide on when to use hyphens with adjectives.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"http://www.quickanddirtytips.com/education/grammar/how-to-use-a-hyphen")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Incomplete sentences
ttk.Label(main, text = "Incomplete").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Subject", command = lambda: pyperclip.copy(r"This is missing a subject.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Verb", command = lambda: pyperclip.copy(r"This is missing a verb.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Giant noun", command = lambda: pyperclip.copy(r"The way this is written makes this a giant noun, and a sentence fragment.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy("Make sure your sentences are complete. A complete sentence has a subject, verb, and possibly an object, depending on the verb chosen. It's also possible to write something that ends up being a noun with a modifying clause, making it an incomplete sentence. For example,\nThe bunny that jumps very high.\nis a subject with a modifying clause. The verb is part of the modifying clause, meaning that the sentence is incomplete even though there is a verb in the sentence. To fix this, you would write,\nThe bunny jumps very high.")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Wrong forms
ttk.Label(main, text = "Form").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Noun", command = lambda: pyperclip.copy(r"This is a noun.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Verb", command = lambda: pyperclip.copy(r"This is a verb.")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Adjective", command = lambda: pyperclip.copy(r"This is an adjective.")).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy(r"Make sure you have the right forms of words (nouns, verbs, adjectives, etc.) Words in English can have multiple forms. For example, distinction is a noun, distinguish is a verb, and distinct and distinctive are adjectives. Use a dictionary to make sure you have the right form of a word. :)")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Formality
ttk.Label(main, text = "Formality").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Formal+", command = lambda: pyperclip.copy(r"Try a more formal equivalent of this, ")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "And/But", command = lambda: pyperclip.copy(r"You shouldn't start sentences with 'and or 'but'. Try the more formal equivalents, 'in addition' and 'however'. :)")).grid(column = 2, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy('Some of the words in your writing are a bit informal and can be replaced by more formal versions. For example, "" can be replaced by "". Here\'s a guide that has other formal versions of common words. :)')).grid(column = 3, row = row, sticky = (W, E))
ttk.Button(main, text = "Link", command = lambda: pyperclip.copy(r"https://depts.gpc.edu/gpcltc/handouts/communications/levelsofformality.pdf")).grid(column = 4, row = row, sticky = (W, E))

row += 1

#Passive and Active
ttk.Label(main, text = "Passive/Active").grid(column = 0, row = row, sticky = W)
ttk.Button(main, text = "Passive'd", command = lambda: pyperclip.copy(r"This makes the verb passive, which changes its meaning.")).grid(column = 1, row = row, sticky = (W, E))
ttk.Button(main, text = "Summary", command = lambda: pyperclip.copy('Be careful with active and passive forms of verbs. :) Getting them confused can turn subjects into objects and objects into subjects! For example, "I found" means that I am the one doing the finding, while "I was found" means that someone else found me. Here\'s a guide that details a bit more about active and passive forms. :)')).grid(column = 3, row = row, sticky = (W, E))
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