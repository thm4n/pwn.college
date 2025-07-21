#!/bin/bash

function push() {
    scp_flags="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
    if [[ "$3" == *.sh ]]; then
        dest_file="try.sh"
    elif [[ "$3" == *.py ]]; then
        dest_file="try.py"
    elif [[ -d "./$2/$3" ]]; then
        dest_file="try"
        scp_flags="-r ${scp_flags}"
    else
        echo "$3 is not a .sh or .py file."
        exit 1
    fi

    scp -i ~/.ssh/id_rsa ${scp_flags} ./$2/$3 hacker@pwn.college:/home/hacker/${dest_file}
}

function solve() {
    if [[ "$3" == *.sh ]]; then
        command="chmod +x ./try.sh ; ./try.sh"
        dest_file="try.sh"
    elif [[ "$3" == *.py ]]; then
        command="python try.py"
        dest_file="try.py"
    elif [[ -d "./$2/$3" ]]; then
        command="python ./try/solution.py \`find /challenge -name 'baby*'\`"
    else
        echo "$3 is not a .sh or .py file."
        exit 1
    fi
    ssh -i ~/.ssh/id_rsa hacker@pwn.college "cd /home/hacker ; ${command} ; rm -rf /home/hacker/${dest_file}"
}

function fetch() {
    mkdir -p $2/$3
    scp -i ~/.ssh/id_rsa hacker@pwn.college:/challenge/* ./$2/$3 
}

case "$1" in
    "solve")
        push $@
        solve $@
        ;;
    "fetch")
        fetch $@
        ;;
    *)
        echo "Usage: $0 {solve|push}"
        exit 1
        ;;
esac
