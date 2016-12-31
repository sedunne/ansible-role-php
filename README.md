# Ansible Role: Nexcess SCL PHP

Installs Necxess' SCL PHP Version(s).  By default this role only installs the CLI version of PHP.  FPM options are available (see Role Variables below).

## Role Variables

See `defaults/main.yml`.

## Dependencies

- https://github.com/nexcess/ansible-role-repo-nexcess

## Add to Requirements

    - src: https://github.com/nexcess/ansible-role-php.git
      name: nexcess.php

## Example Playbook

    - hosts: php_hosts
      roles:
        - nexcess.php

## License

MIT / BSD
