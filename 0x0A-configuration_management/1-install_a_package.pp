# 1. Install flask 2.1.0 package 
exec { 'install flask':
  command =>  'pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/usr/sbin',];
  unless  =>  'pip3 list | grep flask',
}
