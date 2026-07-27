class MultipleFunctionCall():
        def Subfields():
            hope_AI_topic = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
            print("Sub-fields in AI are:")
            for i in hope_AI_topic:
                print(i)      

        def OddEven():
            oddeven = int(input("Enter the Number to check, the given Number is Odd or Even :"))
            if oddeven % 2 == 0:
                print(f'{oddeven} is a Even Number')
            else:
                print(f'{oddeven} is a Odd Number') 

        def Eligibility():
            gender = input("Enter your Gender :").upper()
            age = int(input("Enter your Age :"))
            if (gender == "MALE" or gender == "M") and age >= 21:
                print("You are Eligible for Getting Married")
            elif (gender == "FEMALE" or gender == "F") and age >= 18:
                print("You are Eligible for Getting Married")
            else:
                print("Sorry, You are Not Eligible for Marriage")

        def percentage():
            print("Enter you 10th Marks to Caluclate your Percentage")
            tamil = int(input("TAMIL   :"))
            english = int(input("ENGLISH :"))
            maths = int(input("MATHS   :"))
            science = int(input("SCIENCE :"))
            social = int(input("SOCIAL  :"))
            total = tamil + english + maths + science + social
            percentage = total / 5
            print("Your Total is :",total)
            print("Your Percentage is :",percentage)


        def area():
            height = int(input("Enter Height of the Triangle:"))
            breadth = int(input("Enter Breadth of the Triangle:"))
            area_calc = (height * breadth) / 2
            print("Area of Triangle:",area_calc)
    
        def perimeter():
            side_1 = int(input("Enter the Length of Side A:"))
            side_2 = int(input("Enter the Length of Side B:"))
            side_3 = int(input("Enter the Length of Side C:"))
            perimeter_calc = side_1 + side_2 + side_3
            print("Perimeter of Triangle:",perimeter_calc)