
for file in '/data/Twitter dataset/'geoTwitter20-01*.zip; do
	echo "running file $file"
	$(./src/map.py --input_path="$file")
	echo "finish running file"
done
