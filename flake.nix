{
  description = "Motion Canvas Project";

  inputs = 
    {
      nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    };

  outputs = { self, nixpkgs, ...}@inputs:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in
  {
    devShells.${system}.default = 
		pkgs.mkShell 
		{
    	nativeBuildInputs = with pkgs; [
        python3
    	];

    	shellHook = ''
       	echo -e "Dev shell opened with success!\nHave a great developing!"
      '';
    };
  };
}
