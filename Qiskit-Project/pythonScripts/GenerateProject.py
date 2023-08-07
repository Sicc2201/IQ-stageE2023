import argparse
import jstyleson as json
import os

def main():

    parser = argparse.ArgumentParser(add_help=True, description="This is a project dependencies generator. It create a templates for inputs and create dependencies. It generates a modules folder, a folder to put the qasm files, a main project python file template and a JSON input file template.")
    parser.add_argument('projectName', type=str, help="The name of your project.")
    parser.add_argument('-b', "--backend", type=str, help="Set a backend when creating the JSON input file template (default = ibm_perth)")
    parser.add_argument('-q', "--nqubits", type=int, help="Set number of qubits participants will have when creating the JSON input file template (default = 1)")
    args = parser.parse_args()

    if len(vars(args)) < 2:
        print("choose a name for your project as argument")
        parser.print_usage()
    else:

        curr = os.getcwd()
        imagesFolder = curr + "/Images"
        resultsFolder = curr + "/Results"
        qasmOutputFolder = curr + "/Qasm_output"
        mainFile = curr + "/PythonScripts/" + args.projectName + ".py"
        scriptsFolder = curr + "/PythonScripts/" + args.projectName + "_modules"
        qasmFolder = curr + "/QasmFiles/" + args.projectName
        jsonFile = curr + "/JsonFiles/" + args.projectName + "_input.JSON"

        # create empty directories for the project if needed
        if not os.path.exists(imagesFolder):
            os.makedirs(imagesFolder)
        if not os.path.exists(resultsFolder):
            os.makedirs(resultsFolder)
        if not os.path.exists(qasmOutputFolder):
            os.makedirs(qasmOutputFolder)
        if not os.path.exists(scriptsFolder):
            os.makedirs(scriptsFolder)
        if not os.path.exists(qasmFolder):
            os.makedirs(qasmFolder)
            os.makedirs(qasmFolder + "/participants")
            os.makedirs(qasmFolder + "/communication")

        # create the json file as input based on the template
        if not os.path.isfile(jsonFile):
            with open(jsonFile, "w") as newFile, open(curr + "/jsonFiles/template.JSON", "r") as template:
                for line in template:
                    newFile.write(line)

            if args.backend:
                with open(jsonFile, "r") as f:
                    jsfile = json.load(f)
                jsfile["backend"] = args.backend
                newjs = json.dumps(jsfile, indent=4)
                with open(jsonFile, "w") as f:
                    f.write(newjs)

            if args.nqubits:
                with open(jsonFile, "r") as f:
                    jsfile = json.load(f)
                for p in jsfile["participants"]:
                    p["nqubits"] = args.nqubits
                newjs = json.dumps(jsfile, indent=4)
                with open(jsonFile, "w") as f:
                    f.write(newjs)

        # create the main file to execute based on the template
        if not os.path.isfile(mainFile):   
            with open(mainFile, "w") as newFile, open(curr + "/pythonScripts/template.py", "r") as template:
                for line in template:
                    newFile.write(line)    

if __name__ == "__main__":
    main()
