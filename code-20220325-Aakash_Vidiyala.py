import json

# Opening JSON file
f = open('1.json')
#Perfoming json.load to extract the data
data=json.load(f)
count_overweight=0


#Calculating the range
def BMI_Range(x):
    if(x<=18.4):
        return 1
    if(x>=18.5 and x<=24.9):
        return 2
    if(x>=25 and x<=29.9):
        return 3
    if(x>=30 and x<=34.9):
        return 4
    if(x>=35 and x<= 39.9):
        return 5
    return 6
#Return the relevant string for the given range
def BM_Rng(x):
    if(x==1):
        return "18.4"
    if(x==2):
        return "18.5-24.9"
    if(x==3):
        return "25-29.9"
    if(x==4):
        return "20-34.9"
    if(x==5):
        return "35-39.9"
    return "40 and above"

#Returning the BMI Category for a given BMI
def BMI_Category(x):
    BmiRng=BMI_Range(x)
    if(BmiRng==1):
        d="Underweight"
        return d
    if(BmiRng==2):
        d="Normal weight"
        return d
    if(BmiRng==3):
        d="Overweight"
        return d
    if(BmiRng==4):
        d="Moderately obese"
        return d
    if(BmiRng==5):
        d="Severely obese"
        return d
    d="Very severely obese"
    return d
#Returning the Health Risk for a given BMI
def Health_Risk(x):
    BmiRng=BMI_Range(x)
    if(BmiRng==1):
        d="Malnutrition risk"
        return d
    if(BmiRng==2):
        d="Low risk"
        return d
    if(BmiRng==3):
        d="Enhanced risk"
        return d
    if(BmiRng==4):
        d="Medium risk"
        return d
    if(BmiRng==5):
        d="High risk"
        return d
    d="Very high risk"
    return d
#Iterating through the given json

for i in data:
    gender=i['Gender']
    height=i['HeightCm']
    height/=100
    weight=i['WeightKg']
    bmi=weight/(height*height)
    BmiCat=BMI_Category(bmi)
    i['BMI Category']=BmiCat
    bmiRange=BMI_Range(bmi)
    if(bmiRange==3):
        count_overweight+=1
    BmRg=BM_Rng(bmiRange)
    i['BMI Range']=BM_Rng(BmRg)
    HealthRisk=Health_Risk(bmiRange)
    i['Health risk']=HealthRisk
    #print(i)
    '''print("Gender=",gender)
    print("Height=", height)
    print("Weight=", weight)
    
    print("BMI=",)'''

#Display the updated data
print(data)
print("Number of Overweight people =",count_overweight)
