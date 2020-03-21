# covid19-hospital-scheduler

## Usage and arguments

Call main.py to run a simulation.
You need to pass the following arguments:

### Necessary arguments

scenario: Choose from options `"worst","high","normal"`

Defines the scenario for which the simulation is run.

Usage example: `python main.py worst`

### Optional arguments

-visualize: Default is `False`

You can turn on/off visualization using this switch. To enable visualization use:

`python main.py normal -visualize=True`

-output: Default is `True`

You can turn on/off output with this switch. Usage example:

`python main.py normal -output=True`
