from ham.cw.ntcexam import GenText
from ham.cw import Cw
import argparse
import logging


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    parser = argparse.ArgumentParser(description="NTC Cw Parser")
    # These are the switches - they do not require params
    parser.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        help="Debug wanted. Set -d to Enable. ",
    )
    # Group
    parser_group = parser.add_mutually_exclusive_group(required=False)
    parser_group.add_argument(
        "-s",
        "-s",
        "--standard",
        dest="output",
        action="store_const",
        const="S",
        default="S",
    )
    parser_group.add_argument(
        "-r", "-R", "--random", dest="output", action="store_const", const="R"
    )
    args = parser.parse_args()
    ntc_gen_text = GenText()
    if args.output == "R":
        test_as_str = ntc_gen_text.random_letters()
        print("Random text chosen")
    else:
        test_as_str = ntc_gen_text.ntctest()
        print("NTC text chosen")
    # print(f"Test_text \n{test_as_str}")
    wav_cnt = ntc_gen_text.count_wav()
    morse = Cw()
    print(f"Creating NTC{wav_cnt}.wav")
    morse.text_to_wav(test_as_str, f"NTC{wav_cnt}.wav")
    with open(f"NTC{wav_cnt}.txt", "wt") as cw_text:
        cw_text.write(
            f"This is the Sample NTC CW Exam.\n\n\n{test_as_str}\n\n\n\n\nGood Luck.\n\n"
        )
    print(f"Please find 2 files - NTC{wav_cnt}.wav and NTC{wav_cnt}.txt")

