# 1. Install flask 2.1.0 package 
package { 'pip install flask':
  provider => 'pip3',
  require  => Package['python-pip']
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
