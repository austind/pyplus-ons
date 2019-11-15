from pathlib import Path
import pytest
import subprocess

TEST_CASES = [
./day2/recap/solutions/exercise1.py
./day2/recap/solutions/exercise2.py
./day2/structure/solutions/exercise1.py
./day2/structure/solutions/exercise2.py
./day2/classes/solutions/exercise1.py
./day2/classes/solutions/exercise2.py
./day2/functions/solutions/exercise3.py
./day2/functions/solutions/exercise4.py
./day2/functions/solutions/exercise1.py
./day2/functions/solutions/exercise2.py
./day2/regex/solutions/exercise1_named_patterns.py
./day2/regex/solutions/exercise1.py
./day2/regex/solutions/exercise2.py
./day2/netmikox/solutions/exercise1.py
./day2/netmikox/solutions/exercise2.py
]


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_runner(test_case):
    path_obj = Path(test_case)
    python_script = path_obj.name
    script_dir = path_obj.parents[0]
    cmd_list = ["python", python_script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, script_dir)
    assert return_code == 0
    assert std_err == ""
