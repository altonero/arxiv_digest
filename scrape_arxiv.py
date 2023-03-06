######################
# This module contains two functions for arXiv web page scraping.
######################

import requests # http requests
from bs4 import BeautifulSoup # web scraping



# The following function makes a soup of the arXiv web page content
def make_soup(url): 
    
    print(f'Making {url} soup...')
    
    response = requests.get(url)
    
    if response:
        print(response,'Success!')
    else:
        print(response, 'An error has occurred.')
    print('')    
    
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    
    return soup



# The following function gets all the New submissions from the arXiv page divided by category: New, Cross-list, Replacements. 
# They are organized in heterogeneous list: (paper number, title, authors and category of submission).
def get_arxiv_newsub(soup): 
    
    lsnew = soup.find_all('dl')[0] 
    lscross = soup.find_all('dl')[1]
    lsreplace = soup.find_all('dl')[2]
    
    title_new = [tag.text.replace('Title:','').strip() for tag in lsnew.find_all('div',attrs={'class':'list-title mathjax'})]
    authors_new = [tag.text.replace('Authors:\n','').replace('\n','') for tag in lsnew.find_all('div',attrs={'class':'list-authors'})]
    enum_new = [j for j in range(1,len(title_new)+1)]
    new =[enum_new,title_new,authors_new,'new']
    
    title_cross = [tag.text.replace('Title:','').strip() for tag in lscross.find_all('div',attrs={'class':'list-title mathjax'})]
    authors_cross = [tag.text.replace('Authors:\n','').replace('\n','') for tag in lscross.find_all('div',attrs={'class':'list-authors'})]
    enum_cross = [j for j in range(len(title_new)+1,len(title_new)+len(title_cross)+1)]
    cross =[enum_cross,title_cross,authors_cross,'cross']
    
    title_replace = [tag.text.replace('Title:','').strip() for tag in lsreplace.find_all('div',attrs={'class':'list-title mathjax'})]
    authors_replace = [tag.text.replace('Authors:\n','').replace('\n','') for tag in lsreplace.find_all('div',attrs={'class':'list-authors'})]
    enum_replace = [j for j in range(len(title_new)+len(title_cross)+1,len(title_new)+len(title_cross)+len(title_replace)+1)]
    repl =[enum_replace,title_replace,authors_replace,'replace']
    
    return new, cross, repl
