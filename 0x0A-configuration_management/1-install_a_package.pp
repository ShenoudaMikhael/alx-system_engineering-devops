# 1. Install flask 2.1.0 package 
package { 'flask==2.1.0':
  ensure => 'installed',
  provider => 'pip3',

}
