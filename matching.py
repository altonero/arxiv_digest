from scrape_arxiv import *
from sending_email import *
import  datetime # date and time manipulation




# The following function takes as input a list of scraped papers in the format of the output 
# of get_arxiv_newsub() function defined in scrape_arxiv.py. It produces as output an html string with 
# all papers that have a specific keyword in the title. 
def match_keyword(keyword,list): 
    
    listmatch = []
    
    for k in range(len(list[1])):
    
        if keyword.lower() in list[1][k].lower():
            listmatch.append(k)
            
    cntk=''
    
    if len(listmatch)!=0:
        
        print(keyword + " found in the following " + list[3] + " submissions:\n")
        cntk += '<b>'+keyword.upper()+'</b>' + " found in the following " + list[3] + " submissions:" +  '<br><br>\n'
        
        for i in listmatch:
            
            print(str(list[0][i])+")",list[1][i])
            cntk += '<b>'+str(list[0][i])+") "+list[1][i]+ '</b>' + '<br>\n'
            
            if list[0][i] / 10 < 1:
                print('   Authors: '+ list[2][i]+'\n')
                cntk += '      Authors: '+ list[2][i]+ '<br><br>\n'
            else:
                print('    Authors: '+ list[2][i]+'\n')
                cntk += '       Authors: '+ list[2][i]+ '<br><br>\n'
                
        return cntk

    if len(listmatch)==0:
        
        pass


# The following function takes as input a list of scraped papers in the format of the output 
# of get_arxiv_newsub() function defined in scrape_arxiv.py. It produces as output an html string with 
# all papers written by a specific author name. 
def match_author(name,list): 
    
    listmatch = []
    
    for k in range(len(list[2])):
    
        if name.lower() in list[2][k].lower():
            listmatch.append(k)
            
    cntk=''
    
    if len(listmatch)!=0:
        
        print(name + " found in the following " + list[3] + " submissions:\n")
        cntk += '<b>'+name.upper()+'</b>' + " found in the following " + list[3] + " submissions:" +  '<br><br>\n'
        
        for i in listmatch:
            
            print(str(list[0][i])+")",list[1][i])
            cntk += '<b>'+str(list[0][i])+") "+list[1][i]+ '</b>' + '<br>\n'
            
            if list[0][i] / 10 < 1:
                print('   Authors: '+ list[2][i]+'\n')
                cntk += '      Authors: '+ list[2][i]+ '<br><br>\n'
            else:
                print('    Authors: '+ list[2][i]+'\n')
                cntk += '       Authors: '+ list[2][i]+ '<br><br>\n'
                
        return cntk

    if len(listmatch)==0:
        
        pass



def search_keywords(klist,cat='hep-ph',type='new',send=False):
    
    if not isinstance(klist,list): 
        raise Exception("The input is not a list!")
    
    url = 'http://arxiv.org/list/'+cat+'/new'
    
    soup = make_soup(url)

    list_new, list_cross, list_repl = get_arxiv_newsub(soup)
    
    if type == 'new':
        lar = list_new
    elif type == 'cross':
        lar = list_cross
    elif type == 'replace':
        lar = list_repl

    now = datetime.datetime.now()
    date = str(now.day) + '-' + str(now.month) + '-' + str(now.year)
    
    print(date +': Searching for user selected keywords in the titles of today\'s '+cat+' '+type+' submissions.' + ' ' + '\n')

    cnt=''
    
    for word in klist:
        cntp = match_keyword(word,lar)
        if cntp!=None:
            cnt += cntp 
      
    if cnt =='':
        cnt += '<b>'+"No matches from your keywords\' list!"+'</b>'+'<br><br>\n'
        print("No matches from your keyword\' list!")

    cnt += 'For more details visit <a href=\"'+url+'\"+>arxiv.org/list/'+cat+'/new</a>'+'<br><br>\n'
    #print(cnt)

    if send == True:
        
        # create subject as plain text
        subject='Scraping titles of '+cat+' arXiv new submissions - ' + type + ' - ' + date
        sendemail(subject,cnt)
        
        
        
def search_authors(autlist,cat='hep-ph',type='new',send=False):
    
    url = 'http://arxiv.org/list/'+cat+'/new'
    
    soup = make_soup(url)

    list_new, list_cross, list_repl = get_arxiv_newsub(soup)
    
    if type == 'new':
        lar = list_new
    elif type == 'cross':
        lar = list_cross
    elif type == 'replace':
        lar = list_repl

    now = datetime.datetime.now()
    date = str(now.day) + '-' + str(now.month) + '-' + str(now.year)
    
    print(date +': Searching for user selected authors in today\'s '+cat+' '+type+' submissions.' + ' ' + '\n')

    cnt=''
    
    for name in autlist:
        cntp = match_author(name,lar)
        if cntp!=None:
            cnt += cntp 
      
    if cnt =='':
        cnt += '<b>'+"No matches from your authors\' list!"+'</b>'+'<br><br>\n'
        print("No matches from your authors\' list!")

    cnt += 'For more details visit <a href=\"'+url+'\"+>arxiv.org/list/'+cat+'/new</a>'+'<br><br>\n'
    #print(cnt)

    if send == True:
        
        # create subject as plain text
        subject='Scraping authors of '+cat+' arXiv new submissions - ' + type + ' - ' + date
        sendemail(subject,cnt)