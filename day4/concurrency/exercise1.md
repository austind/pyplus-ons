# Concurrency Exercise 1

1. Write a simple function that accepts a "dev" dictionary (dictionary with Netmiko connetion information) and a "cmd" string to execute on the device. Return the output of the command from the function.
2. Using concurrent futures ThreadPoolExecutor, spawn threads to execute 'show ip arp' on two Cisco routers (cisco3.lasthop.io and cisco4.lasthop.io), and two Arista switches (arista1.lasthop.io and arista2.lasthop.io).
3. Wait until all threads are completed, then iterate through the threads and print the result.
