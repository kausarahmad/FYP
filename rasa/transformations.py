#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import numpy


# In[24]:


def transform_badge(badge):
    try:
        if (numpy.isnan(badge)):
            badge = ''
            return badge
    except:
        pass
    badge = re.sub(r"(?i)(^no$)|(^all\W?others$)", "", badge)
    badge = re.sub(r"^[^0-9A-Za-z]+$", "", badge)
    badge = badge.upper()
    badge = re.sub(r"-| ", "", badge)
    badge = re.sub(r"(?i)4WD", "4X4", badge)
    badge = re.sub(r"(?i)lpg", "", badge)
    
    return badge

