import random
from matplotlib import pyplot as plt

number_of_healthy_people = 2500
number_of_sick_people = 2
number_of_days = 100

class person:
    def __init__(self,status) -> None:
        self.status = status
        self.sick_days = 0
        

        
people = [person("healthy") for i in range(number_of_healthy_people)] + \
            [person("sick") for i in range(number_of_sick_people)]  ## need \ for new line
days = [day for day in range(number_of_days)]


#  list with the count of people with each status
#  The first element will be the input data at day 1
healthy = []
sick = []
recovered =[]
dead = []
infection = []

for day in days:
    number_healthy = 0
    number_sick = 0
    number_dead = 0
    number_recovered = 0
    number_new_infection = 0
    
    
    for man in people:
        if man.status == "healthy":
            number_healthy +=1
        elif man.status == "sick":
            number_sick += 1
            man.sick_days += 1 # Count the number of sick days
        elif man.status == "dead":  
            number_dead +=1
        else:
            number_recovered+= 1
    for man in people:
        if man.status == "sick" and man.sick_days == 15:
            if random.randint(0,9) == 9:  # 10% chance ::: random will return a number from 0 to 9
                man.status = "dead"
            else:
                man.status = "recovered"
        
        chance_of_infection = 0.0008*number_sick
        if man.status == "healthy":
            if random.random() > chance_of_infection:
                man.status = "sick"
                number_new_infection += 1

        
    healthy.append(number_healthy)
    sick.append(number_sick)
    recovered.append(number_recovered)
    dead.append(number_dead)
        

fig, axs = plt.subplots(4, sharex=True, sharey=False)
fig.suptitle('VIRUS SIMULATION')
axs[0].plot(days, healthy)
axs[0].set_title('HEALTHY')
axs[1].plot(days, sick, 'tab:orange')
axs[1].set_title('SICK')
axs[2].plot(days, recovered, 'tab:green')
axs[2].set_title('RECOVERED')
axs[3].plot(days, dead, 'tab:red')
axs[3].set_title('DEAD')

plt.show()