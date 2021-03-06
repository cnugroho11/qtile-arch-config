# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import psutil
import os
import subprocess

from libqtile import hook
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()


colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"],
          ["#6272a4", "#6272a4"],
          ["#413c69", "#413c69"]]

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    
    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    Key([mod], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
 

    # Floating keybinding
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod, "shift"], "m", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),


    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+")),

    # Screen
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),


    # App keybinding
    Key([mod], "p", lazy.spawn("j4-dmenu-desktop"), desc="Show dmenu"),
    Key([mod, "shift"], "p", lazy.spawn("dmenu_run"), desc="Show dmenu"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Thunar file manager"),
    Key([], "Print", lazy.spawn("scrot '/home/cnugroho/Pictures/Screenshot/Screenshot_%Y%m%d-%H%M%S.png'")),
    Key([mod], "F1", lazy.spawn("brave"), desc="Brave browser"),
    Key([mod], "F2", lazy.spawn("code"), desc="Visual Studio Code"),
    Key([mod], "F3", lazy.spawn("telegram-desktop"), desc="Telegram Desktop"),

    # Rofi keybinding
    Key([mod], "d", lazy.spawn(".config/rofi/launchers/ribbon/launcher.sh"), desc="Show launcher"),
    Key([mod], "x", lazy.spawn(".config/rofi/powermenu/powermenu.sh"), desc="Show pewermenu"),

]

groups = [
     Group('www'),
     Group('code', matches=[Match(wm_class=["code"])]),
     Group('term'),
     Group('file'),
     Group('docs', matches=[Match(wm_class=["libreoffice", "libreoffice-writer", "libreoffice-impress", "libreoffice-calc", "xreader"])]),
     Group('view', matches=[Match(wm_class=["feh"])]),
     Group('disc', matches=[Match(wm_class=["discord"])]),
     Group('spot', matches=[Match(wm_class=["spotify"])]),
     Group('tele', matches=[Match(wm_class=["telegram-desktop"])])
]

for index, grp in enumerate(groups):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(index+1), lazy.group[grp.name].toscreen(),
            desc="Switch to group {}".format(grp.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(index+1), lazy.window.togroup(grp.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(grp.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


layout_theme = {"border_width": 4,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }


layouts = [
    layout.MonadTall(**layout_theme),
    #layout.Tile(**layout_theme),
    #layout.Columns(border_focus_stack='#d75f5f'),
    #layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    #layout.MonadWide(**layout_theme),
    # layout.RatioTile(), 
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='FiraCode Nerd Font Mono',
    fontsize=15,
    padding=3,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(
                #    foreground = colors[2],
                #    background = colors[4],
                #    padding = 5
                #),
                widget.GroupBox(
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 0,
                    padding_x = 3,
                    borderwidth = 3,
                    active = colors[3],
                    inactive = colors[2],
                    rounded = False,
                    highlight_color = colors[1],
                    highlight_method = "line",
                    this_current_screen_border = colors[6],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[6],
                    other_screen_border = colors[4],
                    foreground = colors[2],
                    background = colors[0]
                ),
                #widget.Sep(
                #    linewidth = 0,
                #    padding = 40,
                #    foreground = colors[2],
                #    background = colors[0]
                #),
                widget.WindowName(
                    max_chars = 65,
                    background = colors[0],
                    foreground = 'ffb86c',
                    padding = 10
                ),
                #widget.Spacer(
                #    background = colors[0]
                #),
                #widget.Sep(
                #    linewidth = 0,
                #    padding = 40,
                #    foreground = colors[2],
                #    background = colors[0]
                #),
                #widget.Chord(
                #    chords_colors={
                #        'launch': ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                widget.TextBox(
                    text = " ???",
                    foreground = colors[2],
                    background = colors[4],
                    padding = 0
                ),
                widget.Volume(
                    background = colors[4],
                    padding = 10
                ),
                widget.CPU(
                    format = '??? {freq_current}GHz {load_percent}%',
                    background = colors[5],
                    padding = 10
                ),
                widget.TextBox(
                    text = "???",
                    background = colors[5],
                ),
                widget.Memory(
                    format = '{MemUsed:.0f}M',
                    background = colors[5],
                    padding = 10
                ),  
                widget.TextBox(
                    text = " ???",
                    foreground = colors[2],
                    background = colors[4],
                    padding = 0
                ),
                widget.Battery(
                    format = '{char} {percent:2.0%}',
                    background = colors[4],
                    padding = 10
                ),
                widget.Net(
                    format = '??? {down} ?????? {up}',
                    background = colors[5],
                    padding = 10
                ),
                widget.Clock(
                    foreground = colors[2],
                    background = colors[4],
                    format = "%a, %b %d - %H:%M",
                    padding = 10
                ),
                widget.Systray(
                    background = colors[0],
                    padding = 5
                ),

                #widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),
        Match(wm_class='telegram-desktop'),  # GPG key password entry
    ],**layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
