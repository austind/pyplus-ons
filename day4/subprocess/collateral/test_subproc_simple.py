import subprocess


def subprocess_wrapper(cmd_list):
    """Wrapper to execute subprocess including byte to UTF-8 conversion."""
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


cmd_list = ["ls", "-a", "-l"]
std_out, std_err, return_code = subprocess_wrapper(cmd_list)
print()
print(f"Return Code: {return_code}")
print(std_out)
print()
