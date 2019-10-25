# Matthew Chan (PM), Hannah Fried, Coby Sontag, Jionghao Wu [Team SOS]
# SoftDev1 pd2
# P00 -- Da Art of Storytellin'
# 2019-10-28

import sqlite3 # enable control of an sqlite database

def uniqueTitle(curse, title): # return a boolean for whether or not a given title matches one already in the table.
    repeats = curse.execute("SELECT Title FROM stories;")
    for titleS in repeats:
        if (names[0] == title):
            return False
    return True

def uniqueUsername(curse, username): # return a boolean for whether or not a given username matches one already in the table
    repeats = curse.execute("SELECT Username FROM users;")
    for names in repeats:
        if (names[0] == username):
            return False
    return True

def addUser(curse, username, password): # add a row to the users database, with the given username/passwrd combo. Return nothing.
    curse.execute("INSERT INTO users (Username, Password) VALUES("+username+","+password+");")

def addEntry(curse, title, entry, author): # add a row to the stories database, with the given title/entry/author combo. Return nothing.
    curse.execute("INSERT INTO stories (Title, Entries, Author) VALUES("+title+","+entry+","+author+");")

#=====TEMPORARILY Returning simple Booleans=====
def authenticate(curse, username, password): # return true if the username/password combo exists within the database, otherwise return false.
    givenUser = (username, password)
    cursorObject = curse.execute("SELECT Password FROM users WHERE Username = '%s';" % username)
    for passwordTuple in cursorObject:
        if (passwordTuple[0] != password):
            return False
        return True
    return False

def getFullStory(curse, title): # return a list of every entry associated with a story within a list for the story
    textEntries = []
    storyTuple = curse.execute("SELECT Entries FROM stories WHERE Title = %s;" % title)
    for currentStory in storyTuple:
        textEntries.append(currentStory)
    return textEntries

def getContributedStories(curse, username): # return a set of the titles of every story contributed to by an author
    contributedStories = []
    titleTuple = curse.execute("SELECT Titles FROM stories WHERE Author = %s;" % username)
    for currentTitle in titleTuple:
        contributedStories.append(currentTitle)
    return set(contributedStories)

def getOtherStories(curse, username): # return a set of the titles of every NOT story contributed to by an author
    notContributedStories = []
    titlesTuple = curse.execute("SELECT Titles FROM stories WHERE Author != %s;" % username)
    for currentTitle in titlesTuple:
        notContributedStories.append(currentTitle)
    return set(notContributedStories)
