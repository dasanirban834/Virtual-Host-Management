:: SELF LEARNING ::\

// How to get last git Hash id? ::>> git rev-list HEAD | head -1\
// Fetch he file name of last hash id/commit id ::>> git diff-tree --no-commit-id --name-only -r $Last_Hash_id\
{ 
    "Servers": [
        "x",
        "y",
        "z"
    ]
}\

// How to get values of "Servers" ::>> jq . start.json | jq .Servers\
// Length of "Servers" ::>> jq . start.json | jq '.Servers | length'\
// Want to reove quotes from the instance ids ::>> jq . start.json | jq .Servers[0] | sed 's/"//g'\
// If we want any certain file to trigger gitlab ci file, use below keywords.\
only:
        changes:
            - start.json\
