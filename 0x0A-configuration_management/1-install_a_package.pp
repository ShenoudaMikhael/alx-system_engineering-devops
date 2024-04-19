# 1. Install flask 2.1.0 package 
package { 'pip3 install flask':
  provider => 'pip3',
  require  => Package['python3-pip']
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
