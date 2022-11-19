# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

$comando = 'Get-WmiObject win32_logicaldisk | foreach {Write-Host $_.deviceID $_.size $_.freespace}'
$encoded = [System.Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($comando))
Write-Host $encoded
Write-Host "Se ejecutará el siguiente comando: powershell -E" $encoded -ForegroundColor Cyan
Start-Sleep 1
powershell -E $encoded
Start-Sleep 2
$comando_secret = 'RwBlAHQALQBXAG0AaQBPAGIAagBlAGMAdAAgAHcAaQBuADMAMgBfAGIAYQBzAGUAcwBlAHIAdgBpAGMAZQAgAHwAZgBvAHIAZQBhAGMAaAAgAHsAVwByAGkAdABlAC0ASABvAHMAdAAgACQAXwAuAGQAaQBzAHAAbABhAHkAbgBhAG0AZQAgACQAXwAuAHMAdABhAHQAZQB9AA=='
$decoded = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($comando_secret))
Write-Host "El comando codificado es:" $comando_secret -ForegroundColor Cyan
Write-Host "El comando ya sin codificar es:" $decoded -ForegroundColor Cyan