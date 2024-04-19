# 1. Install flask 2.1.0 package 
exec { 'pip3 install flask==2.1.0':
  path    => ['/usr/bin', '/usr/sbin',];
}
