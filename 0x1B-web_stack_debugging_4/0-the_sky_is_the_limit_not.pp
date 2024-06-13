#change request limit
exec { 'Change limit':
  command  => 'sudo echo -e "* hard nofile 2500\n* soft nofile 25000" > /etc/security/limits.conf',
  provider => shell,
}