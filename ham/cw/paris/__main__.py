from ham.cw import Cw

if __name__ == "__main__":
    morse = Cw()
    morse.text_to_wav("parisparisparisparisparis ", "paris.wav")
    with open("paris.txt", "wt") as cw_text:
        cw_text.write(
            f"This wav file called paris.wav - should take 1 minute to play. "
            f"As Paris is the test work to determi CW speed."
        )
    print("Please find 2 files - paris.wav and paris.txt")
    print("They will be overwritten the next time you run this program")
