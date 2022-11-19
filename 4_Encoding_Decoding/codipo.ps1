# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

Clear-Host
Write-Host "Bienvenido a un ejemplo de de/codificacion Base64 usando PowerShell" -ForegroundColor Green
Write-Host "Codificando el archivo de texto"

$file = 'C:\script\secret.txt'
$fc = Get-Content $file
$gb = [System.Text.Encoding]::UTF8.GetBytes($fc)
$enc_text = [System.Convert]::ToBase64String($gb)

Write-Host "El contenido del archivo condificado es:" $enc_text -ForegroundColor Green

Write-Host "Decodificando el archivo de texto"
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($enc_text)) | Out-File -Encoding 'ASCII' 'C:\decoded_secret.txt'
$ofile = Get-Content 'C:\decoded_secret.txt'
Write-Host "El texto decodificado es:" $ofile