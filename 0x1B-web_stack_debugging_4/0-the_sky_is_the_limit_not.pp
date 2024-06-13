#change request limit
exec { 'Change limit':
    command  => 'echo "ULIMIT=\"-n 25000\"" > /etc/default/nginx && sudo service nginx restart',
    provider => shell,
}