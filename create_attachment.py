def copy_attachment():
    fp = open("attachment_file.py", "r")
    fp2 = open("attachment.py", "w")
    fp2.write(fp.read())
    fp.close()
    fp2.close()
    print("attachment copied")