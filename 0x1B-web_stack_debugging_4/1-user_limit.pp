# Remove holberton user file limits
exec { 'Remove Limits':
  command  => '/usr/bin/env sed -i /holberton/d /etc/security/limits.conf',
}
