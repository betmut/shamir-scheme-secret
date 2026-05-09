{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-25.11";
  };

  outputs = inputs@{ self, nixpkgs, ...}:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
  in
  {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        #for ASCII art
        figlet
        lolcat

        python313

        #python packages
        python313Packages.numpy
      ];

      shellHook = ''
        export PS1="\[\033[1;34m\](nix-dev) \[\033[1;32m\]\u@\h\[\033[00m\] $ "

        figlet "Skripsi" | lolcat
        echo -e "\033[1;31mJudul  :\033[0m Deteksi dan Identifikasi Kecurangan Pembagian Rahasia Linear Berbasis Skema Shamir"
        echo -e "\033[1;31mAuthor :\033[0m Mathew Elhans"
        echo " "
        echo -e "\033[1;33mProject Status:\033[0m"
        echo "-----------------------------------------------------"
        echo "Python version  : $(python --version)"
        echo "Packages        : numpy"
        echo "Git Branch      : $(git branch --show-current)"
        echo "Last Commit     : $(git log -1 --format=%s)"
        echo "-----------------------------------------------------"
      '';
    };
  };
}
