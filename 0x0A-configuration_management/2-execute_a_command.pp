#  2. Execute a command
exec {'pkillkillmenow'
  command => 'pkill killmenow'
  path    => ['/usr/bin', '/usr/sbin',],
}
