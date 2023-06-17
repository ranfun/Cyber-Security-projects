To install the library, Run the following command on your terminal window 

-> pip install cryptidy

To execute the server, Run the following command on your terminal window (Make sure data_base.csv and private.txt are in the same folder with the script)

-> python3 server.py <port_number> data_base.csv private.txt

To execute the client, Run the following command on your terminal window (Make sure public.txt is in the same folder with the script)

-> python3 client.py localhost <port_number> public.txt

Note I've used localhost assuming you're running both the scripts on the same machine. Do use the server's IP Address if you're running on a different machine.

Thank you!