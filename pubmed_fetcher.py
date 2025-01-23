import requests
import csv
import xml.etree.ElementTree as ET
from typing import List, Optional

# Function to query PubMed API
def fetch_papers(query: str, max_results: int = 100) -> List[dict]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "xml"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return parse_pubmed_ids(response.text)

def parse_pubmed_ids(xml_data: str) -> List[str]:
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()
    return [id.text for id in root.findall(".//IdList/Id")]

# Function to fetch detailed paper data from PubMed by IDs
def fetch_paper_details(paper_ids: List[str]) -> List[dict]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    papers = []
    for pubmed_id in paper_ids:
        params = {
            "db": "pubmed",
            "id": pubmed_id,
            "retmode": "xml"
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        paper = parse_paper_details(response.text)
        papers.append(paper)
    return papers

def parse_paper_details(xml_data: str) -> dict:
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()
    docsum = root.find(".//DocSum")
    
    pubmed_id = docsum.find(".//Id").text
    title = docsum.find(".//Item[@Name='Title']").text
    pub_date = docsum.find(".//Item[@Name='PubDate']").text
    authors = docsum.findall(".//Item[@Name='Author']")
    corresponding_email = docsum.find(".//Item[@Name='CorrespondingAuthorEmail']").text if docsum.find(".//Item[@Name='CorrespondingAuthorEmail']") else None

    non_academic_authors = []
    company_affiliations = []
    
    for author in authors:
        name = author.text
        affiliation = author.get('Affiliation', "")
        if any(keyword in affiliation.lower() for keyword in ['pharmaceutical', 'biotech', 'company', 'industry']):
            company_affiliations.append(affiliation)
        else:
            non_academic_authors.append(name)
    
    return {
        "PubmedID": pubmed_id,
        "Title": title,
        "PublicationDate": pub_date,
        "NonAcademicAuthors": ", ".join(non_academic_authors),
        "CompanyAffiliations": ", ".join(company_affiliations),
        "CorrespondingAuthorEmail": corresponding_email
    }

# Function to save results to CSV
def save_to_csv(data: List[dict], filename: str):
    keys = data[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

