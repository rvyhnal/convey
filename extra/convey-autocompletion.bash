#!/usr/bin/env bash
# bash completion for convey
_convey()
{
  local cur
  local cmd

  cur=${COMP_WORDS[$COMP_CWORD]}
  prev="${COMP_WORDS[COMP_CWORD-1]}";
  cmd=( ${COMP_WORDS[@]} )

  if [[ "$prev" == -f ]] || [[ "$prev" == --field ]] ||  [[ "$prev" == -fe ]] || [[ "$prev" == --field-excluded ]]; then
        COMPREPLY=( $( compgen -W "HostnameTldExternal base64 charset cidr country_name date email first_method formatted_time hostname ip isotimestamp plaintext port quoted_printable second_method time tld unit url urlencode code external reg reg_m reg_s abusemail asn country csirt_contact incident_contact netname prefix a aaaa dmarc mx ns spf txt"  -- "$cur" ) )
        return 0
    fi

  if [[ "$prev" == -a ]] || [[ "$prev" == --aggregate ]]; then
    param=(${cur//,/ })
        COMPREPLY=( $( compgen -W "${param[0]},avg ${param[0]},sum ${param[0]},count ${param[0]},min ${param[0]},max ${param[0]},list ${param[0]},set"  -- "$cur" ) )
        return 0
    fi

  if [[ "$cur" == -* ]]; then
    COMPREPLY=( $( compgen -W "-h --help --debug --testing -F --fresh -R --reprocess -v --verbose -q --quiet -y --yes -H --headless --send --jinja --attach-files --file -i --input -o --output --delimiter --quote-char --header --no-header -d --delete -f --field -fe --field-excluded -t --type --split -s --sort -u --unique -ef --exclude-filter -if --include-filter -a --aggregate --otrs_id --otrs_num --otrs_cookie --otrs_token --csirt-incident --whois --nmap --dig --web --disable-external --json --config --user-agent -S --single-query --single-detect -C --csv-processing --multiple-hostname-ip --multiple-cidr-ip --whois-ttl --show-uml --get-autocompletion --compute-preview --delete-whois-cache --version --server --daemon" -- $cur ) )
    return 0
  fi
}

complete -F _convey -o default convey
