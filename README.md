# Qtile config

This is my qtile config i usually use.

![Qtile Screenshot](https://github.com/cnugroho11/qtile-arch-config/blob/master/screenshot/qtile.png)

## Installation

Arch

```bash
pacman -S qtile
pacman -S python-pip
pacman -S i3lock
pacman -S rofi

pip install psutil
# or
pacman -S python-psutil 
```
For rofi theme
https://github.com/adi1090x/rofi.git

## Usage

```bash
git clone https://github.com/cnugroho11/qtile-arch-config.git
cd qtile-arch-config

cp config.py ~/.config/qtile/

# only if you use xorg-xinit
cp .xinitrc ~/
startx
```

