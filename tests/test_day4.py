from pathlib import Path
import pytest
import subprocess

TEST_CASES = [
    "../day4/subprocess/solutions/exercise1.py",
    "../day4/csv_excel/solutions/exercise1/exercise1.py",
    "../day4/csv_excel/solutions/exercise2/exercise2.py",
    "../day4/csv_excel/solutions/exercise3/exercise3.py",
#    "../day4/jinja/solutions/exercise2/exercise2.py",
#    "../day4/jinja/solutions/exercise1.py",
#    "../day4/jinja/solutions/exercise3/exercise3.py",
#    "../day4/slack/solutions/exercise1.py",
#    "../day4/slack/solutions/exercise2.py",
#    "../day4/napalmx/solutions/exercise3.py",
#    "../day4/napalmx/solutions/napalm_devices.py",
#    "../day4/napalmx/solutions/exercise1.py",
#    "../day4/napalmx/solutions/exercise2.py",
#    "../day4/concurrency/solutions/exercise3.py",
#    "../day4/concurrency/solutions/exercise1.py",
#    "../day4/concurrency/solutions/exercise2.py",
#    "../day4/testing/solutions/exercise1.py",
#    "../day4/testing/solutions/exercise2.py",
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
