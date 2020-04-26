from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from .agent import Individual

class SocialDistancing_Model(Model):
    """
    A model that creates an isolated neighbourhood on a grid. Individuals are placed arbitrarily on the grid initially, and with each step they are allowed to move to a neighbouring cell.
    A certain percentage of the initial population infected at random to characterise the initial outbreak. 
    As each individual agent moves across the grid, if they occupy a cell with another agent whos is already sick, there will be a certain probability (Transmission Rate) of themselves also being infected. 
    Infected individual agents can recover from the Virus after a certain duration of time (denoted as the Recovery Time). 
    A certain portion of the infected individuals die and are chosen randomly baseed on the Mortatlity Rate.
    Movement of individuals can be employed to indicate social distancing measures. 
    """
    def __init__(self, N, width, height, Initial_Outbreak, TR, RT, MR, Policy):
        self.num_agents = N
        self.grid = MultiGrid(width, height, False)
        self.Init_OB = Initial_Outbreak
        # self.TR = Transmission_Rate
        self.schedule = RandomActivation(self)
        self.running = True 


        self.Transmission = TR #Transmission Rate 
        self.IP = 0   #Incubation Period
        self.Recovery = RT  #Recovery Time 
        self.Mortality = MR

        self.policy = Policy # Percentage Immobile


                # Create agents
        for i in range(self.num_agents):
            a = Individual(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            
            if self.random.random() < self.Init_OB:
                a.condition = 'Sick'
                a.infection_time = 1

            self.grid.place_agent(a, (x, y))
        
            model_reporters = {
                            'Total': lambda m: m.schedule.get_agent_count(),
                            'Healthy': lambda m: self.count_type(m, 'Healthy'),
                            'Sick': lambda m: self.count_type(m, 'Sick'),
                            'Immune': lambda m: self.count_type(m, 'Immune'),
                            'Transmission Rate': self.Transmission,
                            'Recovery Time': self.Recovery,
                            'Mortality Rate': self.Mortality,
                            'Social Distancing Policy': self.policy
                            }

        self.datacollector = DataCollector(model_reporters=model_reporters)


    def step(self):
        self.datacollector.collect(self) #Ensuring the data is stored from all agents for all models. 
        self.schedule.step()
        
        if self.schedule.time == 100:
            self.running = False



    @staticmethod
    def count_type(model, individual_condition):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for individual in model.schedule.agents:
            if individual.condition == individual_condition:
                count += 1
        return count
