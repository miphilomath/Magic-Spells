cnt=1

for file in `ls *.jpg` ; do
	mv ${file} ${cnt}."jpg"
	cnt=$(( cnt +1 ))
done
