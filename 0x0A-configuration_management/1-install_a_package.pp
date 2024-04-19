# 1. Install flask 2.1.0 package 
exec { 'pip3 install flask==2.1.0':
  command =>  'pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/usr/sbin',];
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',

}
