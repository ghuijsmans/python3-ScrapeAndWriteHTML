#by: https://github.com/ghuijsmans
#import requirements
import bs4 as bs
import requests
import urllib.request

def ReplaceInFile(counter, tableRow):
    if counter > 0:
        fin = open("outputfile.html", "rt")
    elif counter == 0:
        fin = open("inputfile.html", "rt")
    data = fin.read()
    data = data.replace('@'+str(counter), tableRow)
    fin.close()
    
    fin = open("outputfile.html", "wt")
    fin.write(data)
    fin.close()

# set values
the_url = 'https://www.example-site.com/news'
base_url = 'https://www.example-site.com'

# get&interpret html
sauce = urllib.request.urlopen(the_url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# select the unordered list named link-list bigger
section = soup.find('ul', class_='link-list bigger')

# select all list items in $section
subsections = section.find_all('li')

#create start of table
table_start = "<h2>HTML Table</h2>\n<table>"

# for each news item in the news section performs actions described in comments.
counter = 0
for subsection in subsections:
    
    # selects href from single news headline, concatenates it with base-url.
    news_link = base_url + subsection.a.get('href')

    # selects text part from single news headline, strips empty white spaces before and after
    stripped_text = subsection.text.strip()

    # seperates release-date from headline for a single news headline
    news_date = stripped_text[0:5]
    news_headline = stripped_text[5:]

    #create row for table from single news subject
    table_row = "<tr>\n    <th>"+news_date+"</th>\n    <th>"+news_headline+"</th>\n    <th>"+news_link+"</th>\n  </tr>"
    
    ReplaceInFile(counter, table_row)
    counter = counter + 1