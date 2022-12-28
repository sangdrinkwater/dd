from re import A

class BMR:    
    def getName():
        f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\name.txt", "r")
        name = f.read()
        f.close()
        return name

    def getAge():
        f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\age.txt", "r")
        age = f.read()
        f.close()
        return age

    def getWeight():
        f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\weight.txt", "r")
        weight = f.read()
        f.close()
        return weight

    def getHeight():
        f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\height.txt", "r")
        height = f.read()
        f.close()
        return height

    def getGender():
        f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\gender.txt", "r")
        gender = f.read()
        f.close()
        return gender

    def calBMR():
        if gender == "male":
            bmr = 88.376 + 13*weight + 4.799*height - 5.677*age
        elif gender == "female": 
            bmr = 447.593 + 9.247*weight + 3.098*height - 4.330*age

        bmr = round(bmr)
        return bmr
