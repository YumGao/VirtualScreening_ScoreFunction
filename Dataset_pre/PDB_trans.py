import os
import glob
#prepare the output path for converted files
data_dir = './Docked_PDBQTs_receptors/'
result_dir = './Docked_PDBs_receptors/'
if not os.path.exists(result_dir):
    os.makedirs(result_dir)
cmds = ""
data_file_path = data_dir + "*_receptor.pdbqt"
data_files = glob.glob(data_file_path)

for fr_f in data_files:
    cn_f = result_dir + fr_f.split("/")[-1].replace("pdbqt","pdb")
    cmd = "load "+ fr_f + ";save " + cn_f + ";delete all;\n"
    cmds = cmds + cmd        
#print(cmds)

#write the .pml file with pymol command for SDF conversion   
f = open("PDB_trans.pml","w")
f.write(cmds)
f.close()
