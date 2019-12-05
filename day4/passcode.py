

def digit_count(code:int)->bool:

    for digit in code:
        if(code.count(digit))==2:
            return True
            
    return False


def main():

    lowerbound = 273035
    upperbound = 767253

    valid_nums = 0

    for i in range(lowerbound,upperbound):

        code = [int(j) for j in str(i)]
        
        if(code == sorted(code)
            and digit_count(code)):
            valid_nums+=1
            print(i)

    print("Valid nums {}".format(valid_nums))    

if __name__ == "__main__":
    main()