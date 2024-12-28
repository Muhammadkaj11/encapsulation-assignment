class StringReversal:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        
        words = self.input_string.split()


        reversed_words = words[::-1]


        reversed_string = " ".join(reversed_words)
        return reversed_string

input_str = "Hello world this is a test"
string_reversal = StringReversal(input_str)
reversed_str = string_reversal.reverse_words()
print(reversed_str)  
