# initially assum every link starts with
# <a href ="<url>">....
# We are not worrying how we got the actual content of the page
# Find the start of the first link

# -----------------------------------------------
# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''


start_link = page.find("<a href=") #return the value of where the first link starts

# -----------------------------------------------
# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')


start = page.find('http', start_link)
end = page.find('"', start)

print url

# OR OR OR OR

start = page.find("\"", start_link) + 1
end = page.find("\"",sstart +1)

url = page[start:end]

print url


# OR OR OR OR

start_quote = page.find('"',start_link)
end_quote = page.find('"', start_link+1)

url = page[start_quote+1:end_quote]
