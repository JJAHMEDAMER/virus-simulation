import random
from matplotlib import pyplot as plt


number_of_healthy_people = 25000
number_of_sick_people = 25
number_of_days_to_simulate = 100
number_of_zones = 75
class person:
    def __init__(self,status) -> None:
        self.status = status
        self.days_sick = 0
        self.zone = 0
        
        
class ZONE:
    def __init__(self,zone_id) -> None:
        self.zone_id = zone_id
        self.number_of_people_in_zone = 0
        self.number_of_sick_people = 0
        
        
people = [person("healthy") for i in range(number_of_healthy_people)] + \
    [person("sick") for i in range(number_of_sick_people)]

days = [day for day in range(number_of_days_to_simulate)]

zones = [ZONE(i) for i in range(number_of_zones)]



healthy = list()
sick = list()
recovered = list()
dead = list()



for day in days:
    number_healthy = 0
    number_sick = 0
    number_dead = 0
    number_recovered = 0
    number_new_infection = 0
    
    for man in people:
            man.zone = zones[random.randint(0, len(zones)-1)]
    
    #  COUNTING 
    for man in people:
        #man.zone = random.randint(0, number_of_zones)
        if man.status == "healthy":
            number_healthy += 1
        elif man.status == "sick":
            number_sick += 1
            man.days_sick += 1
            man.zone.number_of_sick_people += 1
        elif man.status == "recovered":
            number_recovered += 1
        else:
            number_dead += 1
            
    for man in people:
        if man.status == "sick" and man.days_sick == 15:
            if random.randint(0,9) == 9:
                man.status = "dead"
            else:
                man.status = "recovered"
        infection_rate = 0.0008*man.zone.number_of_sick_people
        if man.status == "healthy":
            if random.random() < infection_rate:
                man.status = "sick"
       
    for x in zones:
        x.number_of_sick_people = 0
             
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
    
    
    
    
    
    
    
    
    