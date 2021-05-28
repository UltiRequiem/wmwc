import json
from importlib import import_module
from os.path import expanduser

from wmwc.providers.provider import Provider


def get_config_file():
    try:
        with open(expanduser("~/.config/wm-wallpaper-changer/config.json"),'r') as json_data:
            return  json.load(json_data)
    except FileNotFoundError:
        print("No config") #TODO: Add more documentation


def get_config(secction, option):
    json_data = get_config_file()
    try:
        return json_data[secction][option]
    except:
        return "none"


def generate_class(options, url, filename):
    return Provider(
        options["monitor_long"],
        options["monitor_height"],
        options["topic"],
        options["save"],
        url,
        filename,
        options["system"],

    )


def dynamic_import(module):
    try:
        return import_module(module)
    except ImportError as error:
        print(f"Oops {error} ocurred.")



def set_image(options):
    provider = options["provider"]
    if provider ==  "wallhaven":
        from wmwc.providers.wallhaven import run
        run(options)
    if provider == "unsplash":
        from wmwc.providers.unsplash import run
        run(options)
    if provider == "local":
        from wmwc.providers.local import run
        run(options)
