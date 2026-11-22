This is the implementation of the fraud detection of Shamir's secret sharing scheme implemented by Python `3.14.10`. 
Which is required for my undergraduate thesis project. 

## How it works

## How to test this project

<details>
<summary> uv </summary>

Install `uv` first in your system. Inside project's directory, create and activate virtual environment and 
then install required packages by running:
```bash
uv venv                         # initialize .venv directory
source .venv/bin/activate       # activate the environment
uv init
uv add -r requirements.txt
```
you can deactivate the project environment by running
```bash
deactivate
```
</details>

<details>
<summary> nix </summary>

Install [Nix package manager](https://nixos.org/download/) to able to test this project. And then run this command below
```bash
nix develop -c $SHELL
```
</details>

Run the implementation by
```bash
python main.py
```
