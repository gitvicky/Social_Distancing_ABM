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
run_data = batch_run.get_model_vars_dataframe()


# %%
import pandas as pd
br_step_data = pd.DataFrame()
for i in range(len(run_data)):
    i_run_data = run_data["Data Collector"][i].get_model_vars_dataframe()
    br_step_data = br_step_data.append(i_run_data, ignore_index=True)

# %%
