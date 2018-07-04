"""Run doubling experiments and 'Tada!' you get the time complexity"""

import sys
import perf

from tada.util import configuration
from tada.util import display
from tada.util import run
from tada.util import save

# Make available the package with functions-under-analysis
sys.path.insert(0, "/home/gkapfham/working/research/source/speed-surprises")

# TODO: the name of the experiment should be an argument
PERF_EXPERIMENT_NAME = "perf_mcopies_ofc"

if __name__ == "__main__":
    # setup parameters of a simple doubling experiment
    size = 100
    factor = 2
    size_stop = 100
    save.save_configuration(configuration.CONFIGURATION, size)
    # perform the small doubling experiment
    while size <= size_stop:
        # run the benchmark by using it through python
        display.display_start_message(size)
        current_output, current_error = run.run_command(
            configuration.PYTHON_EXEC
            + configuration.SPACE
            + PERF_EXPERIMENT_NAME
            + configuration.PYTHON_EXT
        )
        # display the standard output and error
        display.display_output(current_output.decode(configuration.UTF8))
        display.display_output(current_error.decode(configuration.UTF8))
        # read the JSON file containing the results
        current_benchmark = perf.Benchmark.load(
            configuration.RESULTS
            + configuration.SEPARATOR
            + PERF_EXPERIMENT_NAME
            + str(size)
            + configuration.JSON_EXT
        )
        # print('Values {0}'.format(current_benchmark.get_values()))
        print("Mean {0}".format(current_benchmark.mean()))
        print("Median {0}".format(current_benchmark.median()))
        display.display_end_message(size)
        # go to the next size for the doubling experiment
        size = size * 2
        # write the next doubling experiment size to the file
        save.save_configuration(configuration.CONFIGURATION, size)