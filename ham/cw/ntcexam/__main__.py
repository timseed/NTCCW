from ham.cw.ntcexam import GenText
from ham.cw import Cw
import logging
import daiquiri

if __name__ == "__main__":
    ntc_gen_text = GenText()
    test_as_str = ntc_gen_text.ntctest()
    # print(f"Test_text \n{test_as_str}")
    morse = Cw()
    morse.text_to_wav(test_as_str, "NTC.wav")
    with open("NTC.txt", "wt") as cw_text:
        cw_text.write(
            f"This is the Sample NTC CW Exam.\n\n\n{test_as_str}\n\n\n\n\nGood Luck.\n\n"
        )
    print("Please find 2 files - NTC.wav and NTC.txt")
    print("They will be overwritten the next time you run this program")
