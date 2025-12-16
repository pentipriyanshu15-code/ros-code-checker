import zipfile, os, ast, json, re, shutil

SAFE_MIN = -3.14
SAFE_MAX = 3.14

def extract_zip(zip_path):
    if os.path.exists("extracted"):
        shutil.rmtree("extracted")
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall("extracted")
    return "extracted"

def syntax_check(file):
    try:
        ast.parse(open(file).read())
        return "OK"
    except Exception as e:
        return str(e)

def ros_checks(code):
    errors = []
    if "rospy.init_node" not in code:
        errors.append("Missing init_node")
    if "Publisher" not in code and "Subscriber" not in code:
        errors.append("No Publisher/Subscriber")
    return errors

def safety_checks(code):
    warn = []
    joints = re.findall(r"\[([0-9\.,\-\s]+)\]", code)
    for j in joints:
        for v in j.split(","):
            try:
                f = float(v)
                if f < SAFE_MIN or f > SAFE_MAX:
                    warn.append("Joint out of safe range")
            except:
                pass
    if "sleep" not in code:
        warn.append("No sleep in loop")
    return warn

def run(zip_path):
    report = []
    path = extract_zip(zip_path)
    for r,_,f in os.walk(path):
        for file in f:
            if file.endswith(".py"):
                p = os.path.join(r,file)
                code = open(p).read()
                report.append({
                    "file": file,
                    "syntax": syntax_check(p),
                    "ros": ros_checks(code),
                    "safety": safety_checks(code)
                })
    json.dump(report, open("report.json","w"), indent=4)
    open("report.txt","w").write(json.dumps(report,indent=4))
    return report

if __name__ == "__main__":
    zp = input("Enter ZIP path: ")
    print(run(zp))

