You have override grappelli.min.js.
If you update grappelli, you should remodify the file.

The changes are simple:
sed -i.bak 's/delay:\([0-9]\+\)/delay:1/g' grappelli.min.js
sed -i.bak 's/minLength:\([0-9]\+\)/minLength:0/g' grappelli.min.js

Copy the updated grappelli.min.js into db/static/grappelli/js
and apply those commands. Or better: just one (prefered):

sed -i.bak -e 's/delay:\([0-9]\+\)/delay:1/g' -e 's/minLength:\([0-9]\+\)/minLength:0/g' grappelli.min.js


