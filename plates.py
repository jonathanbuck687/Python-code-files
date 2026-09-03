def is_valid(plateNum):
    abc = "qwertyuioplkjhgfdsazxcvbnm"
    nums = "1234567890"

    if (len(plateNum) < 2 or len(plateNum) > 6):
        return("Invalid")
    
    i = 0
    while (i <= len(plateNum) - 1):
        if (not(plateNum[i:i+1] in abc) and not(plateNum[i+1:i+2] in nums)):
            return("Invalid")
        i = i + 1

    if (not(plateNum[:1] in abc) and not(plateNum[1:2] in abc)):
        return("Invalid")
    
    j = 0
    barn = True
    while (j <= len(plateNum) - 1 and barn):
        if ((plateNum[j:j+1] in nums)):
            if ((plateNum[j:j+1] == "0")):
                return("Invalid")
            else:
                barn = False
        j = j + 1
    
    k = 0
    while (k <= len(plateNum) - 2):
        if ((plateNum[k:k+1] in nums)):
            if ((plateNum[k+1:k+2] in abc)):
                return("Invalid")
        k = k + 1
    return "Valid"

def main():
    done = False
    while(not done):
        plateNum = input("Validate: ")
        plateNum = plateNum.lower()
        print(is_valid(plateNum))
        if (is_valid(plateNum) == "Valid"):
            done = True

main()