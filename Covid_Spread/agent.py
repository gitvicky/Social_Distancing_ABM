# import numpy as np
# from mesa import Agent

# class Individual(Agent):
#     """
#     An Individual Cell that could represent a household/office or an individual. 

#     Attributes:
#         x, y: Grid coordinates
#         condition: Can be "Healthy", "Sick", or "Immune"
#         unique_id: (x,y) tuple.

#     unique_id isn't strictly necessary here, but it's good
#     practice to give one to each agent anyway.
#     """
#     def __init__(self,unique_id, model):
#         """
#         Create a new agent
#         Args:
#             pos: The agent's coordinates on the grid.
#             model: standard model reference for agent.
#         """
#         super().__init__(unique_id, model)
#         self.condition = 'Healthy'
#         self._next_condition = None
#         self.infected_time = 0
#         self.infection_time = 0


#         self.TR = self.model.Transmission #Transmission Rate 
#         self.IP = 5  #Incubation Period
#         self.RT = self.model.Recovery  #Recovery Time 
#         self.MR = self.model.Mortality

#         self.policy = self.model.policy # Percentage Immobile

#     @property
#     def hasSick(self):
#         return self.condition == 'Sick'

#     @property
#     def occupants(self):
#         return self.model.grid.iter_cell_list_contents(self.pos)

#     def move(self):
#         possible_steps = self.model.grid.get_neighborhood(
#             self.pos,
#             moore=True,
#             include_center=False)
#         new_position = self.random.choice(possible_steps)
#         self.model.grid.move_agent(self, new_position)

#     def get_infected(self):
#         self.infected_time = self.model.schedule.time 
#         self.get_sick()


#     def get_sick(self): 
#         self.infection_time  = self.model.schedule.time - self.infected_time
#         if self.infection_time > self.IP:
#             self.condition = 'Sick'

#     def recovery(self):
#         self.infection_time  = self.model.schedule.time - self.infected_time
#         if self.infection_time > self.RT:
#             self.condition = 'Immune'

#     def death(self):
#         # if self.infection_time > 14 :
#         self.model.grid._remove_agent(self.pos, self)
#         self.model.schedule.remove(self)



#     def pass_on(self):
#         # print(self.unique_id, self.condition)
        
#         sick_occupants = sum(occupant.hasSick for occupant in self.occupants)
#         if sick_occupants > 1:
#             for occupant in self.occupants:
#                 if occupant.condition == 'Sick':
#                     occupant.recovery() 
#                 elif occupant.condition == 'Healthy':
#                     if np.random.uniform() < self.TR :
#                         occupant.get_sick()
            
#         if self.condition == "Sick":
#             self.recovery()
#             if np.random.uniform() < self.MR :
#                 self.death()   

#         if sick_occupants > 1 and self.infected_time ==0:
#             if np.random.uniform() < self.TR :
#                 self.get_infected()
            

#         if sick_occupants > 1 and self.condition == 'Healthy':
#             self.get_sick()


#     def step(self):
#         """
#         Move an agent to a neihbouring cell and check whether it can pass on the virus. 
#         """
#         # assume no state change
#         # self._next_condition = self.condition
#         if np.random.uniform() > self.policy:
#             self.move()
#         self.pass_on()
#         print(self.model.schedule.time)



#     # def advance(self):
#     #     '''
#     #     Set the condition to the new computed condition -- computed in step().
#     #     '''
#     #     self.condition = self._next_condition
    
#     def get_pos(self):
#         return self.pos
        
import numpy as np
from mesa import Agent

class Individual(Agent):
    """
    An Individual Cell that could represent a household/office or an individual. 
    Attributes:
        x, y: Grid coordinates
        condition: Can be "Healthy", "Sick", or "Immune"
        unique_id: (x,y) tuple.
    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """
    def __init__(self,unique_id, model):
        """
        Create a new agent  
        Args:
            pos: The agent's coordinates on the grid.
            model: standard model reference for agent.
        """
        super().__init__(unique_id, model)
        self.condition = 'Healthy'
        self._next_condition = None
        self.infection_time = 0


        multiplier = 3
        self.TR = self.model.Transmission #Transmission Rate 
        self.IP = 0 * multiplier #Incubation Period
        self.RT = self.model.Recovery * multiplier #Recovery Time 
        self.MR = self.model.Mortality / multiplier 

        self.HC = 5000

        self.policy = self.model.policy # Percentage Immobile


    @property
    def hasSick(self):
        return self.condition == 'Sick'

    @property
    def occupants(self):
        return self.model.grid.iter_cell_list_contents(self.pos)

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)


    def get_sick(self):
        self.infection_time +=1
        if self.infection_time > self.IP:
            self.condition = 'Sick'

    def recovery(self):
        self.infection_time += 1 
        if self.infection_time > self.RT:
            self.condition = 'Immune'

    def death(self):
        if self.infection_time > 14 :
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)



    def pass_on(self):
        # print(self.unique_id, self.condition)
        
        sick_occupants = sum(occupant.hasSick for occupant in self.occupants)
        if sick_occupants > 1:
            for occupant in self.occupants:
                if occupant.condition == 'Sick':
                    occupant.recovery() 
                elif occupant.condition == 'Healthy':
                    if np.random.uniform() < self.TR :
                        occupant.get_sick()
            
        if self.condition == "Sick":
            self.recovery()
            if np.random.uniform() < self.MR:
                self.death()   
            elif self.model.count_type(self.model, 'Sick') > self.HC and np.random.uniform() < 0.10:
                self.death()


        if sick_occupants > 1 and self.condition == 'Healthy':
            if np.random.uniform() < self.TR :
                self.get_sick()


    def step(self):
        """
        Move an agent to a neihbouring cell and check whether it can pass on the virus. 
        """
        # assume no state change
        # self._next_condition = self.condition
        if np.random.uniform() > self.policy:
            self.move()
        self.pass_on()


    # def advance(self):
    #     '''
    #     Set the condition to the new computed condition -- computed in step().
    #     '''
    #     self.condition = self._next_condition
    
    def get_pos(self):
        return self.pos