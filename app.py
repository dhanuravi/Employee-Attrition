from pywebio.output import *
from pywebio.input import * 
from flask import Flask, send_from_directory
from  pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH,start_server
import time
from data import encode
from test import ada,gb,xg
import argparse
import statistics
from statistics import mode
app = Flask(__name__)


def attrition():
    with popup("Welcome to Attrition predictor"):
        put_text("Kindly fill all the required information to get results")
    Age = input("Enter the age of employee",type = NUMBER,placeholder = "age")
    BusinessTravel = select('Which the type of BusinessTravel?', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    DailyRate = input("Enter the DailyRate of employee",type = NUMBER,placeholder = "range 102 to 1499")
    Department = select('Which the type of Department?', ['Sales', 'Research & Development', 'Human Resources'])
    DistanceFromHome = input("Enter the distance from home",type = NUMBER,placeholder = "range 1 to 29")
    Education = select('Which the type of Education?', ['1','2','3','4','5'])
    EducationField = select('Which the field of Education?', ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'])
    EmployeeCount = 1
    EnvironmentSatisfaction = select('Which the Environment Satisfaction level?', ['1','2','3','4'])
    Gender = select('Which the gender of employee?', ['Female', 'Male'])
    HourlyRate  = input("Enter the HourlyRate",type = NUMBER,placeholder = "range 30 to 100")
    JobInvolvement = select('select JobInvolvement level of employee?', ['1','2','3','4'])
    JobLevel = select('select joblevel of employee?', ['1','2','3','4','5'])
    JobRole = select('select the JobRole of employee', ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
    JobSatisfaction = select('select JobSatisfaction level of employee?', ['1','2','3','4'])
    MaritalStatus =  select('select the marital status of employee?', ['Single', 'Married', 'Divorced'])
    MonthlyIncome  = input("Enter the MonthlyIncome",type = NUMBER,placeholder = "range 1009 to 19999")
    MonthlyRate	  = input("Enter the MonthlyRate",type = NUMBER,placeholder = "range 2094 to 26999")
    NumCompaniesWorked = input("Enter the Number of Companies Worked",type = NUMBER,placeholder = "range 0 to 9")
    OverTime =  select('does the employee do overtime?', ['Yes', 'No'])
    PercentSalaryHike = input("Enter the PercentSalaryHike",type = NUMBER,placeholder = "range 11 to 25")
    PerformanceRating = select('select PerformanceRating', ['1','2','3', '4','5'])
    RelationshipSatisfaction  = select('select Relationship Satisfactionlevel', ['1','2','3', '4'])
    StandardHours = 80
    StockOptionLevel= select('select StockOptionLevel', ['0','1','2','3'])
    TotalWorkingYears = input("Enter the working years",type = NUMBER,placeholder = "range 0 to 40")
    TrainingTimesLastYear = select('select no of TrainingTimesLastYear', ['0','1','2','3','4','5','6'])
    WorkLifeBalance  = select('select WorkLife Balance Satisfactionlevel', ['1','2','3', '4'])
    YearsAtCompany = input("Enter the Years At Company",type = NUMBER,placeholder = "range 0 to 40")
    YearsInCurrentRole	 = input("Enter the Years In CurrentRole",type = NUMBER,placeholder = "range 0 to 18")
    YearsSinceLastPromotion		= input("Enter the Years Since LastPromotion",type = NUMBER,placeholder = "range 0 to 15")
    YearsWithCurrManager	 = input("Enter the Years With CurrManager",type = NUMBER,placeholder = "range 0 to 17")




    Gender = int(encode['colname']['Gender'][Gender])
    BusinessTravel = int(encode['colname']['BusinessTravel'][BusinessTravel])
    Department = int(encode['colname']['Department'][Department])
    EducationField = int(encode['colname']['EducationField'][EducationField])
    JobRole = int(encode['colname']['JobRole'][JobRole])
    MaritalStatus = int(encode['colname']['MaritalStatus'][MaritalStatus])
    OverTime = int(encode['colname']['OverTime'][OverTime])
    Education = int(Education)
    EnvironmentSatisfaction = int(EnvironmentSatisfaction)
    JobInvolvement = int(JobInvolvement)
    JobLevel = int(JobLevel)
    JobSatisfaction = int(JobSatisfaction)
    PerformanceRating = int(PerformanceRating)
    RelationshipSatisfaction = int(RelationshipSatisfaction)
    StockOptionLevel = int(StockOptionLevel)
    TrainingTimesLastYear = int(TrainingTimesLastYear)
    WorkLifeBalance = int(WorkLifeBalance)

    data = [Age	,BusinessTravel	,DailyRate,	Department,	DistanceFromHome	,Education,	EducationField,	EmployeeCount	,EnvironmentSatisfaction	,Gender,	HourlyRate,	JobInvolvement	,JobLevel,	JobRole,	JobSatisfaction	,MaritalStatus	,MonthlyIncome	,MonthlyRate,	NumCompaniesWorked	,OverTime	,PercentSalaryHike	,PerformanceRating	,RelationshipSatisfaction,	StandardHours	,StockOptionLevel,	TotalWorkingYears	,TrainingTimesLastYear,	WorkLifeBalance,	YearsAtCompany,	YearsInCurrentRole,	YearsSinceLastPromotion	,YearsWithCurrManager]

    #data = [39,	0,	592	,1,	2	,3,	1	,1,	1	,0,	54,	2	,1,	2	,1,	2,	3646,	17181,	2,	1,	23,	4	,2,	80,	0,	11	,2,	4	,1,	0,	0	,0]
    result=[]
    result.append(ada(data)[0])
    result.append(xg(data)[0])
    result.append(gb(data)[0])
    final = mode(result)
    put_processbar('bar')
    for i in range(1, 11):
        set_processbar('bar', i / 10)
        time.sleep(0.1)
    put_markdown("Here is your result")
    if final == 1:
        put_text('Employee will leave!')
        put_image(open('leave.jpg', 'rb').read())
        put_text('  ')
        put_text('  ')
        put_text('when attrition crosses a particular threshold, it becomes a cause for concern. For example, attrition among minority employee groups could be hurting diversity at your organization. Or, attrition among senior leaders can lead to a significant gap in organizational leadership')
        put_text('  ')
        put_text('Here are some steps to reduce attrition rate!')
        
        put_text('1.  COMMUNICATE YOUR VISION')
        put_text('      When your staff is in the loop of what’s driving the business, they will share in the same vision that you have. It earns their dedication and commitment')
        put_text('  ')
        
        put_text('2.  OPTIMIZE RECRUITMENT')
        put_text('      You can optimize your recruitment process by starting with clear and specific requirements. Set goals for hiring for a position and clearly list the tasks and responsibilities, and what value the position will bring to your business')
        put_text('  ')
        
        put_text('3.  MAKE THE INTERVIEW MATTER')
        put_text('      The interview questions should be based on past and present work performance and behaviours. Allow the candidate to demonstrate their skill levels, motivations and competencies in their fields of experience')
        put_text('  ')
        
        put_text('4.  IMPROVE WORK CONDITIONS')
        put_text('      What you offer as work benefits is a big deal for your employees. Top companies that are known for their perks for their employees have strong development programs, outstanding benefits not only for employees but also to their families, and fun work cultures. When a business knows to meet the needs of their employees beyond the office, they benefit more from their employees.')
        put_text('  ')
        
        put_text('5.  CREATE A PLEASANT WORKSPACE')
        put_text('      Employees spend almost half a day inside their workplaces. Any person would want that place to be where they are most productive, happy, healthy, and engaged. A person’s well-being affects his productivity and work performance, so it is common sense to provide for such.')
        put_text('  ')
        
        put_text('6.  BENEFITS AND PERKS')
        put_text('      The most common reason employees leave is because of the their salary. No matter how loyal and how driven they are with the company’s vision, if it cannot meet with their financial needs, they often look for new jobs.A great addition to any salary package are the benefits. You can add in paid time off, stock options, and even education assistance. ')
        put_text('  ')
        
        put_text('7.  EMPLOYEE ENAGEMENT')
        put_text('      When you have talented employees, you need to find ways that you can help them expand their skill set. Give your feedback, let them know what you think. Pay attention, and let them know that you are there for them. If you don’t engage with them, they will get bored and complacent, and think that they are not growing within the organization.')
        put_text('  ')
        put_image(open('doyouknow.jpg', 'rb').read())
        put_text('  ')
        put_text('Some positive and interesting facts about your company:')
        put_text('  1.The overall attrition rate of your firm is 16.12% - a pretty good number')
        put_text('  2.66% of your employees are good in balancing work life balance and only 1.97 are bad in work life balance.')
        put_text('  3.28.3% of employees do overtime. -Try to reduce this number')
        put_text('  4.Most of the employees are satisfied working here except 289.')
        put_text('  5.Average income of a employee is 6.50k')
        put_text('  6.Average years a employee at company is 7.01')
        put_text('  7.Every 2.19 years a employee gets promoted in your firm.')
        put_text('  8.Average salary hike is 15.21')
        put_text('  ')
    
    else:
        put_text('Employee will stay!')
        put_image(open('stay.jpg', 'rb').read())
        put_text('  ')
        put_text('Some positive and interesting facts about your company:')
        put_text('  ')
        put_image(open('doyouknow.jpg', 'rb').read())
        put_text('  ')
        
        put_text('  1.The overall attrition rate of your firm is 16.12% - a pretty good number')
        put_text('  2.66% of your employees are good in balancing work life balance and only 1.97 are bad in work life balance.')
        put_text('  3.28.3% of employees do overtime. -Try to reduce this number')
        put_text('  4.Most of the employees are satisfied working here except 289.')
        put_text('  5.Average income of a employee is 6.50k')
        put_text('  6.Average years a employee at company is 7.01')
        put_text('  7.Every 2.19 years a employee gets promoted in your firm.')
        put_text('  8.Average salary hike is 15.21')
        put_text('  ')


app.add_url_rule('/','webio_view',webio_view(attrition),methods = ['GET','POST','OPTIONS'])
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(attrition, port=args.port)
