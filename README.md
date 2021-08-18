# Wallger: The Wallpaper Changer

![CodeQL](https://github.com/UltiRequiem/wallger/workflows/CodeQL/badge.svg)
![Pylint](https://github.com/UltiRequiem/wallger/workflows/Pylint/badge.svg)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/wallger)](https://pypi.org/project/wallger)
![Repo Size](https://img.shields.io/github/repo-size/ultirequiem/wallger?style=flat-square&label=Repo)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Lines of Code](https://img.shields.io/tokei/lines/github.com/UltiRequiem/wallger?color=blue&label=Total%20Lines)

https://user-images.githubusercontent.com/71897736/129631224-d4f00320-265c-4514-9086-a01b26cfdfd2.mp4

## Install

You can install [Wallger](https://pypi.org/project/wallger) from PyPI like
any other package:

```bash
pip install wallger
```

To get the last version:

```bash
pip install git+https:/github.com/UltiRequiem/wallger
```

If you use Linux, you may need to install this with sudo to
be able to access the command throughout your system.

## Example Config

This configuration goes in `~/.config/wallger/config.json`:

```json
{
  "resolution": [1600, 900],
  "provider": "wallhaven",
  "path": "/home/zero/disk/sabare/wallger",
  "topic": "anime",
  "tool": "feh",
  "nsfw": false
}
```

- Resolution: The resolution of you monitor
- Provider: It can be Wallhaven or Unsplash
- Path: Where to save the images
- Topic: The topic (Eg. "Math", "Code Geass", "Mirai Nikki")
- Tool: The tool to change the Wallpaper. Options = ["feh","gnome","mate","kde"]
- NSFW: No safe for work

There are not default values.

### License

Wallger is licensed under the [MIT License](./LICENSE).
