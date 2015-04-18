#/bin/sh

# Tento skript projde cely soubor IP s IP adresama a vytvori soubory ktere jsou pojmenovane podle country codu zemi a do techto souboru pripise vsechny IP adresy pro danou zemi

cat IP |
while read line
do
COUNTRY=$(whois -h ripedb2.nic.cz -- $line | grep country |cut -d: -f2 | sed 's/^ *//;s/ *$//' )
#edvard: pridat zrejme case insensitive
echo $line >> "${COUNTRY}"
done
