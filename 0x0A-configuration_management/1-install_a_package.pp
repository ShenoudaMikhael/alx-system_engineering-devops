# 1. Install flask 2.1.0 package 
package { 'flask==2.1.0':
  ensure   => present,
  provider => 'pip3',
  require  => Package['python-pip']
}
