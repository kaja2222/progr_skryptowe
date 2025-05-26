
$ip  = Read-Host "podaj ip"
$api = "your api"



Write-Host "podstawowe dane"
$data = Invoke-WebRequest -Uri "https://api.shodan.io/shodan/host/$($ip)?key=$api" | ConvertFrom-Json
$data | select-object "city", "ip", "last_update", "hostnames", "country_name", "domains", "org"

Write-Host "otwarte porty"
$data | select-object "ports"
