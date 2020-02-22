from ham.cw.ntcexam import GenText
from ham.cw import Cw

if __name__ == "__main__":
    g = GenText()
    test = g.ntctest()
    print(f"Test_text \n{test}")
    line1 = test.split("\n")[0]
    print(f"Line1  \n{line1}")
    morse = Cw()
    paris = morse.cw_timing("paris paris paris")
    p = morse.signal("paris paris paris")
    morse.text_to_wav(line1)
    #p = morse.signal2("paris paris paris")
    #morse.wav2(p, "cw.wav")
    print("Done")
