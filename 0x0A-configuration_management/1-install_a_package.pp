# 1. Install flask 2.1.0 package 
package { 'Flask=2.1.0':
  ensure   => '2.1.0',
  provider => 'pip3',
}
