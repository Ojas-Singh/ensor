rname=filename.strip(".pdb")+"_p_"+str(p)+str(datetime.datetime.now())+'.log'
r = open("data/"+rname, "a")
            
r.write("This DATA is generated on "+str(datetime.datetime.now())+"\n")
r.write("  ______ _   _  _____  ____  _____   "+"\n")
r.write(" |  ____| \ | |/ ____|/ __ \|  __ \  "+"\n")
r.write(" | |__  |  \| | (___ | |  | | |__) | "+"\n")
r.write(" |  __| | . ` |\___ \| |  | |  _  /  "+"\n")
r.write(" | |____| |\  |____) | |__| | | \ \  "+"\n")
r.write(" |______|_| \_|_____/ \____/|_|  \_\ "+"\n")
r.write("                                     "+"\n")
r.write("https://github.com/Ojas-Singh/ensor  "+"\n")
r.write("                                     "+"\n")
r.write("Molecule "+filename.strip(".pdb")+"\n")
r.write("System arg passed on the run."+"\n")
r.write("   "+str(sys.argv)+"\n")
while True:
    try:
        r.write("Calculated Energy : "+str(totE)+"\n")
        r.write("Time taken by ENSOR : "+ str(tfinal-t0)+"\n")
        break
    except ValueError:
        print("Oops! Try again with -g09 option to generate Valid log.")
r.close()