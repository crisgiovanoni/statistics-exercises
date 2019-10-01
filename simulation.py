# How likely is it that you roll doubles when rolling two dice?

n_trials = 10_000
n_dice = 2

two_rolls = np.random.choice([1,2,3,4,5,6], (n_trials,n_dice))

only_doubles = two_rolls.sum(axis=1) >= 1

(lambda row: row[0] == row[1], axis=1)]
doubles



# If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

# Compare Heights

# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?
# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?

# What is the probability that we observe an installation issue within the first 150 students that download anaconda?

# How likely is it that 450 students all download anaconda without an issue?

# There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?

# How likely is it that a food truck will show up sometime this week?

# If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?