### THEORETICAL PROBABILITY ###

# For the following problems, use python to simulate the problem and calculate an experimental probability, then compare that to the theoretical probability.

from scipy import stats
import numpy as np

# Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3.
# Calculate the following:

#**Theoretical
# What grade point average is required to be in the top 5% of the graduating class?
p_top_5 = 5/100
mean_graduates = 3 
sd_graduates = 0.3
grads = stats.norm(mean_graduates, sd_graduates)

grads.isf(p_top_5)

# An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile.
p_third_point = 3/10
p_fourth_point = 4/10

third_point = grads.ppf(p_third_point)
fourth_point = grads.ppf(p_fourth_point)

# Would a student with a 2.8 grade point average qualify for this scholarship?
n = 2.8
qualify = n > third_point and n < fourth_point 
qualify

# If I have a GPA of 3.5, what percentile am I in?
in_percentile = grads.cdf(3.5)
in_percentile

#**Simulated
sim_no_of_students = 10_000
graduates_data = np.random.normal(mean_graduates, sd_graduates,sim_no_of_students)

top_five_percent = np.percentile(graduates_data, 95)

#30th percentile - 20th percentile
thirtieth_percentile = np.percentile(graduates_data, 30)
twentieth_percentile = np.percentile(graduates_data, 20)

student_gpa = 2.8
student_qualify = student_gpa > twentieth_percentile and student_gpa < thirtieth_percentile

# A marketing website has an average click-through rate of 2%.
# One day they observe 4326 visitors and 97 click-throughs. How likely is it that this many people or more click through?

ctr = 2/100
ctr_observed = 97/4326

website = stats.poisson(ctr).sf(ctr_observed)
website

# You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.
# What is the probability that at least one of your first 60 answers is correct?

questions = 100
p_success = 0.5

homework = stats.binom(questions, p_success).pmf(60) #pmf because being correct or incorrect is discrete?
homework

first_sixty = np.random.choice(["Correct", "Incorrect"],(sim_visitors,60))

((first_sixty == "Incorrect").sum(axis=1) == 60).mean()

# The codeup staff tends to get upset when the student break area is not cleaned up.
# Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area.
# How likely is it that the break area gets cleaned up each day? How likely is it that it goes two days without getting cleaned up? All week?

p_cleaning = .03
n_students = .90 * (3*22)

#success = days the break area is cleaned

cleaning = stats.binom(n_students,p_cleaning).pmf(5) #all week days
cleaning

cleaning = stats.binom(n_students,p_cleaning).pmf(1) #once in a week
cleaning

cleaning = stats.binom(n_students,p_cleaning).pmf(0) #not cleaned at all
cleaning

# You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime.
# After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed
# with a mean of 15 and standard deviation of 3.
# If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food
# what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class?
# Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

p_of_service = .2
mean_customers = 15
sd_customers = 3

served = stats.norm(mean_customers,sd_customers)

order_time = 12

# Connect to the employees database and find the average salary of current employees, along with the standard deviation. Model the distribution of employees salaries with a normal distribution and answer the following questions:

def get_db_url(u,p,h,d):
    url = f'mysql+pymysql://{u}:{p}@{h}/{d}'
    return url

# Use your function to obtain a connection to the employees database.
from env import host, user, password

host = host
user = user
password = password

url = get_db_url(user,password,host,"employees")
url

salaries_df = pd.read_sql('SELECT * FROM salaries', url)

# What percent of employees earn less than 60,000?

salaries_df.head()

mean_salary = salaries_df.salary.mean()
sd_salary = salaries_df.salary.std()

salary_dist = stats.norm(mean_salary,sd_salary)

salary_dist.cdf(60_000)

# What percent of employees earn more than 95,000?

salary_dist.sf(95_000)

# What percent of employees earn between 65,000 and 80,000?

lower_bound = salary_dist.sf(65_000)
upper_bound = salary_dist.sf(80_000)

in_between = lower_bound - upper_bound
in_between

# What do the top 5% of employees make?

percentage = .95

salary_dist.isf(percentage)


### EXPERIMENTAL PROBABILITY ###

import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(3)

# A marketing website has an average click-through rate of 2%.
# One day they observe 4326 visitors and 97 click-throughs.
# How likely is it that this many people or more click through?

sim_visitors = 100_000_000
ctr_observed
mean_website = 2/100


sim_ctr = np.random.normal(mean_website, 0.03, sim_visitors) >= ctr_observed
sim_ctr.mean()

# You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place.
# Looking to save time, you put down random probabilities as the answer to each question.
# What is the probability that at least one of your first 60 answers is correct?

#bunch of data, see if the first 60 answers out of 100 are correct.



# The codeup staff tends to get upset when the student break area is not cleaned up.
# Suppose that there's a 3% chance that any one student cleans the break area when they visit it,
# and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area.
# How likely is it that the break area gets cleaned up each day? How likely is it that it goes two days without getting cleaned up? All week?

cleaning_probability = ["Cleaned"] * 2 + ["Not Cleaned"] * 64

weekly_cleaning_streak = (((np.random.choice(cleaning_probability,(sim_visitors,7)) == "Cleaned").sum(axis=1)) == 7).mean()

weekly_cleaning_streak_2 = (((np.random.choice(cleaning_probability,(sim_visitors,2)) == "Not Cleaned").sum(axis=1)) == 2).mean()

weekly_cleaning_streak_7 = (((np.random.choice(cleaning_probability,(sim_visitors,7)) == "Not Cleaned").sum(axis=1)) == 7).mean()

# You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime.
# After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3.
# If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

mean_customers
sd_customers

panaderia_traffic = np.random.normal(mean_customers,sd_customers,sim_visitors)

panaderia_traffic_with_time = panaderia_traffic * 12

(panaderia_traffic_with_time <= 45).mean()

# Connect to the employees database and find the average salary of current employees, along with the standard deviation.
# Model the distribution of employees salaries with a normal distribution and answer the following questions:
# What percent of employees earn less than 60,000?
# What percent of employees earn more than 95,000?
# What percent of employees earn between 65,000 and 80,000?
# What do the top 5% of employees make?

employees_simulation = np.random.normal(mean_salary,sd_salary,sim_visitors)
(employees_simulation < 60_000).mean()
(employees_simulation > 95_000).mean()

((employees_simulation >= 65_000) & (employees_simulation <= 80_000)).mean()

top_5_employee_salary = np.percentile(employees_simulation,95)
top_5_employee_salary

# A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars.
# Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.
# What is the probability that no cars drive up in the noon hour?
# What is the probability that 3 or more cars come through the drive through?
# How likely is it that the drive through gets at least 1 car?

cars = np.random.poisson(2,sim_visitors)
cars
plt.hist(cars)

no_cars = (np.isin(cars,0).sum())/len(cars)
three_or_more_cars = (cars >= 3).mean()
at_least_one = (cars > 0).mean()
