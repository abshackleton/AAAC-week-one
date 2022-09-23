def multiplication_or_sum(first_number, second_number):
    # given two numbers, if the product is less than 1000 return the product
    # is the product is more than 1000 return the sum
    # e.g. multiplication_or_sum(50, 5) = 250
    # e.g. multiplication_or_sum(50, 50) = 100
    # write your code here, don't forget to include a return statement
    product = first_number * second_number
    if product > 1000:
        return first_number + second_number
    else:
        return product


def return_last_word(list_of_words):
    # given a list of words, return the last one alphabetically
    # e.g. ["mouse", "muskrat", "antelope"] should return muskrat
    # write your code here, don't forget to include a return statement
    list_of_words.sort()
    return list_of_words[-1]


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
    farming_method_code = code[0]
    farming_method = ""
    if farming_method_code == "1":
        farming_method = "Organic"
    elif farming_method_code == "2":
        farming_method = "Free range"
    elif farming_method_code == "3":
        farming_method = "Barn"
    elif farming_method_code == "4":
        farming_method = "Cage"
    
    country_code = code[1:3]
    country = ""
    if country_code == "UK":
        country = "United Kingdom"
    elif country_code == "NL":
        country = "Netherlands"
    elif country_code == "BE":
        country = "Belgium"
    elif country_code == "DE":
        country = "Germany"
    
    farm = code[3:]

    if farming_method == "" or country == "" or len(code) < 8 or len(code) > 8:
        return 0
    else:
        return [farming_method, country, farm]


if __name__ == '__main__':
    print(multiplication_or_sum(5, 4))