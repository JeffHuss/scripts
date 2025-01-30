#! /bin/bash
# This script takes a flat JSON that's being indexed
# via the Bulk API and adds the index and document
# statements to every other line starting with the first.

IFS=$'\n'
x=0
a='{"index":{"_index":"ecommerce","_id":'
b='}}'
for i in $(cat ecommerce.json); do
	c="${a}${x}${b}"
	echo ${c} >> new-ecommerce.json
	echo ${i} >> new-ecommerce.json
	((x=x+1))
done
