from bs4 import BeautifulSoup
import requests
import re

def get_protein_seq(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')

    protein_seq = str(soup.find_all('pre')[0]).replace('<pre>', '').replace('</pre>', '')
    protein_seq = re.sub(r"0|1|2|3|4|5|6|7|8|9", "", protein_seq).replace(' ', '')
    protein_seq = re.sub(r'\n', '', protein_seq)
    return protein_seq

#Test call
print(get_protein_seq('https://www.fludb.org/brc/proteinSequence.spg?ncbiProteinId=IRD_1095423276_130_2286&decorator=influenza'))