#  2. Add a custom HTTP header with Puppet 
class nginx_setup {
  
  exec {'sudo apt update':
    path    => ['/usr/bin', '/usr/sbin',];
  }

  package { 'nginx':
    ensure => installed,
    before => File['/etc/nginx/sites-available/default'],
  }

  file { ['/var/www/html', '/var/www/error']:
    ensure => directory,
    mode   => '0755',
  }

  file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!',
  }

  file { '/var/www/html/404.html':
    ensure  => present,
    content => "Ceci n'est pas une page",
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "
      server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        add_header X-Served-By \\$hostname;
        location / {
          try_files \\$uri \\$uri/ =404;
        }
        if (\\$request_filename ~ redirect_me){
        rewrite ^ https://thedreamcatcher.dev permanent;
        }
        error_page 404 /404.html;
        
        
        location = /404.html {
          internal;
        }
      }
    ",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }

}

# Kame Hame HAAAAAAAAAAAAAAAAAAA
include nginx_setup
