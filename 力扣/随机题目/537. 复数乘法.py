class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        real1, imag1 = a.split("+")
        imag1 = imag1[:-1]

        real2, imag2 = b.split("+")
        imag2 = imag2[:-1]

        cp1 = complex(int(real1), int(imag1))
        cp2 = complex(int(real2), int(imag2))

        ans_cp = cp1 * cp2

        return "{}+{}i".format(int(ans_cp.real), int(ans_cp.imag))
