# 1. Install flask 2.1.0 package 
exec { 'install_flask_and_dependencies':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.1.1',
  path    => '/usr/bin',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0" && /usr/bin/pip3 show werkzeug | grep -q "Version: 2.1.1"',
}
