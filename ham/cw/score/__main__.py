import logging
import argparse

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    parser = argparse.ArgumentParser(description="NTC Cw Parser")
    # These are the switches - they do not require params
    parser.add_argument(
        "-f", "--from", dest="from", help="From file",
    )
    parser.add_argument(
        "-t", "--to", dest="to", help="To file",
    )
    args = parser.parse_args()
