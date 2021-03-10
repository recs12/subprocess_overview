import subprocess

def myCmd(item, cmd):
    try:
        s = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(s.args)
        print(s.check_returncode())
        # print(s.stdout.decode()) # when text=False
        print(s.stdout)
        print(s.stderr)
    except subprocess.CalledProcessError as c:
        with open("log.txt","a") as l:
            l.write(f"Failure item: {item}\n")
        return

for i, item in enumerate(["di","dir","di"]):
    myCmd(i, item)