astring = "Hello world!"
print(astring.index("o"))
print(astring.count("l"))
print(astring[2:7])
print(astring[3:7:3])

# is same [start:stop:step] steps is skipped
print(astring[3:7])
print(astring[3:7:1])

# There is no function like strrev in C to reverse a string.
print(astring[::-1])

print(astring.upper())
print(astring.lower())

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print(afewwords)