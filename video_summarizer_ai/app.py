import subprocess
from dotenv import dotenv_values
from ui.interface import build_interface

if __name__ == "__main__":
    env_vars = dotenv_values(".env")

    for key, value in env_vars.items():
        subprocess.run(f'export {key}="{value}"', shell=True)

    demo = build_interface()
    demo.launch()