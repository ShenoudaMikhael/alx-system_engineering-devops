#  SSH configuration file so that you can connect to a server without typing a password.
file_line { 'IdentityFile_.ssh/school':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
}

file_line { 'PasswordAuthentication_no':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}
