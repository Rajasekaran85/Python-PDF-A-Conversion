import os
import ghostscript

print("\n PDF to PDF/A Conversion \n")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 20 April 2022 \n\n")

# ghostscript package used
# Output: PDF/A - 1b conversion

filepath1 = input(" Enter the File path: ")

Output1 = input(" Enter the Output path: ")

output = Output1 + "\\"

filepath = filepath1 + "\\"

filelist = os.path.isdir(filepath) # specified path is an existing directory or not




# os.listdir = list the file list in the directory
for fname in os.listdir(filepath):
    print(fname)
    if not fname.endswith(".pdf"):
        continue
    path = os.path.join(filepath, fname) 
    print(path)
    
    #print(fname)
    #print(path)
    ghostScriptExec = ['gs', '-dPDFA', '-dBATCH', '-dNOPAUSE', '-dUseCIEColor', '-sProcessColorModel=DeviceRGB',
                   '-sDEVICE=pdfwrite', '-dFastWebView', '-sPDFACompatibilityPolicy=1',
                   '-sOutputFile='+ output + 'PDFA-' + fname, path]
    ghostscript.Ghostscript(*ghostScriptExec)
    #print(filepath)
print("\n Conversion Completed\n")

