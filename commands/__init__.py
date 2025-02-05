"""
Cogs package for EAP-Bot.
This allows dynamic loading of bot features.
"""
# commands/__init__.py
import os
import importlib

def load_commands(bot):
    """
    Auto-loads all command modules from the commands/ folder.
    """
    for filename in os.listdir(os.path.dirname(__file__)):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"commands.{filename[:-3]}"
            try:
                bot.load_extension(module_name)
                print(f"✅ Loaded: {module_name}")
            except Exception as e:
                print(f"❌ Failed to load {module_name}: {e}")
