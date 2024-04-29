#  2. Add a custom HTTP header with Puppet 
class nginx_setup {
  
  exec {'apt_update':
    command => '/usr/bin/apt-get update',
  }

  package { 'nginx':
    ensure => installed,
    before => File['/etc/nginx/sites-available/default'],
  }

  file_line { 'http_header':
    path  => '/etc/nginx/nginx.conf',
    match => 'http {',
    line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  }
  exec {'start_service':
    command => '/usr/sbin/service nginx start',
  }



}

# Kame Hame HAAAAAAAAAAAAAAAAAAA
include nginx_setup
