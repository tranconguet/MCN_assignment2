class PrefixCodeTree:
    def __init__(self, codebook={}):
        self.codebook = codebook

    def insert(self, codeword, symbol):
        self.codebook[symbol] = ''.join(str(el) for el in codeword)

    def decode(self, encodedData, datalen):
        bytes_as_bits = ''.join(format(byte, '08b') for byte in encodedData)  # convert bytes to bits data
        bitdata = bytes_as_bits[:datalen]  # use only datalen bits
        print(bitdata)
        res = ''
        while bitdata != '':
            for pre in self.codebook:
                if bitdata.startswith(self.codebook[pre]):  # if data starts with any codeword then added to res
                    res += pre
                    bitdata = bitdata[len(self.codebook[pre]):]  # remove recent codeword added
        return res
