from ham.cw.ntcexam import GenText
from ham.cw import Cw

if __name__ == "__main__":
    g = GenText()
    test = g.ntctest()
    print(f"Test_text \n{test}")
    line1 = test.split("\n")[0]
    print(f"Line1  \n{line1}")
    morse = Cw()
    paris=morse.cw_timing("paris")
    # morse.text_to_wav(line1)
    p = morse.signal(line1)
    morse.wav(p, "cw.wav")
