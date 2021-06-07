#!/usr/bin/env python
# coding: utf-8

# Establishes secure connection to SQL Server database.

# In[1]:


# pyodbc is an open source python <==> sql interface allowing sql code to be run in python code
import pyodbc
# getpass keeps an input password from being written to the filestream in plaintext
from getpass import getpass


# In[2]:


# Creates a pyodbc connection 
def Cnxn(ip='24.251.129.86', server='PEREGRINE\SQLEXPRESS', database='WideWorldImporters'):
    # server optionally takes the filepath of the target server defaulting to my local server
    # database optionally takes the name of the target database defaulting to WWI for this project
    # username optionally takes a UID variable only used if not a trusted connection
    # Returns a connection object and a functional connection string for use with pandas
    
    # Fixes -151 case connection error
    def HandleHierarchyId(v):
        return str(v)
    
    # Begins by trying to connect as a trusted connection using environment variables
    try:
        # Constructs the connection string
        connection_str = 'Driver={SQL Server Native Client 11.0};' + f'Server={server};Database={database};Trusted_Connection=yes;'
        # Forms connection and handles -151 error
        connection = pyodbc.connect(connection_str)
        connection.add_output_converter(-151, HandleHierarchyId)
        # Turns off autocommit to reduce the chances of a mistaken transaction
        connection.autocommit = False
        
    
    except:
        
        try:
            # Constructs the alternate connection string querying a password
            server = str(ip) + '\SQLEXPRESS'
            connection_str = 'Driver={SQL Server Native Client 11.0};' + f'Server={server};Database={database};UID={str("Enter your UID: ")};PWD={str(getpass(prompt="Enter your password: "))}"'
            # Forms connection and handles -151 error
            connection = pyodbc.connect(connection_str)
            connection.add_output_converter(-151, HandleHierarchyId)
            # Turns off autocommit to reduce the chances of a mistaken transaction
            connection.autocommit = False
            
        # Handles errors associated with a bad UID or PWD
        except InterfaceError:
            print("An InterFace Error has occurred. Please check that the username and password entered are correct and try again.")
        
    # Returns the connection and string
    finally:
        return connection, connection_str
        
    
    


# ## Unit Test

# In[3]:


if __name__ == "__main__":
    import pandas as pd
    cnxn, cnxn_str = Cnxn('24.251.129.86')
    data = pd.read_sql("SELECT TOP(10) * FROM Application.Cities", cnxn)
    print(data)
    
    

