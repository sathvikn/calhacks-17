from bs4 import BeautifulSoup
import requests
import re

def get_seq_link(genomic_acc):
    url = 'https://www.fludb.org/brc/fluSegmentDetails.spg?ncbiGenomicAccession='+str(genomic_acc)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    link = "https://www.fludb.org"
    for i in soup.find_all('a'):
        if "View Sequence" in i:            
            link += i.get('href');
            break
    return link;
link = get_seq_link('GQ200230')

def get_protein_seq(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')

    protein_seq = str(soup.find_all('pre')[0]).replace('<pre>', '').replace('</pre>', '')
    protein_seq = re.sub(r"0|1|2|3|4|5|6|7|8|9", "", protein_seq).replace(' ', '')
    protein_seq = re.sub(r'\n', '', protein_seq)
    return protein_seq

#Test call
print(get_protein_seq(link))