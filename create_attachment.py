def copy():
    fp = open("attachment.py", "r")
    fp2 = open("copy_attachment.py", "w")
    fp2.write(fp.read())
    fp.close()
    fp2.close()

if __name__ == "__main__":
    copy()