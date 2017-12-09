# Ansible Role: Nexcess SCL PHP

Installs Remi's SCL PHP Version(s).  By default this role only installs the CLI version of PHP. PHP 7.1 is the current default version of PHP installed by this role, but you can override via 'php_prefix'.  FPM options are available (see Role Variables below).

## Role Variables

See `defaults/main.yml`.

## Dependencies

- https://github.com/nexcess/ansible-role-repo-remi

## Add to Requirements

    - src: https://github.com/nexcess/ansible-role-php.git
      name: nexcess.php

## Example Playbook

    - hosts: php_hosts
      roles:
        - nexcess.php

## License

MIT
