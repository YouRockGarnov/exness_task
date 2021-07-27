The solution of the interview task

* To run tests run /app/pytest_main.py
* To run the server use this instruction https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04-ru


For concurrent execution use --workers and --threads options 

For example:  
"uwsgi --workers <workers> --threads <threads> --socket <ip_address>:<port> --protocol=http",
  where <ip_address> is the ip address of the server, <port> is the port to which signals will be sent, <workers> is the number of processes, I recommend putting the same number of cores on the server, <threads> is the number of threads, similarly.