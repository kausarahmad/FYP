#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql


# In[2]:


db = pymysql.connect(host='localhost',user='root',passwd='',db='caroogle')      #connect with database
cursor = db.cursor()


# In[3]:


def get_make(make):
    query_make = ("SELECT dim_make.make_id FROM dim_make WHERE dim_make.make='"+make+"';")
    cursor.execute(query_make)
    return cursor.fetchall()[0][0]

def get_model(model):
    query_model = ("SELECT dim_model.model_id FROM dim_model WHERE dim_model.model='"+model+"';")
    cursor.execute(query_model)
    return cursor.fetchall()[0][0]

def get_fuel(fuel):
    query_fuel = ("SELECT dim_fuel_type.fuel_type_id FROM dim_fuel_type WHERE dim_fuel_type.fuel_type='"+fuel+"';")
    cursor.execute(query_fuel)
    return cursor.fetchall()[0][0]

def get_body(body):
    query_body = ("SELECT dim_body_type.body_type_id FROM dim_body_type WHERE dim_body_type.body_type='"+body+"';")
    cursor.execute(query_body)
    return cursor.fetchall()[0][0]

