import numpy as np
from math import sin, pi
from numpy.random import normal
import pandas as pd
import scipy.io.wavfile as sw

"""
Note that after each dit/dah of the letter P -- one element spacing is used except the last one. (Intra-Character).
After the last dit of P is sent, 3 elements are added (Inter-Character). After the word PARIS - 7 elements are used.
Thus:
P = di da da di = 1 1 3 1 3 1 1 (3) = 14 elements 
A = di da = 1 1 3 (3) = 8 elements 
R = di da di = 1 1 3 1 1 (3) = 10 elements 
I = di di = 1 1 1 (3) = 6 elements 
S = di di di = 1 1 1 1 1 [7] = 12 elements 
Total = 50 elements 
() = intercharacter
[] = interword
If you send PARIS 5 times in a minute (5WPM) you have sent 250 elements (using correct spacing). 250 elements into 60 seconds per minute = 240 milliseconds per element.
"""


class Cw:
    def __init__(self, wpm: int = 5, tq: int = 0):
        """

        :param wpm:  Words per minute
        :param tq: Decay os signal in seconds
        """
        self.WPM = wpm
        self.Tq = tq
        self.gap = ' '
        self.endword ='_'
        self.MorseCode = {
            "!": "-.-.--",
            "$": "...-..-",
            "'": ".----.",
            "(": "-.--.",
            ")": "-.--.-",
            ",": "--..--",
            "-": "-....-",
            ".": ".-.-.-",
            "/": "-..-.",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            ":": "---...",
            ";": "-.-.-.",
            ">": ".-.-.",  # <ar>
            "<": ".-...",  # <as>
            "{": "....--",  # <hm>
            "&": "..-.-",  # <int>
            "%": "...-.-",  # <sk>
            "}": "...-.",  # <ve>
            "=": "-...-",  # <bt>
            "?": "..--..",
            "@": ".--.-.",
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
            "\\": ".-..-.",
            "_": "..--.-",
            "~": ".-.-",
            " ": "_",
        }

    def letter_to_dot_dash(self, letter):
        if letter.lower() in self.MorseCode:
            return self.MorseCode[letter.lower()]
        else:
            raise ValueError

    def len_chr(self, ch):
        """
        Length in dits
        :param ch: Human form character/number etc
        :return: length in dits
        """
        s = self.MorseCode[ch]
        return self.len_dits(s)

    def encode_morse(self, cws: str) -> str:
        """
        Encode string of characters to a Morse code string (dit='.'/dah='-')
        :param cws: cw String 'abc '
        :return: ".- -... -.-.'
        """
        s = []
        for ch in cws.lower():
            try:  # try to find CW sequence from Codebook
                s += self.gap.join(self.MorseCode[ch])
                if ch != self.gap :
                    s += self.gap   # Interblock gap
            except IndexError:
                if ch == self.gap:
                    s.append(self.endword)
                print("error: %s not in Codebook" % ch)
                continue

        return "".join(s).rstrip(self.endword).rstrip(self.gap) + self.endword

    def len_dits(self, cws):
        # length of string in dit units, include spaces
        val = 0
        for ch in cws:
            if ch == ".":  # dit len + el space
                val += 1
            if ch == "-":  # dah len + el space
                val += 3
            if ch == self.gap:  # el space
                val += 1
            if ch == self.endword:  # el space
                val += 7
        return val

    def signal(self, cw_str, sigma=0.0, padded=False, verbose=False):
        """
        :param cw_str: for given CW string i.e. 'ABC '
        :param sigma: adds gaussian noise with standard deviation of sigma to signal
        :param padded:
        :param verbose:
        :return: pandas dataframe with signals and  symbol probabilities
        """
        cw_str = "paris"
        cws = self.encode_morse(cw_str)

        # calculate how many milliseconds this string will take at speed WPM
        dit_len = int(1200 / self.WPM)  # dit length in msec, given WPM
        print(f"dit_len is {dit_len}")
        if padded:
            msec = dit_len * self.len_dits(cw_str) * 32 + 7  # padded to 32
        else:
            msec = dit_len * (
                self.len_dits(cw_str) + 7
            )  # reserve +7 for the last pause
        msec = int(msec)
        print(f"msec is set to {msec}")
        t = np.arange(msec) / 1000.0  # time array in seconds
        ix = list(range(0, int(msec)))  # index for arrays

        # Create a DataFrame and initialize
        col = ["t", "sig", "dit", "dah", "ele", "chr", "wrd", "spd"]
        P = pd.DataFrame(index=ix, columns=col)
        P.t = t  # keep time
        P.sig = np.zeros(msec)  # signal stored here
        P.dit = np.zeros(msec)  # probability of 'dit' stored here
        P.dah = np.zeros(msec)  # probability of 'dah' stored here
        P.ele = np.zeros(msec)  # probability of 'element space' stored here
        P.chr = np.zeros(msec)  # probability of 'character space' stored here
        P.wrd = np.zeros(msec)  # probability of 'word space' stored here
        P.spd = np.ones(msec) * self.WPM  # speed stored here

        # pre-made arrays of zeros and ones with multiple(s) of ditlen
        z = np.zeros(dit_len)
        z2 = np.zeros(2 * dit_len)
        z4 = np.zeros(4 * dit_len)
        dit = np.ones(dit_len)
        dah = np.ones(3 * dit_len)

        # For all dits/dahs in CW string generate the signal, update symbol probabilities
        # Note: this is very slow in Python and could be optimized a lot
        i = 0
        n = 0  # counter for elements until ' ' or '_'
        for ch in cws:
            prct = 100.0 * float(i) / float(msec)
            if (i % 1000) == 0 and verbose:
                print("Done: " + "{:.6f}".format(prct) + "%")
            if ch == ".":
                dur = len(dit)
                P.sig[i : i + dur] = dit
                P.dit[i : i + dur] = dit
                i += dur
                n += dur
                dur = len(z)
                P.sig[i : i + dur] = z
                P.ele[i : i + dur] = np.ones(dur)
                i += dur
                n += dur

            if ch == "-":
                dur = len(dah)
                P.sig[i : i + dur] = dah
                P.dah[i : i + dur] = dah
                i += dur
                n += dur
                dur = len(z)
                P.sig[i : i + dur] = z
                P.ele[i : i + dur] = np.ones(dur)
                i += dur
                n += dur

            if ch == " ":
                dur = len(z2)
                P.sig[i : i + dur] = z2
                P.chr[i : i + dur] = np.ones(dur)
                i += dur
                n += dur
                if padded:
                    fil = 32 - n
                    # print 'i:fil:n',i,fil,n
                    for j in range(fil):
                        dur = len(z)
                        # print 'j:i:dur',j,i,dur
                        P.sig[i : i + dur] = z
                        P.chr[i : i + dur] = np.ones(dur)
                        i += dur
                n = 0

            if ch == "_":
                dur = len(z4)
                P.sig[i : i + dur] = z4
                P.wrd[i : i + dur] = np.ones(dur)
                i += dur
                n += dur
                if padded:
                    fil = 32 - n
                    # print 'i:fil:n',i,fil,n
                    for j in range(fil):
                        dur = len(z)
                        # print 'j:i:dur',j,i,dur
                        P.sig[i : i + dur] = z
                        P.chr[i : i + dur] = np.ones(dur)
                        i += dur
                n = 0

        if self.Tq > 0.0:  # QSB cycle time impacts signal amplitude
            qsb = 0.5 * sin((1.0 / float(self.Tq)) * t * 2 * pi) + 0.55
            P.sig = qsb * P.sig
        if sigma > 0.0:
            P.sig += normal(0, sigma, len(P.sig))
        return P

    def wav(self, pandas_obj, filename="cw.wav"):
        """
        Extract the Wav filename from the Pandas data object.
        :param pandas_obj: A Pandas Data Frame - which has been output from Signal method
        :param filename: Name of the Wav file to create
        :return: A Wav stream object
        """
        sample_rate = 8000

        w = pandas_obj[["sig"]].values.flatten()
        t = pandas_obj[["t"]].values.flatten()

        dit = 1.200 / self.WPM
        # print(dit * t[len(t) - 1])
        # fo = 600.0
        bit_stream = []
        for n in range(0, len(w)):
            bit_stream.append(sin(80 * t[n] * 2 * pi) * w[n])
        # bit_stream = sin(80 * t * 2 * pi) * w
        # plt.plot(t[0:200], s[0:200])
        sw.write(filename, sample_rate, np.array(bit_stream))

    def text_to_wav(self, text, filename="cw.wav"):
        """

        :param text:
        :param filename:
        :return:
        """
        return self.wav(self.signal(text), filename)
