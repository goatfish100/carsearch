from craigslist import CraigslistForSale
import json
import os
import emailutil
import jinja2
from dotenv import load_dotenv
load_dotenv()


cl_e = CraigslistForSale(site='sfbay', category='cto', filters={'search_distance': 59, \
                                                                'zip_code': 94087, \
                                                                'auto_bodytype': 'mini-van', \
                                                                'min_year': 2009, \
                                                                'max_price': 5000\
                                                                })

# exclude stuff we don't want -for tickets - we don't want these terms
csales = []

# Connecting to the database file
for result in cl_e.get_results(sort_by='newest'):
    csales.append(result)

# print('1):', all_rows)
#
templateLoader = jinja2.FileSystemLoader( searchpath="/" )
templateEnv = jinja2.Environment( loader=templateLoader )
#
TEMPLATE_FILE = os.environ["PWD"]+'/carsearch.jinja'
template = templateEnv.get_template(TEMPLATE_FILE)
#
templateVars = { "title" : "Car Search",
                 "description" : "A simple inquiry of function.",
                 "favorites" : csales
                }
#
outputText = template.render( templateVars )
#
print(outputText)

f = open("mechspc.html", "a")
f.write(outputText)
f.close()
#emailutil.send_email('james.lapointe@gmail.com', 'car search', outputText)
