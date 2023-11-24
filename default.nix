# default.nix

{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [ pkgs.poetry pkgs.qt6.full pkgs.python310Packages.pyqt6 ];
}
