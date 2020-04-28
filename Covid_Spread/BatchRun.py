# %%
import numpy as np
import pandas as pd

# %%
from agent import Individual
from model import SocialDistancing_Model

from mesa.batchrunner import BatchRunner

# %%
# model = SocialDistancing_Model(N=10000,
#                                width = 100,
#                                 height=100,
#                                 Initial_Outbreak=0.2)

# model = SocialDistancing_Model(50, 10, 10, 0.1)
# for i in range(20):
#     model.step()
# %%
# model.run_model()

# %%
# results =model.datacollector.get_model_vars_dataframe()    


# %%
fixed_params = {
    "N": 10000,
    "width": 100,
    "height": 100,
    'Initial_Outbreak': 0.1,
    'TR': 0.5,
    'RT': 28,
    'MR': 0.02,
    'Policy': 0.0
}
variable_params = None

#
# %%
batch_run = BatchRunner(
     SocialDistancing_Model,
     variable_params,
     fixed_params,
     iterations=20,
     max_steps=100,
    model_reporters={"Data Collector": lambda m: m.datacollector})


# %%
batch_run.run_all()
# %%
run_data_0 = batch_run.get_model_vars_dataframe()



# %%

fixed_params = {
    "N": 10000,
    "width": 100,
    "height": 100,
    'Initial_Outbreak': 0.1,
    'TR': 0.5,
    'RT': 28,
    'MR': 0.02,
    'Policy': 0.25
}
variable_params = None

batch_run_25 = BatchRunner(
     SocialDistancing_Model,
     variable_params,
     fixed_params,
     iterations=20,
     max_steps=100,
    model_reporters={"Data Collector": lambda m: m.datacollector})

batch_run_25.run_all()

run_data_25 = batch_run_25.get_model_vars_dataframe()


fixed_params = {
    "N": 10000,
    "width": 100,
    "height": 100,
    'Initial_Outbreak': 0.1,
    'TR': 0.5,
    'RT': 28,
    'MR': 0.02,
    'Policy': 0.50
}
variable_params = None

batch_run_50 = BatchRunner(
     SocialDistancing_Model,
     variable_params,
     fixed_params,
     iterations=20,
     max_steps=100,
    model_reporters={"Data Collector": lambda m: m.datacollector})

batch_run_50.run_all()

run_data_50 = batch_run_50.get_model_vars_dataframe()


fixed_params = {
    "N": 10000,
    "width": 100,
    "height": 100,
    'Initial_Outbreak': 0.1,
    'TR': 0.5,
    'RT': 28,
    'MR': 0.02,
    'Policy': 0.75
}
variable_params = None

batch_run_75 = BatchRunner(
     SocialDistancing_Model,
     variable_params,
     fixed_params,
     iterations=20,
     max_steps=100,
    model_reporters={"Data Collector": lambda m: m.datacollector})

batch_run_75.run_all()

run_data_75 = batch_run_75.get_model_vars_dataframe()



fixed_params = {
    "N": 10000,
    "width": 100,
    "height": 100,
    'Initial_Outbreak': 0.1,
    'TR': 0.5,
    'RT': 28,
    'MR': 0.02,
    'Policy': 0.90
}
variable_params = None

batch_run_90 = BatchRunner(
     SocialDistancing_Model,
     variable_params,
     fixed_params,
     iterations=20,
     max_steps=100,
    model_reporters={"Data Collector": lambda m: m.datacollector})

batch_run_90.run_all()

run_data_90 = batch_run_90.get_model_vars_dataframe()




# %%
import pandas as pd
def create_df(run_data, pol_val):

    br_step_data = pd.DataFrame()
    for i in range(len(run_data)):
        i_run_data = run_data["Data Collector"][i].get_model_vars_dataframe()
        br_step_data = br_step_data.append(i_run_data, ignore_index=True)

    br_step_data['N'] = pd.Series(np.ones(2000)*fixed_params['N'])
    br_step_data['Initial_Outbreak'] = pd.Series(np.ones(2000)*fixed_params['Initial_Outbreak'])
    br_step_data['TRansmission_Rate'] = pd.Series(np.ones(2000)*fixed_params['TR'])
    br_step_data['Recovery_Time'] = pd.Series(np.ones(2000)*fixed_params['RT'])
    br_step_data['Mortality_Rate'] = pd.Series(np.ones(2000)*fixed_params['MR'])
    br_step_data['Policy'] = pd.Series(np.ones(2000)*pol_val)
    br_step_data['Exp_#'] =  pd.Series(np.ones(2000))
    br_step_data['Time'] = pd.Series(np.ones(2000))

    for ii in range(len(br_step_data)):
        br_step_data['Time'][ii] = ii%100
        br_step_data['Exp_#'][ii] = ii//100 + 1 

    return br_step_data

# %%
Policy_0 = create_df(run_data_0, 0.0)
Policy_25 = create_df(run_data_25, 0.25)
Policy_50 = create_df(run_data_50, 0.50)
Policy_75 = create_df(run_data_75, 0.75)
Policy_90 = create_df(run_data_90, 0.90)

# %%

Policy_0.to_csv('/Users/Vicky/Desktop/Code/Agent_Based_Modelling/Social_Distancing/Social_Distancing_ABM/Run_Data/Policy_0.csv')
Policy_25.to_csv('/Users/Vicky/Desktop/Code/Agent_Based_Modelling/Social_Distancing/Social_Distancing_ABM/Run_Data/Policy_25.csv')
Policy_50.to_csv('/Users/Vicky/Desktop/Code/Agent_Based_Modelling/Social_Distancing/Social_Distancing_ABM/Run_Data/Policy_50.csv')
Policy_75.to_csv('/Users/Vicky/Desktop/Code/Agent_Based_Modelling/Social_Distancing/Social_Distancing_ABM/Run_Data/Policy_75.csv')
Policy_90.to_csv('/Users/Vicky/Desktop/Code/Agent_Based_Modelling/Social_Distancing/Social_Distancing_ABM/Run_Data/Policy_90.csv')

# %%

import numpy as np
import pandas as pd 

Policy_0 = pd.read_csv('/Users/vgopakum/Desktop/Github/Social_Distancing_ABM/Run_Data/Policy_0.csv')
Policy_25 = pd.read_csv('/Users/vgopakum/Desktop/Github/Social_Distancing_ABM/Run_Data/Policy_25.csv')
Policy_50 = pd.read_csv('/Users/vgopakum/Desktop/Github/Social_Distancing_ABM/Run_Data/Policy_50.csv')
Policy_75 = pd.read_csv('/Users/vgopakum/Desktop/Github/Social_Distancing_ABM/Run_Data/Policy_75.csv')
Policy_90 = pd.read_csv('/Users/vgopakum/Desktop/Github/Social_Distancing_ABM/Run_Data/Policy_90.csv')


# %%
Avg_Policy_0 = pd.DataFrame()

sums_val_healthy = []
sums_val_sick = []
sums_val_immune = []

#Calculating Mean and Variance
for ii in range(100):
    sums_healthy = []
    sums_sick = []
    sums_immune = []

    for jj in range(20):
        sums_healthy.append(Policy_0['Healthy'][ii+jj*100])
        sums_sick.append(Policy_0['Sick'][ii+jj*100])
        sums_immune.append(Policy_0['Immune'][ii+jj*100])

    sums_val_healthy.append(int(sum(sums_healthy)/20))
    sums_val_sick.append(int(sum(sums_sick)/20))
    sums_val_immune.append(int(sum(sums_immune)/20))

# %%

import seaborn as sns 
import matplotlib.pyplot as plt

def Policy_Impact_plot(policy_data, title_string):
    
    plt.figure()
    ax = sns.lineplot(x="Time", y="Total", 
                      color=sns.xkcd_rgb["amber"],
                      data=policy_data, label ='Total')
    
    sns.lineplot(x="Time", y="Healthy",
                 color=sns.xkcd_rgb["medium green"],
                 data=policy_data, label='Healthy')
    
    sns.lineplot(x="Time", y="Sick", 
                 color=sns.xkcd_rgb["pale red"],
                 data=policy_data, label ='Sick')
    
    sns.lineplot(x="Time", y="Immune",
                 color=sns.xkcd_rgb["denim blue"],
                 data=policy_data, label='Immune')
    
    ax.set(xlabel='Time', ylabel='# Individuals')
    ax.set(title=title_string)


# %%

Policy_Impact_plot(Policy_0, "No Social Distancing")
Policy_Impact_plot(Policy_25, "25% Social Distancing")
Policy_Impact_plot(Policy_50, "50% Social Distancing")
Policy_Impact_plot(Policy_75, "75% Social Distancing")
#Policy_Impact_plot(Policy_90, "90% Social Distancing")