# Qtile config

This is my qtile config i usually use.

## Installation

Arch

```bash
pacman -S qtile
pacman -S pip

pip install psutil
# or
pacman -S python-psutil 
```

## Usage

```bash
git clone https://github.com/cnugroho11/qtile-arch-config.git
cd qtile-arch-config

cp config.py ~/.config/qtile/

# only if you use xorg-xinit
cp .xinitrc ~/
startx
```

