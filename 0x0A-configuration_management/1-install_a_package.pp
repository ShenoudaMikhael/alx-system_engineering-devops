# 1. Install flask 2.1.0 package 
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
