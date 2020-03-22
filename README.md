# covid19-ventilator-optimization

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

Simulations of our Algorithm for scheduling patients to hospital beds.

### Our Optimization Algorithm

![Our Optimization Algorithm](https://raw.githubusercontent.com/jp172/covid19-ventilator-optimization/master/data/vis-output/with-optimization.png)

### Benchmark

![Benchmark](https://raw.githubusercontent.com/jp172/covid19-ventilator-optimization/master/data/vis-output/without-optimization.png)


