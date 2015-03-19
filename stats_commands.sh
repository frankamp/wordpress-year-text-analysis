find ./poems -type f -name "*.txt" -print | xargs wc
find ./poems -type f -name "*.txt" -exec ./analyze.sh {} \;
