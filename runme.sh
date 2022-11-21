# This file is blank, you need to make it work for Task 6

#!/bin/bash
chmod +x install.sh
./install.sh
uvicorn main:app --host 0.0.0.0 --port 15688 
