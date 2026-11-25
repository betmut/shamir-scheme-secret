{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-26.05";
  };

  outputs = { self, nixpkgs, ...}:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
  in
  {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        # for ASCII art
        figlet
        lolcat

	# Python Interpreter
        python314

        # python packages
        python314Packages.uv
	python314Packages.pytest
	python314Packages.seaborn
      ];

      shellHook = ''
        export PS1="\[\033[1;34m\](nix-dev) \[\033[1;32m\]\u@\h\[\033[00m\] $ "

        figlet "Shamir" | lolcat
        echo -e "\033[1;31mJudul  :\033[0m Deteksi dan Identifikasi Kecurangan Pembagian Rahasia Linear Berbasis Skema Shamir"
        echo -e "\033[1;31mAuthor :\033[0m Mathew Elhans"
        echo " "
        echo -e "\033[1;33mProject Status:\033[0m"
        echo "-----------------------------------------------------"
        echo "Python version  : $(python --version)"
        echo "Packages        : $(python metadata.py)"
        echo "Git Branch      : $(git branch --show-current)"
        echo "Last Commit     : $(git log -1 --format=%s)"
        echo "-----------------------------------------------------"
      '';
    };
  };
}
