This is the implementation of the fraud detection of Shamir's secret sharing scheme implemented by Python `3.14.10`. 
Which is required for my undergraduate thesis project. 

## How it works

## How to setup this project

<details>
<summary> uv </summary>

Install `uv` first in your system. Inside project's directory, run this command: 
```bash
uv sync                         # syncing the dependencies
uv run main.py                  # run main.py script
```
</details>

<details>
<summary> nix </summary>

Install [Nix package manager](https://nixos.org/download/) to able to test this project. And then run this command below
```bash
nix develop -c $SHELL
```
</details>

## Thanks to
- Shamir secret scheme's implementation in [wikipedia](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing) for inspiring me 
  to write the implementation
