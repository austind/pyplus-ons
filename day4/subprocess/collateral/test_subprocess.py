import subprocess

cmd_list = ["ls", "-a", "-l"]
proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
std_out, std_err = proc.communicate()
(std_out, std_err) = (std_out.decode(), std_err.decode())

print(std_out)
print(std_err)
