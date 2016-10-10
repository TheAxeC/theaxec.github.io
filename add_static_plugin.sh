
dst="tags/"
prefix="_site/tags/"
for d in _site/tags/*/ ; do
	d=${d#$prefix}
	echo "$d"
	echo "cp -a ${prefix}${d} ${dst}${d}"
	cp -r ${prefix}${d} ${dst}${d}
done

dst="category/"
prefix="_site/category/"
for d in _site/category/*/ ; do
	d=${d#$prefix}
	echo "$d"
	echo "cp -a ${prefix}${d} ${dst}${d}"
	cp -r ${prefix}${d} ${dst}${d}
done