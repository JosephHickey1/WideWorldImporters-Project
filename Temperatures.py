#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pyodbc
from Connection import Cnxn


# In[2]:


cnxn, cnxn_str = Cnxn()


# In[3]:


room_data = pd.read_sql("SELECT TOP(2000) RecordedWhen, ColdRoomSensorNumber, Temperature FROM Warehouse.ColdRoomTemperatures_Archive ORDER BY RecordedWhen, ColdRoomSensorNumber", cnxn)

vehicle_data = pd.read_sql("SELECT TOP(2000) VehicleRegistration, RecordedWhen, ChillerSensorNumber, Temperature FROM Warehouse.VehicleTemperatures ORDER BY VehicleRegistration, RecordedWhen, ChillerSensorNumber", cnxn)


# In[20]:


room_curr = room_data['Temperature'][0]
vehicle_curr = vehicle_data['Temperature'][0]


# In[22]:


print(f"The current temperature in the chiller room is: {room_curr}\nThe current temperature in the vehicle chiller is: {vehicle_curr}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




