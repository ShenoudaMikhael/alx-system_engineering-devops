#  2. Add a custom HTTP header with Puppet 
class nginx_setup {
  
  exec {'sudo apt update':
    path    => ['/usr/bin', '/usr/sbin',];
  }
  exec {'sudo apt install -y nginx':
    path    => ['/usr/bin', '/usr/sbin',];
  }

  file_line { 'http_header':
    path  => '/etc/nginx/nginx.conf',
    match => 'http {',
    line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  }
  exec {'service nginx restart':
    path  => ['/usr/bin', '/usr/sbin',]
  }



}

# Kame Hame HAAAAAAAAAAAAAAAAAAA
include nginx_setup

