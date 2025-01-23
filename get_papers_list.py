import argparse
import logging
from pubmed_fetcher import fetch_papers, fetch_paper_details, save_to_csv

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers based on a query.")
    parser.add_argument("query", help="Query string to search PubMed.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output.")
    parser.add_argument("-f", "--file", help="Output file name for saving results.")
    
    args = parser.parse_args()

    # Enable debug logging if specified
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    
    try:
        # Fetch PubMed IDs
        logging.info("Fetching paper IDs for query: %s", args.query)
        paper_ids = fetch_papers(args.query)
        
        # Fetch detailed paper data
        logging.info("Fetching paper details...")
        papers = fetch_paper_details(paper_ids)
        
        # Save or print results
        if args.file:
            logging.info("Saving results to %s", args.file)
            save_to_csv(papers, args.file)
        else:
            for paper in papers:
                print(paper)
    
    except Exception as e:
        logging.error("An error occurred: %s", str(e))

if __name__ == "__main__":
    main()
