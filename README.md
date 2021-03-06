@Hackathon #WirvsVirus Jury: Our submission (as of Sunday 23:59) can be found in the branch "hackathon-submission".

# covid19-ventilator-optimization

Codebase for the VentilatorOptimizationVsVirus project of the WirvsVirus Hackathon.

The core functionality of this project is a scheduling algorithm that assigns incoming patient requests to hospitals that have reasonable capacities left. Furthermore we have functionalities to generate arbitrary datasets, simulate different schedulers on generated instances, and visualize simulation results.

## Usage and arguments

Call generate_data.py for generating your personal dataset.

Call main.py to run a simulation.
You can pass the following arguments:

### Optional arguments

-visualize: Default is `False`

You can turn on/off visualization using this switch. To enable visualization use:

`python main.py -visualize=True`

-output: Default is `True`

You can turn on/off output with this switch. Usage example:

`python main.py -output=True`

## What to expect

Simulations of our algorithm for scheduling patients to hospital beds. Yellow and green colors are favorable hospital capacities (indicating a balanced distribution of patients in need of ventilation over hospitals), whereas red hospitals symbolize overburdened hospitals.

### Our Optimization Algorithm

![Our Optimization Algorithm](https://raw.githubusercontent.com/jp172/covid19-ventilator-optimization/master/data/vis-output/with-optimization.png)

### Benchmark

![Benchmark](https://raw.githubusercontent.com/jp172/covid19-ventilator-optimization/master/data/vis-output/without-optimization.png)


