#  2. Execute pkill killmenow command
exec {'pkill -f killmenow'
  path    => ['/usr/bin', '/usr/sbin',];
}
