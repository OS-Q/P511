"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.

http://arduino.cc/en/Reference/HomePage
"""

from os.path import join

from SCons.Script import DefaultEnvironment, SConscript

env = DefaultEnvironment()
board = env.BoardConfig()
build_core = board.get("build.core", "").lower()

SConscript("_embed_files.py", exports="env")

if build_core == "mbcwb":
    SConscript(
        join(DefaultEnvironment().PioPlatform().get_package_dir(
            "A52B"), "tools", "esp-build.py"))

elif "idf" not in env.subst("$PIOFRAMEWORK"):
    SConscript(
        join(DefaultEnvironment().PioPlatform().get_package_dir(
            "A52A"), "tools", "build.py"))

elif "espidf" not in env.subst("$PIOFRAMEWORK"):
    SConscript(
        join(DefaultEnvironment().PioPlatform().get_package_dir(
            "framework-arduinoespressif32"), "tools", "platformio-build.py"))
