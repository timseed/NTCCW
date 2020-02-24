import numpy as np
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
        self.audio_sample_rate = 44000.0
        self.WPM = wpm
        self.Tq = tq
        self.dit = "."
        self.dah = "-"
        self.gap = "g"
        self.endletter = "e"
        self.endword = "_"
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
        return self.length_in_dits(s)

    def cw_timing(self, cws: str) -> str:
        """
        Encode string of characters to a Morse code string (dit='.'/dah='-')
        :param cws: cw String 'abc '
        :return: ".- -... -.-.'
        """
        s = []
        for ch in cws.lower():
            try:  # try to find CW sequence from Codebook
                s += self.gap.join(self.MorseCode[ch])
                s += self.endletter  # End of letter gap
            except IndexError:
                if ch == " ":
                    s += self.endword
                print("error: %s not in Codebook" % ch)
                continue

        return "".join(s).rstrip(self.endword).rstrip(self.endletter) + self.endword

    def length_in_dits(self, cws):
        # length of string in dit units, include spaces
        val = 0
        for ch in cws:
            if ch == self.dit:  # dit len + el space
                val += 1
            if ch == self.dah:  # dah len + el space
                val += 3
            if ch == self.gap:  # el space
                val += 1
            if ch == self.endletter:  # el space
                val += 3
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
        cws = self.cw_timing(cw_str)

        # calculate how many milliseconds this string will take at speed WPM
        dit_len = int(1200 / self.WPM)  # dit length in msec, given WPM
        # print(f"dit_len is {dit_len}")
        if padded:
            msec = dit_len * self.length_in_dits(cws) * 32 + 7  # padded to 32
        else:
            msec = dit_len * (
                self.length_in_dits(cws) + 7
            )  # reserve +7 for the last pause
        msec = int(msec)
        # print(f"msec is set to {msec}")
        print(f"This will take {msec/1000} seconds to finish creating your test.")
        bin_data = {
            self.gap: (0, dit_len),
            self.dit: (600, dit_len),
            self.dah: (600, dit_len * 3),
            self.endletter: (0, dit_len * 3),
            self.endword: (0, dit_len * 7),
        }
        wav_buff = np.zeros(10)  # Start off the Audio data will nothing
        for ch in cws:
            if ch in bin_data:
                freq = bin_data[ch][0]
                time_in_ms = bin_data[ch][1]
                wav_buff = np.concatenate(
                    [wav_buff, self.make_audio(time_in_ms / 1000.0, freq)]
                )
            else:
                print(f"Got unknown timing symbol {ch}")
        # print("Audio generation completed")
        return np.array(wav_buff, dtype=np.int16)

    def make_audio(self, time: float = 1.0, frequency: int = 440) -> np.array:
        """
        Create an audio frequency for the required time and duration
        :param time:
        :param frequency:
        :return: Np array of INT16
        """

        # Generate time of samples between 0 and two seconds
        samples = np.arange(self.audio_sample_rate * time) / self.audio_sample_rate
        # print(f"Number of samples is {len(samples)}")
        # Recall that a sinusoidal wave of frequency f has formula w(t) = A*sin(2*pi*f*t)
        wave = 10000 * np.sin(2 * np.pi * frequency * samples)
        # Convert it to wav format (16 bits)
        wav_wave = np.array(wave, dtype=np.int16)
        return wav_wave

    def wav(self, np_audio_data, filename="cw.wav"):
        sw.write(filename, int(self.audio_sample_rate), np.array(np_audio_data))

    def text_to_wav(self, text: str, filename: str = "cw.wav"):
        """

        :param text:
        :param filename:
        :return:
        """
        return self.wav(self.signal(text.replace("\n", "")), filename)
