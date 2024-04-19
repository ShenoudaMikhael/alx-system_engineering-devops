#  2. Execute pkill killmenow command
exec {'pkill-killmenow'
  command => 'pkill -f killmenow'
  path    => ['/usr/bin', '/usr/sbin',];
}
