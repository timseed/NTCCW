import logging
import argparse
from ham.cw.score import Score

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    parser = argparse.ArgumentParser(description="NTC Cw Parser")
    # These are the switches - they do not require params
    parser.add_argument("-f", "--from", dest="frm", help="From file", required=True)
    parser.add_argument("-t", "--to", dest="to", help="To file", required=True)
    args = parser.parse_args()
    scr = Score(args.frm, args.to)
    print(f"The number of edits is {scr.get_score()}")
