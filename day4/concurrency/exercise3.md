# Concurrency Exercise 3

1. Using the function you wrote in the previous exercises, spawn threads using the concurrent futures ThreadPoolExecutor to execute the "show ip arp" command against the same set of devices (cisco3.lasthop.io, cisco4.lasthop.io, arista1.lasthop.io, arista2.lasthop.io).
2. Ensure that all threads are completed before printing out the result from each thread. Do this WITHOUT using the `wait` function (hint: use a context manager!).
