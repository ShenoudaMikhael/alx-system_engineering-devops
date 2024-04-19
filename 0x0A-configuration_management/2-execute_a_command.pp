#  2. Execute a command
exec {'pkill-killmenow'
  command => 'pkill killmenow'
  path    => ['/usr/bin', '/usr/sbin',],
}
