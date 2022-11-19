# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

Clear-Host
Write-Host "Ejemplo de codificador Base64 en PowerShell" -ForegroundColor Yellow
Write-Host "Escribe una frase a codificar: " -ForegroundColor Yellow
$frase = Read-Host
$encoded = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($frase))

Write-Host "La frase, en Base64, es:" $encoded -ForegroundColor Yellow