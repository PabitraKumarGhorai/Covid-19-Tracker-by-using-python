import requests
print("Second wave Covid-19 tracker:")
print("loading.......")


url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "8a58c60349msh4de5fda0ca7b4dfp1a892ajsnc89e755b4e65",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


print("Press 1. for covid status in India.")
print("Press 2. for City wise Covid status in India.")
n=int(input("Please Enter your choice."))

if(n==1):
    def covid_cases(y):
        active = ''
        confirm = ''
        death = ''
        for t in response['total_values']['active']:
            active=active+t
        for c in response['total_values']['confirmed']:
            confirm=confirm+c
        for d in response['total_values']['deaths']:
            death=death+d
        return {'y1':active,'y2':confirm,'y3':death}

    dict=covid_cases('a')
    a=int(dict['y1'])
    c=int(dict['y2'])
    d=int(dict['y3'])
    dr="{:.2f}".format((d/a)*100)

    print("Total Active cases in India in second wave : ",a)
    print("Total Confirmed cases in India till now : ",c)
    print("Total Death cases in India : ",d)
    print("Death rate in India : ",dr,"%")

if(n==2):
    def city_wise(city):
        for state in response['state_wise']:
            if int(response['state_wise'][state]['active'])!=0:
                for city_wise in response['state_wise'][state]['district']:
                    if(city_wise.lower() == city_name.lower()):
                        return response['state_wise'][state]['district'][city_wise]['active']

    flag=1
    while flag !=0:
        city_name=input("Enter the city : ")
        if city_name == "0":
            break
        case = city_wise(city_name)
        print(case)



