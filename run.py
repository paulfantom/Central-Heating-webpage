#!/usr/bin/env python3
from app import app

app.run(host='0.0.0.0',port=80) #port under 1000 needs root
#app.run(debug=True)