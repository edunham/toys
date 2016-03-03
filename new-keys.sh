ips=(
"123.45.678.90"
"123.45.678.91"
)

for ip in "${ips[@]}"
do
    ssh-keygen -f ~/.ssh/known_hosts -R $ip
    ssh-keyscan -H $ip >> ~/.ssh/known_hosts
done
