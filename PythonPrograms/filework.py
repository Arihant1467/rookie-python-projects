fh=open("mbox.txt","r")
fn=open("m-box.txt","w")
for line in fh:
    fn.write(line)
fh.close()
fn.close()