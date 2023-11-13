# https://www.hackerrank.com/challenges/string-validators/

if __name__ == '__main__':
    s = input()
    
    def string_validator(string):
        has_alphanumeric = False
        has_alphabetical = False
        has_digit = False
        has_lowercase = False
        has_uppercase = False
        
        for char in string:
            if char.isalnum():
                has_alphanumeric = True
            if char.isalpha():
                has_alphabetical = True
            if char.isdigit():
                has_digit = True                
            if char.islower():
                has_lowercase = True
            if char.isupper():
                has_uppercase = True
                
        print(has_alphanumeric)
        print(has_alphabetical)
        print(has_digit)
        print(has_lowercase)
        print(has_uppercase)       
                
    string_validator(s)                
