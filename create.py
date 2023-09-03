import os, sys

# IF YOU WISH TO MODIFY, CREATE A TEMPLATE IN /templates/ AND ADD IT HERE
templates = ["python", "node.js"]

def main():
    try:
        os.system('clear')
        project_name = input("» Project Name? ")
        project_type = input("» Project Type (Python, Node.js)? ")

        if project_name:
            if project_type.lower() in templates:
                with open(f"templates/{project_type.lower()}.lzyc", "r") as template:
                    template_contents = template.read()

                if project_type.lower() == "python" and project_name+".py" in os.listdir("output/"):
                    print("Error! File already exists!")
                    raise Exception
                
                if project_type.lower() == "node.js" and project_name+".js" in os.listdir("output/"):
                    print("Error! File already exists!")
                    raise Exception

                if project_type.lower() == "python":
                    with open(f"output/{project_name}.py", "x") as project:
                        project.write(template_contents)
                elif project_type.lower() == "node.js":
                    with open(f"output/{project_name}.js", "x") as project:
                        project.write(template_contents)
                else:
                    print("Error! The project you wish to create does not have a template!")
                    raise Exception
    except Exception as Error:
        print("An error occured. Restart program?")
        print(f"({Error})")

        if input("[y/n]: ").lower() == "y":
            main()

if __name__ == "__main__":
    main()