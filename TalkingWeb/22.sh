cat << EOF | nc challenge.localhost 80
POST /gateway HTTP/1.1
Host: challenge.localhost:80
Content-Type: application/x-www-form-urlencoded
Content-Length: 75

credential=pasiwbej&auth_pass=wdqqixic&security_token=nerpziet&pin=wfujpuro

EOF
