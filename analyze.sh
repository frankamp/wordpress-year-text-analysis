echo "running on $1"
cat $1 | python rid.py > ./analysis/$1
