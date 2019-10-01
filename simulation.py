import numpy as np
import pandas as pd

np.random.seed(123)
# How likely is it that you roll doubles when rolling two dice?

n_trials = 10_000
n_dice = 2

two_rolls = np.random.choice([1,2,3,4,5,6], (n_trials,n_dice))
two_rolls = pd.DataFrame(two_rolls)

only_doubles = two_rolls.apply(lambda row: row[0] == row[1], axis=1).sum()
p_doubles = only_doubles/len(two_rolls)

# If you flip 8 coins, what is the probability of getting exactly 3 heads?
# What is the probability of getting more than 3 heads?

n_trials = 10_000
n_coins = 8

flips = np.random.choice(["head","tail"], (n_trials, n_coins))
flips = pd.DataFrame(flips)

flips.head(1)

def count_heads(row):
    no_of_heads = 0
    for cell in row:
        if cell == "head":
            no_of_heads += 1
    return no_of_heads

p_three_heads = flips.apply(count_heads,axis=1).apply(lambda row: row >= 3).mean()
p_more_than_three_heads = flips.apply(count_heads,axis=1).apply(lambda row: row > 3).mean()

# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup.
# Assuming that Codeup randomly selects an alumni to put on a billboard
# what are the odds that the two billboards I drive past both have data science students on them?

ds = 1/4

n_times = 100_000
n_billboards = 2

weighted_sim_ds = np.random.random((n_times,n_billboards)) <= ds
weighted_sim_ds = pd.DataFrame(weighted_sim_ds)

weighted_sim_ds # Data Frame with 100,000x instances, 2 billboards you drive past, with the DS probability
            
# Probability of instance being both true:
both_ds = weighted_sim_ds.apply(lambda row: row[0] and row[1] == True, axis=1).mean()
both_ds

# Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine.
# If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

n_instance = 1000
stock = 17

daily_consumption = np.random.uniform(1.5,4.5,n_instance)

p_week_consumption = np.random.choice(daily_consumption,(n_instance,5))
p_week_consumption = pd.DataFrame(p_week_consumption)
p_of_within_stock = p_week_consumption.apply(lambda row: row.sum() <= 17, axis=1).mean()

p_of_within_stock

# Compare Heights
# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?

n_choices = 10_000

men_height = np.random.normal(178,8,n_choices)
women_height = np.random.normal(170,6,n_choices)

random_height = pd.DataFrame({"men":men_height, "women":women_height})

p_of_taller_woman = random_height.apply(lambda row: row[1] > row[0], axis=1).mean()

# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails.
# What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?
# What is the probability that we observe an installation issue within the first 150 students that download anaconda?
# How likely is it that 450 students all download anaconda without an issue?

#Answers
#probability of failure after 50 students
failure = 1/250
n_downloads = 50

weighted_sim_dl = np.random.random(n_downloads) <= failure

weighted_sim_dl.mean() 

#probability of failure after 100 students
failure = 1/250
n_downloads = 100

weighted_sim_dl = np.random.random(n_downloads) <= failure

weighted_sim_dl.mean() 

#probability of failure after 150 students
failure = 1/250
n_downloads = 150

weighted_sim_dl = np.random.random(n_downloads) <= failure

weighted_sim_dl.mean() 

#probability of failure after 450 students
failure = 1/250
n_downloads = 150

weighted_sim_dl = np.random.random(n_downloads) <= failure

weighted_sim_dl.mean() 

# There's a 70% chance on any given day that there will be at least one food truck at Travis Park.
# However, you haven't seen a food truck there in 3 days. How unlikely is this?

food_truck = .70
n_days = 365

weighted_sim_days = np.random.random(n_days) < food_truck
weighted_sim_days = pd.DataFrame(weighted_sim_days)

def skip_three_days(df):
    for row in df:
        row.index 
p_no_food_truck = weighted_sim_days.apply(lambda row: row[])


p_of_taller_woman = random_height.apply(lambda row: row[1] > row[0], axis=1).mean()


# How likely is it that a food truck will show up sometime this week?

# If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?