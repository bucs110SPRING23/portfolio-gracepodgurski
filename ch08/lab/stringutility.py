class StringUtility:
    def __init__(self,string):
        pass
    
    def vowels(self):
        my_vowels =['a','e','i','o','u','A','E','I','O','U']
        count = 0
        i = 0 
        for i in range(len(test_strings)):
            if test_strings[i] in my_vowels:
                count += 1
        if count < 5:
            return str(count)
        elif count >= 5:
            return "many"

        print("Number of vowels in the string is:",count)

    def bothEnds(self):
        for i in range(len(test_strings)):
            if len(i) > 2:
                return str(test_strings[0]), str(test_strings[1]), str(test_strings[len(test_strings-2)]), str(test_strings[len(test_strings-1)])
            elif len(i)<=2:
                return " "
            
    def fixStart(self):
        for i in test_strings:
        # Find a way to make this not alter the first letter
            if str(i) = str(test_strings[0]):
                append.test_strings(i='*')

    def asciiSum(self):
        # The range of ASCII values for uppercase letters A-Z is 65-90, and the range for lowercase letters a-z is 97-122
        pass
    
    def cipher(self):
        pass
        