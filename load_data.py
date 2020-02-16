# To add a new cell, type ''
# To add a new markdown cell, type ' '
 
# ## webscraping 


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

 

def load_all_data():
    # ### February Debate

    URL = "https://www.rev.com/blog/transcripts/new-hampshire-democratic-debate-transcript"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')



    temp = soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')
    moderator = temp[0].text + " " + temp[1].text

    pars = [moderator]

    for i, p in enumerate(soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')):
        if (i > 1):
            pars.append(p.text)



    feb = {
        "name": [],
        "time": [],
        "text": [],
    }

    for text in pars:
        feb["name"].append(text.split(': ',1)[0])
        feb["time"].append(text.split(': ',1)[1].split(' ',1)[0])
        feb["text"].append(text.split(': ',1)[1].split(' ',1)[1])
        
    feb_df = pd.DataFrame(data = feb)



    feb_df.to_csv("data/february_transcript.csv", index = False)

    
    # ### January Debate


    URL = "https://www.rev.com/blog/transcripts/january-iowa-democratic-debate-transcript"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')



    temp = soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')
    wolf = temp[0].text + " " + temp[1].text

    pars = [wolf]

    for i, p in enumerate(soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')):
        if (i > 1):
            pars.append(p.text)



    jan = {
        "name": [],
        "time": [],
        "text": [],
    }

    for text in pars:
        jan["name"].append(text.split(': ',1)[0])
        jan["time"].append(text.split(': ',1)[1].split(' ',1)[0])
        jan["text"].append(text.split(': ',1)[1].split(' ',1)[1])
        
    jan_df = pd.DataFrame(data = jan)



    jan_df.to_csv("data/january_transcript.csv", index = False)

    
    # ### December Debate


    URL = "https://www.rev.com/blog/transcripts/december-democratic-debate-transcript-sixth-debate-from-los-angeles"
    r = requests.get(URL)


    soup = BeautifulSoup(r.content, 'html5lib')



    pars = []
    for i, p in enumerate(soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')):
            pars.append(p.text)
            
    dec = {
        "name": [],
        "time": [],
        "text": [],
    }

    for text in pars:
        dec["name"].append(text.split(': ',1)[0])
        dec["time"].append(text.split(': ',1)[1].split(' ',1)[0])
        dec["text"].append(text.split(': ',1)[1].split(' ',1)[1])
        
    dec_df = pd.DataFrame(data = dec)



    dec_df.to_csv("data/december_transcript.csv", index = False)

    
    # ### November Debate


    URL = "https://www.rev.com/blog/transcripts/november-democratic-debate-transcript-atlanta-debate-transcript"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')



    pars = []
    for i, p in enumerate(soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')):
            pars.append(p.text)
            
    nov = {
        "name": [],
        "time": [],
        "text": [],
    }

    for i, text in enumerate(pars):
        try:
            nov["name"].append(text.split(': ',1)[0])
            nov["time"].append(text.split(': ',1)[1].split(' ',1)[0])
            if(i == 263):
                nov["text"].append("")
            else:
                nov["text"].append(text.split(': ',1)[1].split(' ',1)[1])
        except:
            print(i)
        
    nov_df = pd.DataFrame(data = nov)



    nov_df.to_csv("data/november_transcript.csv", index = False)

    
    # ### October Debate


    URL = "https://www.rev.com/blog/transcripts/october-democratic-debate-transcript-4th-debate-from-ohio"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')



    pars = []
    for i, p in enumerate(soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')):
            pars.append(p.text)
            
    octbr = {
        "name": [],
        "time": [],
        "text": [],
    }

    for text in pars:
        octbr["name"].append(text.split(': ',1)[0])
        octbr["time"].append(text.split(': ',1)[1].split(' ',1)[0])
        octbr["text"].append(text.split(': ',1)[1].split(' ',1)[1])
        
    oct_df = pd.DataFrame(data = octbr)



    oct_df.to_csv("data/october_transcript.csv", index = False)

    
    # ### September Debate


    URL = "https://www.rev.com/blog/transcripts/democratic-debate-transcript-houston-september-12-2019"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')



    pars = []
    for i, p in enumerate(soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')):
            pars.append(p.text)
            
    sept = {
        "name": [],
        "time": [],
        "text": [],
    }

    for i, text in enumerate(pars):
        try:
            if(i != 225):     
                sept["name"].append(text.split(': ',1)[0])
                sept["time"].append(text.split(': ',1)[1].split(' ',1)[0])
                sept["text"].append(text.split(': ',1)[1].split(' ',1)[1])
        except:
            print(i)
        
        
        
    sept_df = pd.DataFrame(data = sept)



    sept_df.to_csv('data/september_transcript.csv', index = False)

    
    # ### July Debates
    
    # #### Debate 1


    URL = "https://www.rev.com/blog/transcripts/transcript-of-july-democratic-debate-night-1-full-transcript-july-30-2019"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')



    pars = []
    for i, p in enumerate(soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')):
        if i > 1:
            pars.append(p.text)
            
    july1 = {
        "name": [],
        "time": [],
        "text": [],
    }

    for i, text in enumerate(pars):
        try: 
            if i != 274 and i != 645:
                july1["name"].append(text.split(': ',1)[0])
                july1["time"].append(text.split(': ',1)[1].split(' ',1)[0])
                july1["text"].append(text.split(': ',1)[1].split(' ',1)[1])
        except:
            print(i)
        
        
        
    july1_df = pd.DataFrame(data = july1)



    july1_df.to_csv("data/july1_transcript.csv", index = False)

    
    # #### Debate 2


    URL = "https://www.rev.com/blog/transcripts/transcript-of-july-democratic-debate-2nd-round-night-2-full-transcript-july-31-2019"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')



    pars = []
    for i, p in enumerate(soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')):
        if i > 1:
            pars.append(p.text)
            
    july2 = {
        "name": [],
        "time": [],
        "text": [],
    }

    for i, text in enumerate(pars):
        try:    
            july2["name"].append(text.split(': ',1)[0])
            july2["time"].append(text.split(': ',1)[1].split(' ',1)[0])
            july2["text"].append(text.split(': ',1)[1].split(' ',1)[1])
        except:
            print(i)
        
        
        
    july2_df = pd.DataFrame(data = july2)



    july2_df.to_csv("data/july2_transcript.csv", index = False)

    
    # ### June Debates
    
    # #### Debate 1


    file = open('data/Democratic Presidential Debate - June 26.txt')
    temp = file.read()
    temp = temp.split('\n')[0::2]
    pars = []
    for line in range(len(temp)):
        if temp[line][0] != '[':
            pars.append(temp[line])



    june1 = {
        "name": [],
        "time": [],
        "text": [],
    }

    for text in pars:
        june1["name"].append(text.split(':')[2].split(' ', 1)[1])
        june1["time"].append('(' + text.split(' ', 1)[0] + ')')
        june1["text"].append(text.split(':')[3].split(' ', 1)[1])

    june1_df = pd.DataFrame(data = june1)



    june1_df.to_csv("data/june1_transcript.csv", index = False)

    
    # #### Debate 2


    URL = "https://www.rev.com/blog/transcripts/transcript-from-night-2-of-the-2019-democratic-debates"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')



    pars = []
    for i, p in enumerate(soup.find('div', attrs = {'class' : 'fl-callout-text'}).find_all('p')):
        if i > 0:
            pars.append(p.text)
            
    june2 = {
        "name": [],
        "time": [],
        "text": [],
    }

    for i, text in enumerate(pars):
        try:    
            june2["name"].append(text.split(': ',1)[0])
            june2["time"].append(text.split(': ',1)[1].split(' ',1)[0])
            june2["text"].append(text.split(': ',1)[1].split(' ',1)[1])
        except:
            print(i)
        
        
        
    june2_df = pd.DataFrame(data = june2)



    june2_df.to_csv("data/june2_transcript.csv", index = False)


def main():
    load_all_data()

if __name__ == '__main__':
    main()