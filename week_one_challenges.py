# each of the functions below have some instructions
# remove the "pass" statement and replace it with your own code
# run the test_week_one_ex<x>.py file to see if your code passes the unit tests


# tests in test_week_one_ex1.py
def multiplication_or_sum(first_number, second_number):
    # given two numbers, if the product is less than 1000 return the product
    # is the product is more than 1000 return the sum
    # e.g. multiplication_or_sum(50, 5) = 250
    # e.g. multiplication_or_sum(50, 50) = 100
    # write your code here, don't forget to include a return statement
    pass


# tests in test_week_one_ex2.py
def return_last_word(list_of_words):
    # given a list of words, return the last one alphabetically
    # e.g. ["mouse", "muskrat", "antelope"] should return muskrat
    # write your code here, don't forget to include a return statement
    pass


# tests in test_week_one_ex3.py
def egg_stamp_decoder(code):
    # Given an eight character egg stamp code e.g. 1UK54321
    # decipher it into its three sections
    #
    # First character is Farming Method
    # 1 = Organic
    # 2 = Free range
    # 3 = Barn
    # 4 = Cage
    #
    # Next two characters are country code
    # UK = United Kingdom
    # NL = Netherlands
    # BE = Belgium
    # DE = Germany
    #
    # Final five charaters are farm ID
    # 
    # e.g. 1UK54321 should output ["Organic", "United Kingdom", "54321"] - note farm ID is a string not a number
    #
    # Invalid codes should output 0
    # write your code here, don't forget to include a return statement
    pass


if __name__ == '__main__':
    print("You can use this area to test your code")
    print(multiplication_or_sum(5, 4))