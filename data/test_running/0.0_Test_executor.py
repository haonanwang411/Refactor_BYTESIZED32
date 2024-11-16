import argparse
import subprocess
from command_runner import get_commands  # 导入获取命令的函数 Import the function that gets the command
# 用于playthroughs命令传到游戏文件里，直接在Terminal运行
# The playthroughs command is uploaded to the game files and runs directly in Terminal
# 执行
def execute_commands(commands, script_name):
    # 将所有命令合并为一个字符串，并用换行符分隔 Combine all commands into a single string, separated by a newline
    commands_str = "\n".join(command.strip() for command in commands)
    print(f"--------------Executing combined command--------------\n{commands_str}")
    subprocess.run(["python", script_name, commands_str], check=True)
# 直接输入游戏名 Enter the game name directly
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute commands from a playthrough file for a specified script.")
    parser.add_argument("game_name", help="The Python script to run (e.g., 'bath-tub-water-temperature.py').")
# 添加控制参数，python用于命令行控制运行，当path变得越来越多
    # Add control parameters, python is used for command line control running, as path becomes more and more numerous
    args = parser.parse_args()
    file_path = f"../playthroughs/{args.game_name}-playthrough.txt"
    # 从指定的文件路径加载命令 Load the command from the specified file path
    commands = get_commands(file_path)
    # 执行指定的脚本并传入命令 执行指定的脚本并传入命令 Execute the specified script and pass the command Execute the specified script and pass the command
    execute_commands(commands, args.game_name+".py")


# python 0.0_Test_executor.py balance-scale-heaviest