from ham.cw.ntcexam import GenText

if __name__ == "__main__":
    g = GenText()
    test = g.ntctest()
    print(f"Test_text \n{test}")
