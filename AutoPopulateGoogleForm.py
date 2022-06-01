from datetime import date
##package for url opening 
import webbrowser as wb

##input name 
# =============================================================================
# name = input('Please enter your name: ')
# =============================================================================

name = 'Zhongwang Huang'

where_to_work = str(input('Where are you working at today? (wfh or 520) '))

##auto-today's date
workdate = str(date.today())

##comment in-out shortcut: cmd+4 or cmd+1
# =============================================================================
# print(workdate)
# print(name)
# =============================================================================

##remove leading & trailing space
name = name.strip()
workdate = workdate.strip()

# =============================================================================
# print(workdate)
# print(name)
# =============================================================================

##inserting value into string: f-strings & curly brace {}
##produce pre-populated url for WFH
wfh_url = f"https://docs.googwfhle.com/forms/d/e/1FAIpQLScfPitmPfVr3cDoTQF5WKDuy2T21lV_WgKSFxSoVTzQTScadA/viewform?usp=pp_url&entry.1201986466={workdate}&entry.1584861851={name}&entry.863531926=Home&entry.760522857=NA - Working from home"


##produce pre-populated URL for working at 520
office_url = f"https://docs.google.com/forms/d/e/1FAIpQLScfPitmPfVr3cDoTQF5WKDuy2T21lV_WgKSFxSoVTzQTScadA/viewform?usp=pp_url&entry.1201986466={workdate}&entry.1584861851={name}&entry.863531926=Office-520&entry.760522857=Yes"


##If condition 
if where_to_work == 'wfh':
    url = wfh_url
    print(url)
    wb.open_new(url)

elif where_to_work == '520':
    url = office_url
    print(url)
    wb.open_new(url)

else: print('Re-enter your working location: wfh? 520?')





